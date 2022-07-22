from pydantic import BaseModel

from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.stats import Stats


class PetItemType(BaseModel):
    rarity: Rarity
    stats: Stats



SPOOKY_CUPCAKE = PetItemType(rarity=Rarity.UNCOMMON, stats=Stats(strength=30, speed=20))
TEXTBOOK = PetItemType(rarity=Rarity.LEGENDARY, stats=Stats())
CROCHET_TIGER_PLUSHIE = PetItemType(rarity=Rarity.EPIC, stats=Stats(attack_speed=35))
DWARF_TURTLE_SHELMET = PetItemType(rarity=Rarity.LEGENDARY, stats=Stats())
# TODO: Add all pet item types
