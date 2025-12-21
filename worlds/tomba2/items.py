from BaseClasses import Item, ItemClassification

class Tomba2Item(Item):
	pass

ITEM_TABLE = {
	"Grapple": 820000,
	"Hammer": 820001,
	"Swim": 820002,
	"Dash": 820003,
}

ITEM_CLASSIFICATION = {
	"Grapple": ItemClassification.progression,
	"Hammer": ItemClassification.progression,
	"Swim": ItemClassification.progression,
	"Dash": ItemClassification.progression,
}
