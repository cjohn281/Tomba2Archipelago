from BaseClasses import Location
from typing import NamedTuple, Dict, Tuple


LocPre: Dict[str, str] = {
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


class Tomba2Location(Location):
	pass


class LocationData(NamedTuple):
	prefix: str
	name: str
	requirements: Tuple[Tuple[str, int], ...] = ()

	@property
	def full_name(self) -> str:
		return f"{LocPre[self.prefix]}{self.name}"


location_table: Dict[int, LocationData] = {
	# Town of the Fisherman 8300xx
	830000: LocationData("TotF", "Seesaw 1 Chick"),
	830001: LocationData("TotF", "Seesaw 2 Chick"),
	830002: LocationData("TotF", "Magic Flower"),
	830003: LocationData("TotF", "Rare Fish"),
	830004: LocationData("TotF", "Bucket"),
	830005: LocationData("TotF", "Above Climbable Pole"),
	830006: LocationData("TotF", "Fish Drying Net"),
	830007: LocationData("TotF", "Kainen",(("Bucket", 1),)),
	830008: LocationData("TotF", "Net Bridge",(("Star-Shaped Cog", 1),)),

	# Town of the Fisherman Chests
	830009: LocationData("TotF", "Red Chest near burning house",(("Red Key", 1),)),
	830010: LocationData("TotF", "Red Chest above the third seesaw",(("Red Key", 1),)),
	830011: LocationData("TotF", "Red Chest past the second seesaw",(("Red Key", 1),)),
	# 830012: LocationData("TotF", "Green Chest above the third seesaw",(("Green Key", 1),("Grapple", 1),)),
	# 830013: LocationData("TotF", "Green Chest midair past the second seesaw",(("Green Key", 1),)),
	
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
	# 830019: LocationData("WotH", "Green Chest (Low)",(("Green Key", 1),)),
	# 830020: LocationData("WotH", "Green Chest (High)",(("Green Key", 1),("Grapple", 1),)),
	# 830021: LocationData("WotH", "Alcove Green Chest",(("Green Key", 1),)),
	# 830022: LocationData("WotH", "Blue Chest above Windmill Shed",(("Blue Key", 1),)),
	# 830023: LocationData("WotH", "Blue Chest below seesaws",(("Blue Key", 1),)),

	# Pipe Area 8302xx
	

	# Pipe Area Chests


	# Coal-Mining Town 8303xx


	# Coal-Mining Town Chests


	# Ranch Area 8304xx


	# Ranch Area Chests


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