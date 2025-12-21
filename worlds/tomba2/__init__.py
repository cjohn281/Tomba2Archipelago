from typing import Dict, Any

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import World, WebWorld

from .items import Tomba2Item, ITEM_TABLE, ITEM_CLASSIFICATION
from .locations import Tomba2Location, LOCATION_TABLE


class Tomba2WebWorld(WebWorld):
	tutorials = [
		Tutorial(
			tutorial_name="Setup Guide",
			description="Basic setup for Tomba 2 in Archipelago",
			language="English",
			file_name="",
            link="",
			authors=["Chris Johnson"],
		)
	]


class Tomba2World(World):
	game = "Tomba 2"
	web = Tomba2WebWorld()

	origin_region_name = "Start"

	item_name_to_id: Dict[str, int] = ITEM_TABLE
	location_name_to_id: Dict[str, int] = LOCATION_TABLE

	def create_regions(self) -> None:
		start_region = Region("Start", self.player, self.multiworld)

		for name, code in LOCATION_TABLE.items():
			start_region.locations.append(
				Tomba2Location(self.player, name, code, start_region)
			)

		self.multiworld.regions.append(start_region)

	def create_item(self, name: str) -> Tomba2Item:
		code = ITEM_TABLE[name]
		classification = ITEM_CLASSIFICATION.get(name)
		return Tomba2Item(name, classification, code, self.player)

	def create_items(self) -> None:
		for name in ITEM_TABLE.keys():
			self.multiworld.itempool.append(self.create_item(name))

	def set_rules(self) -> None:
		from worlds.generic.Rules import add_item_rule

		forest_loc = self.multiworld.get_location(
			"Village: Starting Chest", self.player
		)
		village_house_loc = self.multiworld.get_location(
			"Village: House Item", self.player
		)
		forest_grapple_loc = self.multiworld.get_location(
			"Forest: First Chest (needs Grapple)", self.player
		)
		beach_swim_loc = self.multiworld.get_location(
			"Beach: Shallow Chest (needs Swim)", self.player
		)

		forest_loc.access_rule = lambda state: True
		village_house_loc.access_rule = lambda state: True

		forest_grapple_loc.access_rule = lambda state: state.has("Grapple", self.player)
		beach_swim_loc.access_rule = lambda state: state.has("Swim", self.player)

	def fill_slot_data(self) -> Dict[str, Any]:
		return {}
