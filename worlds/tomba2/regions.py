from typing import TYPE_CHECKING
from .locations import location_table, Tomba2Location
from BaseClasses import Region, Entrance

if TYPE_CHECKING:
  from . import Tomba2World

def create_regions(tomba2_world: "Tomba2World") -> None:
  player = tomba2_world.player
  mw = tomba2_world.multiworld

  town_region = Region("Town of the Fishermen", player, mw)
  waterfall_region = Region("Waterfall of the Heavens", player, mw)
  pipe_region = Region("Pipe Area", player, mw)
  mining_town_region = Region("Coal-Mining Town", player, mw)

  #Assign locations to their respective regions based on name prefix
  town_locations = {
    data.full_name: loc_id
    for loc_id, data in location_table.items()
    if data.prefix == "TotF"
  }

  waterfall_locations = {
    data.full_name: loc_id
    for loc_id, data in location_table.items()
    if data.prefix == "WotH"
  }

  pipe_locations = {
    data.full_name: loc_id
    for loc_id, data in location_table.items()
    if data.prefix == "PA"
  }

  mining_town_locations = {
    data.full_name: loc_id
    for loc_id, data in location_table.items()
    if data.prefix == "CMT"
  }

  if town_locations:
    town_region.add_locations(town_locations, Tomba2Location)
  if waterfall_locations:
    waterfall_region.add_locations(waterfall_locations, Tomba2Location)
  if pipe_locations:
    pipe_region.add_locations(pipe_locations, Tomba2Location)
  if mining_town_locations:
    mining_town_region.add_locations(mining_town_locations, Tomba2Location)

  #Connect regions: Town -> Waterfall
  town_to_waterfall = Entrance(player, "Town->Waterfall", town_region)
  town_region.exits.append(town_to_waterfall)
  town_to_waterfall.connect(waterfall_region)

  #Connect regions: Waterfall -> Pipe Area
  waterfall_to_pipe = Entrance(player, "Waterfall->Pipe", waterfall_region)
  waterfall_region.exits.append(waterfall_to_pipe)
  waterfall_to_pipe.connect(pipe_region)

  #Connect regions: Pipe Area -> Coal-Mining Town
  pipe_to_mining_town = Entrance(player, "Pipe->MiningTown", pipe_region)
  pipe_region.exits.append(pipe_to_mining_town)
  pipe_to_mining_town.connect(mining_town_region)


  mw.regions.append(town_region)
  mw.regions.append(waterfall_region)
  mw.regions.append(pipe_region)
  mw.regions.append(mining_town_region)