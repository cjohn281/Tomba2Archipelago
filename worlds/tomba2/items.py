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
	820005: ItemData("Ice Boomerang", 1, ItemClass.progression),
	820006: ItemData("Hammer", 1, ItemClass.progression),

	# Blue Items
	820100: ItemData("Bucket", 1, ItemClass.progression),
	820101: ItemData("Anemone's Hot Dregs", 2, ItemClass.progression),
	820102: ItemData("Banana", 1, ItemClass.progression),
	820103: ItemData("Mudball Surprise", 2, ItemClass.progression),
	820104: ItemData("Low-Purity Lightomight", 1, ItemClass.progression),
	820105: ItemData("Low-Purity Hardonium", 1, ItemClass.progression),
	820106: ItemData("Hi-Purity Lightomight", 1, ItemClass.progression),
	820107: ItemData("Hi-Purity Hardonium", 1, ItemClass.progression),
	
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
	820209: ItemData("Bombs", 1, ItemClass.progression),
	820210: ItemData("Trolley Rail", 1, ItemClass.progression),
	820211: ItemData("Power Coal", 1, ItemClass.progression),
	820212: ItemData("Chick Food x2", 1, ItemClass.progression),
	820213: ItemData("Clay Spatula", 1, ItemClass.progression),
	820214: ItemData("Baked Banana", 1, ItemClass.progression),
	820215: ItemData("Flame Pig Bag", 1, ItemClass.progression),
	820216: ItemData("Traveler's Diary", 1, ItemClass.progression),
	820217: ItemData("Green Key", 1, ItemClass.progression),

	# Consumable Items
	820300: ItemData("Magic Wings", 5, ItemClass.filler),
	820301: ItemData("Magic Wings x2", 2, ItemClass.filler),
	820302: ItemData("Pot of Life (1/2)", 7, ItemClass.useful),
	820303: ItemData("Magic Increase", 2, ItemClass.useful),
	820304: ItemData("Magic Juice", 1, ItemClass.filler),
	820305: ItemData("Ap Gem (1,000)", 1, ItemClass.filler),
	820306: ItemData("Ap Gem (5,000)", 1, ItemClass.filler),
	820307: ItemData("Ap Gem (10,000)", 1, ItemClass.filler),
	820308: ItemData("Lunch Box", 1, ItemClass.filler),
}
