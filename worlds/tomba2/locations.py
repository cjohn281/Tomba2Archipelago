from BaseClasses import Location
from typing import NamedTuple, Dict, Tuple


location_prefix: Dict[str, str] = {
	"TotF": "Town of the Fishermen - ",
	"WotH": "Waterfall of the Heavens - ",
	"PA": "Pipe Area - ",
	"CMT": "Coal-Mining Town - ",
	"KR": "Kujara Ranch Area - ",
	"KRS": "Kujara Ranch Summit - ",
	"DongF": "Donglin Forest - ",
	"DeepF": "Deep Forest - ",
	"CV": "Circus Village - ",
	"WT": "Water Temple - ",
}

req_group: Dict[str, Tuple[Tuple[str, int], ...]] = {
 "grapple_group": (("Grapple", 1),("Doka Pin", 1)),
 "hammer_group": (("Hammer", 1),("Fire Hammer", 1), ("Torch Hammer", 1)),
 "boomerang_group": (("Boomerang", 1),("Ice Boomerang", 1), ("Glacier Boomerang", 1)),
 "flying_group": (("Bird Clothes", 1),("Squirrel Clothes", 1)),
 "fire_group": (("Fire Hammer", 1),("Torch Hammer", 1)),
 "ice_group": (("Ice Boomerang", 1),("Glacier Boomerang", 1)),
 "bucket_group": (("Bucket", 1),("Mermaid Bucket", 1)),
}


class Tomba2Location(Location):
	pass



class LocationData(NamedTuple):
	prefix: str
	name: str
	req_all: Tuple[Tuple[str, int], ...] = ()
	req_any: Tuple[Tuple[str, int], ...] = ()

	@property
	def full_name(self) -> str:
		return f"{location_prefix[self.prefix]}{self.name}"


location_table: Dict[int, LocationData] = {
	# Town of the Fisherman 8300xx
	830000: LocationData("TotF", "Magic Flower", (), req_group["bucket_group"]),
	830001: LocationData("TotF", "Seesaw 1 Chick"),
	830002: LocationData("TotF", "Seesaw 2 Chick"),
	830003: LocationData("TotF", "Rare Fish"),
	830004: LocationData("TotF", "Bucket"),
	830005: LocationData("TotF", "Above Climbable Pole"),
	830006: LocationData("TotF", "Fish Drying Net"),
	830007: LocationData("TotF", "Kainen", (), req_group["bucket_group"]),
	830008: LocationData("TotF", "Net Bridge",(("Star-Shaped Cog", 1),)),

	# Town of the Fisherman Chests
	830009: LocationData("TotF", "Red Chest near burning house",(("Red Key", 1),)),
	830010: LocationData("TotF", "Red Chest above the third seesaw",(("Red Key", 1),)),
	830011: LocationData("TotF", "Red Chest past the second seesaw",(("Red Key", 1),)),
	# 830012: LocationData("TotF", "Green Chest above the third seesaw",(("Green Key", 1)), req_group["grapple_group"]),
	830013: LocationData("TotF", "Green Chest midair past the second seesaw",(("Green Key", 1),)),
	
	# Waterfall of the Heavens 8301xx
	830100: LocationData("WotH", "First Pig"),
	830101: LocationData("WotH", "Between Aquatic Plants"),
	830102: LocationData("WotH", "Platform Crab",(("Crab Basket", 1),)),
	830103: LocationData("WotH", "Near Windmill Shed"),
	830104: LocationData("WotH", "Tower Roof Crab",(("Crab Basket", 1),)),
	830105: LocationData("WotH", "Fisherman"),
	830106: LocationData("WotH", "Kainen",(("Golden Crab", 3),)),
	830107: LocationData("WotH", "Adventurer's Chest (30,000 AP)"),

	# Waterfall of the Heavens Chests
	830108: LocationData("WotH", "Tower Red Chest",(("Red Key", 1),)),
	830109: LocationData("WotH", "Red Chest about barrel platforms",(("Red Key", 1),)),
	830110: LocationData("WotH", "Windmill Shed Red Chest",(("Red Key", 1),)),
	830019: LocationData("WotH", "Green Chest (Low)",(("Green Key", 1),)),
	# 830020: LocationData("WotH", "Green Chest (High)",(("Green Key", 1),("Grapple", 1),)),
	# 830021: LocationData("WotH", "Alcove Green Chest",(("Green Key", 1),)),
	# 830022: LocationData("WotH", "Blue Chest above Windmill Shed",(("Blue Key", 1),)),
	# 830023: LocationData("WotH", "Blue Chest below seesaws",(("Blue Key", 1),)),

	# Pipe Area 8302xx
	830200: LocationData("PA", "Ice Boomerang"),
	830201: LocationData("PA", "Flaming Anemone 1",(("Ice Boomerang", 1),)),
	830202: LocationData("PA", "Flaming Anemone 2",(("Ice Boomerang", 1),)),
	830203: LocationData("PA", "Bridge Magic Wings"),
	830204: LocationData("PA", "Banana"),
	830205: LocationData("PA", "Platform below bridge"),
	830206: LocationData("PA", "Powder Room", (("Hammer", 1),)),
	830207: LocationData("PA", "Magic Flower", (("Bucket", 1),)),
	830208: LocationData("PA", "Hammer", (("Ice Boomerang", 1),)),
	830209: LocationData("PA", "Gran", (("Hammer", 1), ("Bombs", 1),)),

	# Pipe Area Chests
	830210: LocationData("PA", "Flaming Red Chest",(("Red Key", 1),("Ice Boomerang", 1),)),
	830211: LocationData("PA", "Platform Red Chest 1",(("Red Key", 1),)),
	830212: LocationData("PA", "Platform Red Chest 2",(("Red Key", 1), ("Ice Boomerang", 1),)),
	830213: LocationData("PA", "Platform Red Chest 3",(("Red Key", 1), ("Hammer", 1),)),
	830214: LocationData("PA", "Platform Red Chest 4",(("Red Key", 1),)),

	# Coal-Mining Town 8303xx
	830300: LocationData("CMT", "Broken Pot"),
	830301: LocationData("CMT", "Wash Mudball Surprise 1", (("Mudball Surprise", 1),)),
	830302: LocationData("CMT", "Wash Mudball Surprise 2", (("Mudball Surprise", 1),)),
	830303: LocationData("CMT", "Bake the banana", (("Banana", 1),("Hammer", 1),)),
	830304: LocationData("CMT", "Heat the Low-Purity Lightomight", (("Low-Purity Lightomight", 1),("Hammer", 1),("Power Coal", 1))),
	830305: LocationData("CMT", "Heat the Low-Purity Hardonium", (("Low-Purity Hardonium", 1),("Hammer", 1),("Power Coal", 1))),
	830306: LocationData("CMT", "Flame Pig Bag", (("Trolley Rail", 1),("Hammer", 1),("Bombs", 1),)),

	# Coal-Mining Town Chests
	830307: LocationData("CMT", "Gran's House Red Chest",(("Red Key", 1),)),
	830308: LocationData("CMT", "Tabby's House Red Chest",(("Red Key", 1),)),

	# Ranch Area 8304xx
	830400: LocationData("KR", "Traveler",(("Traveler's Diary", 1),)),

	# Ranch Area Chests
	830401: LocationData("KR", "Chimney Shed Red Chest",(("Red Key", 1),)),


	# Ranch Summit 8305xx


	# Ranch Summit Chests


	# Donglin Forest 8306xx


	# Donglin Forest Chests


	# Deep Forest 8307xx


	# Deep Forest Chests


	# Circus Village 8308xx


	# Circus Village Chests


	# Water Temple 8309xx


	# Water Temple Chests


	# Mouse Village 8310xx


	# Mouse Village Chests


	# Towers 8311xx


	# Tower Chests


	# Underground Mine 8312xx


	# Underground Mine Chests


	# Evil Pigs 8313xx
}