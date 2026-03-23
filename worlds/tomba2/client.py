from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Optional, Set

import worlds._bizhawk as bizhawk
from NetUtils import ClientStatus
from worlds._bizhawk.client import BizHawkClient
from Utils import messagebox

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

logger = logging.getLogger("Client")


class Tomba2Client(BizHawkClient):
    """BizHawk client for Tomba 2 using the generic BizHawk connector.

    This is a minimal skeleton wired for your .aptomba2 patches. It:
    - Validates that the loaded ROM looks like Tomba 2.
    - Checks for a future Archipelago marker string in ROM to distinguish
      patched vs vanilla images (TODO once you decide an offset).
    - Sets up basic connection/auth handling so you can later add real
      memory-based location checking and item receiving.
    """

    game = "Tomba 2"
    # BizHawk's PS1 system id is "PSX".
    system = "PSX"
    patch_suffix = ".aptomba2"

    # Example state you might keep; kept here for future expansion.
    local_checked_locations: Set[int]
    rom_auth_bytes: Optional[bytes]

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.rom_auth_bytes = None

    # async def validate_rom(self, ctx):
    #   import logging
    #   logger = logging.getLogger("Client")

    #   try:
    #       system = await bizhawk.get_system(ctx.bizhawk_ctx)
    #       if system != "PSX":
    #           return False

    #       logger.info("Tomba 2 validate_rom called, forcing attach.")
    #       ctx.game = self.game
    #       ctx.items_handling = 0b001
    #       ctx.want_slot_data = False
    #       ctx.watcher_timeout = 0.25
    #       return True
    #   except bizhawk.RequestFailedError:
    #       return False

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        logger = logging.getLogger("Client")

        try:
            # 1) Verify we are on the correct system.
            system = await bizhawk.get_system(ctx.bizhawk_ctx)
            if system != "PSX":
                return False

            # 2) Check that this looks like Tomba 2 by SCUS/ID in MainRAM.
            read_game_id = await bizhawk.guarded_read(
                ctx.bizhawk_ctx,
                [(0x00928C, 12, "MainRAM")],
                [(0x00928C, b'\x53\x43\x55\x53\x5f\x39\x34\x34\x2e\x35\x34\x3B', "MainRAM")])

            if read_game_id is None:
                return False

            # 3) Require the AP marker in MainRAM at the address where the
            #    patched MAIN.EXE string appears once loaded.
            #
            # We write "A01TMBA2" into MAIN.EXE at exe offset 0x009CE70.
            # When the game loads this into RAM, that data shows up at
            # MainRAM address 0x00AC670.
            marker_result = await bizhawk.guarded_read(
                ctx.bizhawk_ctx,
                [(0x00AC670, 10, "MainRAM")],
                [(0x00AC670, b"A01TMBA2", "MainRAM")],
            )

            if marker_result is None:
                return False

            # If we got here, treat this as a valid Tomba 2 AP ROM.
            ctx.game = self.game
            ctx.items_handling = 0b001  # receive items from server, no sending of our items yet
            ctx.want_slot_data = False
            ctx.watcher_timeout = 0.25
            return True
        except (UnicodeDecodeError, bizhawk.RequestFailedError):
          logger.error("Failed to validate Tomba 2 ROM.")
          return False

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        """Set ctx.auth based on ROM data, once you decide where to store it.

        For now, this falls back to prompting the user (ctx.auth stays None).
        Later you can do something like:

            auth_raw = (await bizhawk.read(ctx.bizhawk_ctx, [(marker_addr + 0x10, 16, "ROM")]))[0]
            ctx.auth = base64.b64encode(auth_raw).decode("utf-8")
        """

        # Leaving ctx.auth unset will cause the client to prompt for a name.
        return

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        """Main loop for memory polling.

        This is currently a no-op skeleton. Once you know your RAM layout you
        can:
        - Read flags/collectibles to determine newly checked locations and
          send `LocationChecks`.
        - Detect goal completion and send a `StatusUpdate` with
          `ClientStatus.CLIENT_GOAL`.
        - Apply incoming items by writing to PS1 RAM via BizHawk.
        """

        try:
            # Example placeholder: nothing yet, just ensure we still have a
            # valid connector and ROM.
            await bizhawk.ping(ctx.bizhawk_ctx)
            # When you implement logic, do your guarded_read/write here.
        except bizhawk.RequestFailedError:
            # Connector is having issues; let the outer loop handle reconnect.
            pass
