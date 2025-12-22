from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule, add_rule  # imported for future use
from .locations import location_table

if TYPE_CHECKING:
  from . import Tomba2World
  from BaseClasses import CollectionState


def require_all(state, player, reqs):
  return all(state.has(item, player, count) for item, count in reqs)


def has_waterfall_access(state: "CollectionState", player: int) -> bool:
  return state.has("Star-Shaped Cog", player)

def has_pipe_area_access(state: "CollectionState", player: int) -> bool:
  return state.has("Golden Crab", player, 3)


def set_rules(tomba2_world: "Tomba2World") -> None:
  player = tomba2_world.player
  mw = tomba2_world.multiworld


  # Goal: reach the Windmill Shed Red Chest check in Waterfall of the Heavens
  mw.completion_condition[player] = lambda state: (
    state.can_reach_location(
      "Waterfall of the Heavens - Windmill Shed Red Chest", player
    )
    and state.has("Red Key", player)
  )


  # Region access rules
  town_to_waterfall = mw.get_entrance(
    "Town->Waterfall", player
  ).access_rule = lambda state: has_waterfall_access(state, player)

  waterfall_to_pipe = mw.get_entrance(
    "Waterfall->Pipe", player
  ).access_rule = lambda state: has_pipe_area_access(state, player)


  # Location access rules
  for loc_id, data in location_table.items():
    if not data.requirements:
      continue
    loc = mw.get_location(data.full_name, player)
    reqs = data.requirements
    loc.access_rule = lambda state, reqs=reqs: require_all(state, player, reqs)