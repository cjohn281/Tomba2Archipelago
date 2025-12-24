from typing import Dict, Any

from BaseClasses import Region, Tutorial, Entrance
from worlds.AutoWorld import World, WebWorld

from .items import Tomba2Item, item_table
from .locations import Tomba2Location, location_table
from .rules import set_rules
from .regions import create_regions


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
	game = "Tomba 2"
	web = Tomba2WebWorld()

	origin_region_name = "Town of the Fishermen"

	item_name_to_id = {data.name: item_id for item_id, data in item_table.items()}
	location_name_to_id = {data.full_name: loc_id for loc_id, data in location_table.items()}


	def create_item(self, name: str) -> Tomba2Item:
		item_id = self.item_name_to_id[name]
		return Tomba2Item(name, item_table[item_id].classification, item_id, self.player)

	def create_items(self) -> None:
		starting_weapons = ["Blackjack", "Boomerang"]
		starting_pants = ["Green Pants", "Fast Pants"]

		weapon_choice = self.multiworld.random.choice(starting_weapons)
		pants_choice = self.multiworld.random.choice(starting_pants)
		starting_items = {weapon_choice, pants_choice}

		chicks = self.multiworld.random.choices(["Red Chick", "Blue Chick"], k=2)
		for name in chicks:
			self.multiworld.itempool.append(self.create_item(name))

		for id in item_table.keys():
			quantity = item_table[id].count
			if item_table[id].name in starting_items:
				quantity -= 1
			if item_table[id].name in {"Red Chick", "Blue Chick"}:
				continue	# Chicks are handled above
			for _ in range(max(quantity, 0)):
				self.multiworld.itempool.append(self.create_item(item_table[id].name))

		for item_name in starting_items:
			self.multiworld.push_precollected(self.create_item(item_name))


	create_regions = create_regions
	set_rules = set_rules


	def fill_slot_data(self) -> Dict[str, Any]:
		return {}
