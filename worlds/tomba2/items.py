from BaseClasses import Item, ItemClassification as ItemClass
from typing import NamedTuple, Dict


class Tomba2Item(Item):
	game = "Tomba! 2: The Evil Swine Return Special Edition"


class ItemData(NamedTuple):
		name: str
		count: int
		classification: ItemClass


item_table: Dict[int, ItemData] = {
	# Green Items
	820000: ItemData("Blackjack", 1, ItemClass.progression),
	820001: ItemData("Green Pants", 1, ItemClass.useful),
	820002: ItemData("Boomerang", 1, ItemClass.progression),
	820003: ItemData("Bird Clothes", 1, ItemClass.progression),
	820004: ItemData("Fast Pants", 1, ItemClass.useful),

	# Blue Items
	820100: ItemData("Bucket", 1, ItemClass.progression),
	
	# Pink Items
	820200: ItemData("Red Chick", 0, ItemClass.progression),
	820201: ItemData("Blue Chick", 0, ItemClass.progression),
	820202: ItemData("Rare Fish", 1, ItemClass.progression),
	820203: ItemData("Star-Shaped Cog", 1, ItemClass.progression),
	820204: ItemData("Crab Basket", 1, ItemClass.progression),
	820205: ItemData("Spoon", 1, ItemClass.progression),
	820206: ItemData("Red Key", 1, ItemClass.progression),
	820207: ItemData("Golden Crab", 3, ItemClass.progression),
	820208: ItemData("Pig Nose Panel", 1, ItemClass.progression),

	# Consumable Items
	820300: ItemData("Magic Wings", 3, ItemClass.filler),
	820301: ItemData("Magic Wings x2", 1, ItemClass.filler),
	820302: ItemData("Pot of Life (1/2)", 6, ItemClass.useful),
	820303: ItemData("Magic Increase", 2, ItemClass.useful),
	820304: ItemData("Magic Juice", 1, ItemClass.filler),
	820305: ItemData("Ap Gem (5,000)", 1, ItemClass.filler),
	820306: ItemData("Ap Gem (10,000)", 1, ItemClass.filler),
}
