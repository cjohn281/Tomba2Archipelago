from typing import Dict, Any, ClassVar

import settings
from BaseClasses import Region, Tutorial, Entrance
from worlds.AutoWorld import World, WebWorld

from .items import Tomba2Item, item_table
from .locations import Tomba2Location, location_table
from .rules import set_rules
from .regions import create_regions
from .romhandler import Tomba2ProcedurePatch, write_patch
from .client import Tomba2Client  # ensure BizHawk client (and .aptomba2 suffix) is registered


class Tomba2Settings(settings.Group):
	class RomFile(settings.UserFilePath):
		"""File name of the Tomba 2 Track 1 image"""

		description = "Tomba 2 Track 1 BIN file"
		copy_to = "Tomba! 2 - The Evil Swine Return (Track 1).bin"
		# md5s can be filled in once a canonical ROM is chosen.
		md5s: list[str] = []

	rom_file: RomFile = RomFile(RomFile.copy_to)

	class AudioFile(settings.UserFilePath):
		"""File name of the Tomba 2 Track 2 (audio) image"""

		description = "Tomba 2 Track 2 BIN file"
		copy_to = "Tomba! 2 - The Evil Swine Return (Track 2).bin"
		md5s: list[str] = []

	audio_file: AudioFile = AudioFile(AudioFile.copy_to)


class Tomba2WebWorld(WebWorld):
	tutorials = [
		Tutorial(
			tutorial_name="Setup Guide",
			description="Basic setup for Tomba 2 in Archipelago",
			language="English",
			file_name="",
			link="",
			authors=["clickspark"],
		)
	]


class Tomba2World(World):
	game: ClassVar[str] = "Tomba 2"
	web: ClassVar[WebWorld] = Tomba2WebWorld()
	settings_key: ClassVar[str] = "tomba2_settings"
	settings: ClassVar[Tomba2Settings]

	origin_region_name = "Town of the Fishermen"

	item_name_to_id = {data.name: item_id for item_id, data in item_table.items()}
	location_name_to_id = {data.full_name: loc_id for loc_id, data in location_table.items()}


	def create_item(self, name: str) -> Tomba2Item:
		item_id = self.item_name_to_id[name]
		return Tomba2Item(name, item_table[item_id].classification, item_id, self.player)

	def create_items(self) -> None:
		# Original item generation logic (depends on many items not yet in item_table):
		# starting_weapons = ["Blackjack", "Boomerang", "Ice Boomerang", "Hammer"]
		# starting_pants = ["Green Pants", "Fast Pants"]
		#
		# weapon_choice = self.multiworld.random.choice(starting_weapons)
		# pants_choice = self.multiworld.random.choice(starting_pants)
		# starting_items = {weapon_choice, pants_choice}
		#
		# chicks = self.multiworld.random.choices(["Red Chick", "Blue Chick"], k=2)
		# for name in chicks:
		# 	self.multiworld.itempool.append(self.create_item(name))
		#
		# for id in item_table.keys():
		# 	quantity = item_table[id].count
		# 	if item_table[id].name in starting_items:
		# 		quantity -= 1
		# 	if item_table[id].name in {"Red Chick", "Blue Chick"}:
		# 		continue	# Chicks are handled above
		# 	for _ in range(max(quantity, 0)):
		# 		self.multiworld.itempool.append(self.create_item(item_table[id].name))
		#
		# for item_name in starting_items:
		# 	self.multiworld.push_precollected(self.create_item(item_name))

		# Temporary simple pool: generate exactly item_table.count copies of
		# every defined item. This avoids KeyError for items that don't yet
		# exist in item_table (e.g., "Blue Chick").
		for item_id, data in item_table.items():
			for _ in range(max(data.count, 0)):
				self.multiworld.itempool.append(self.create_item(data.name))


	create_regions = create_regions
	set_rules = set_rules


	def fill_slot_data(self) -> Dict[str, Any]:
		return {}

	def generate_output(self, output_directory: str) -> None:
		"""Create a per-player patch file for this Tomba 2 slot.

		This is called by the generator in a thread pool after items and
		locations have been assigned. It produces a .apt2se file that can be
		fed to Archipelago's Patch.py (and ultimately to BizHawk) to obtain a
		patched PS1 image.
		"""

		out_file_base = self.multiworld.get_out_file_name_base(self.player)
		patch = Tomba2ProcedurePatch(
			player=self.player,
			player_name=self.multiworld.player_name[self.player],
		)
		write_patch(self, patch)

		import os
		patch_path = os.path.join(output_directory, f"{out_file_base}{patch.patch_file_ending}")
		patch.write(patch_path)
