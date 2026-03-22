from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule, add_rule  # imported for future use
from .locations import location_table, req_group

if TYPE_CHECKING:
  from . import Tomba2World
  from BaseClasses import CollectionState


def require_all(state, player, reqs):
  return all(state.has(item, player, count) for item, count in reqs)


def require_any(state, player, reqs):
  return any(state.has(item, player, count) for item, count in reqs)


def has_waterfall_access(state: "CollectionState", player: int) -> bool:
  return state.has("Star-Shaped Cog", player)

def has_pipe_area_access(state: "CollectionState", player: int) -> bool:
  return state.has("Golden Crab", player, 3)

def has_mining_town_access(state: "CollectionState", player: int) -> bool:
  return require_any(state, player, req_group["ice_group"])

def has_ranch_access(state: "CollectionState", player: int) -> bool:
  return (
    require_any(state, player, req_group["hammer_group"])
    and state.has("Bombs", player, 1)
    and state.has("Trolley Rail", player, 1)
  )


def set_rules(tomba2_world: "Tomba2World") -> None:
  player = tomba2_world.player
  mw = tomba2_world.multiworld


  # Original goal (requires many unfinished locations/items):
  # mw.completion_condition[player] = lambda state: (
  #   state.can_reach_location(
  #     "Coal-Mining Town - Flame Pig Bag", player
  #   )
  #   and state.has("Flame Pig Bag", player)
  # )

  # Barebones goal for a minimal world: beat the game when the
  # player has the single progression item defined in item_table
  # (currently "Magic Wings"). This avoids referencing locations
  # that aren't in location_table yet.
  mw.completion_condition[player] = lambda state: state.has("Magic Wings", player)


  # Region access rules
  town_to_waterfall = mw.get_entrance(
    "Town->Waterfall", player
  ).access_rule = lambda state: has_waterfall_access(state, player)

  waterfall_to_pipe = mw.get_entrance(
    "Waterfall->Pipe", player
  ).access_rule = lambda state: has_pipe_area_access(state, player)

  pipe_to_coal_mining = mw.get_entrance(
    "Pipe->MiningTown", player
  ).access_rule = lambda state: has_mining_town_access(state, player)

  coal_mining_to_ranch = mw.get_entrance(
    "MiningTown->Ranch", player
  ).access_rule = lambda state: has_ranch_access(state, player)


  # Location access rules
  for loc_id, data in location_table.items():
    reqs_all = data.req_all
    reqs_any = data.req_any

    # Skip locations with no requirements at all
    if not reqs_all and not reqs_any:
      continue

    loc = mw.get_location(data.full_name, player)

    # Require all items in reqs_all, plus at least one item in reqs_any (if any)
    loc.access_rule = (
      lambda state, reqs_all=reqs_all, reqs_any=reqs_any: (
        require_all(state, player, reqs_all)
        and (not reqs_any or require_any(state, player, reqs_any))
      )
    )