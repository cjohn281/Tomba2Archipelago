from typing import TYPE_CHECKING, Dict
from .locations import location_table, Tomba2Location
from BaseClasses import Region, Entrance

if TYPE_CHECKING:
  from . import Tomba2World

def create_regions(tomba2_world: "Tomba2World") -> None:
  player = tomba2_world.player
  mw = tomba2_world.multiworld

  town_locations = {}
  waterfall_locations = {}
  pipe_locations = {}
  mining_town_locations = {}
  ranch_locations = {}
  ranch_summit_locations = {}
  forest_locations = {}
  deep_forest_locations = {}
  circus_locations = {}
  water_temple_locations = {}

  town_region = Region("Town of the Fishermen", player, mw)
  waterfall_region = Region("Waterfall of the Heavens", player, mw)
  pipe_region = Region("Pipe Area", player, mw)
  mining_town_region = Region("Coal-Mining Town", player, mw)
  ranch_region = Region("Ranch Area", player, mw)
  ranch_summit_region = Region("Ranch Summit", player, mw)
  forest_region = Region("Donglin Forest", player, mw)
  deep_forest_region = Region("Deep Forest", player, mw)
  circus_region = Region("Circus Village", player, mw)
  water_temple_region = Region("Water Temple", player, mw)

  #Assign locations to their respective regions based on name prefix
  for loc_id, data in location_table.items():
    match data.prefix:
      case "TotF":
        town_locations[data.full_name] = loc_id
      case "WotH":
        waterfall_locations[data.full_name] = loc_id
      case "PA":
        pipe_locations[data.full_name] = loc_id
      case "CMT":
        mining_town_locations[data.full_name] = loc_id
      case "KR":
        ranch_locations[data.full_name] = loc_id
      case "KRS":
        ranch_summit_locations[data.full_name] = loc_id
      case "DongF":
        forest_locations[data.full_name] = loc_id
      case "DeepF":
        deep_forest_locations[data.full_name] = loc_id
      case "CV":
        circus_locations[data.full_name] = loc_id
      case "WT":
        water_temple_locations[data.full_name] = loc_id

  # town_locations: Dict[str, int]   = {
  #   data.full_name: loc_id
  #   for loc_id, data in location_table.items()
  #   if data.prefix == "TotF"
  # }

  # waterfall_locations = {
  #   data.full_name: loc_id
  #   for loc_id, data in location_table.items()
  #   if data.prefix == "WotH"
  # }

  # pipe_locations = {
  #   data.full_name: loc_id
  #   for loc_id, data in location_table.items()
  #   if data.prefix == "PA"
  # }

  # mining_town_locations = {
  #   data.full_name: loc_id
  #   for loc_id, data in location_table.items()
  #   if data.prefix == "CMT"
  # }

  if town_locations:
    town_region.add_locations(town_locations, Tomba2Location)
  if waterfall_locations:
    waterfall_region.add_locations(waterfall_locations, Tomba2Location)
  if pipe_locations:
    pipe_region.add_locations(pipe_locations, Tomba2Location)
  if mining_town_locations:
    mining_town_region.add_locations(mining_town_locations, Tomba2Location)
  if ranch_locations:
    ranch_region.add_locations(ranch_locations, Tomba2Location)
  if ranch_summit_locations:
    ranch_summit_region.add_locations(ranch_summit_locations, Tomba2Location)
  if forest_locations:
    forest_region.add_locations(forest_locations, Tomba2Location)
  if deep_forest_locations:
    deep_forest_region.add_locations(deep_forest_locations, Tomba2Location)
  if circus_locations:
    circus_region.add_locations(circus_locations, Tomba2Location)
  if water_temple_locations:
    water_temple_region.add_locations(water_temple_locations, Tomba2Location)

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

  #Connect regions: Coal-Mining Town -> Ranch Area
  mining_town_to_ranch = Entrance(player, "MiningTown->Ranch", mining_town_region)
  mining_town_region.exits.append(mining_town_to_ranch)
  mining_town_to_ranch.connect(ranch_region)

  #Connect regions: Ranch Area -> Ranch Summit
  ranch_to_ranch_summit = Entrance(player, "Ranch->RanchSummit", ranch_region)
  ranch_region.exits.append(ranch_to_ranch_summit)
  ranch_to_ranch_summit.connect(ranch_summit_region)

  #Connect regions: Ranch Summit -> Donglin Forest
  ranch_summit_to_forest = Entrance(player, "RanchSummit->DonglinForest", ranch_summit_region)
  ranch_summit_region.exits.append(ranch_summit_to_forest)
  ranch_summit_to_forest.connect(forest_region)

  #Connect regions: Donglin Forest -> Deep Forest
  forest_to_deep_forest = Entrance(player, "DonglinForest->DeepForest", forest_region)
  forest_region.exits.append(forest_to_deep_forest)
  forest_to_deep_forest.connect(deep_forest_region)

  #Connect regions: Deep Forest -> Circus Village
  deep_forest_to_circus = Entrance(player, "DeepForest->CircusVillage", deep_forest_region)
  deep_forest_region.exits.append(deep_forest_to_circus)
  deep_forest_to_circus.connect(circus_region)

  #Connect regions: Circus Village -> Water Temple
  circus_to_water_temple = Entrance(player, "CircusVillage->WaterTemple", circus_region)
  circus_region.exits.append(circus_to_water_temple)
  circus_to_water_temple.connect(water_temple_region)


  mw.regions.append(town_region)
  mw.regions.append(waterfall_region)
  mw.regions.append(pipe_region)
  mw.regions.append(mining_town_region)
  mw.regions.append(ranch_region)
  mw.regions.append(ranch_summit_region)
  mw.regions.append(forest_region)
  mw.regions.append(deep_forest_region)
  mw.regions.append(circus_region)
  mw.regions.append(water_temple_region)