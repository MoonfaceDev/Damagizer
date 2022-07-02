from damagizer.entities.gemstones.slot import GemstoneSlot
from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.stats import Stats
from damagizer.entities.types.weapon import WeaponType


class SwordType(WeaponType):
    gemstone_slots: set[GemstoneSlot] = {}
    attributable: bool = False


CLEAVER = SwordType(rarity=Rarity.UNCOMMON, damage=40, stats=Stats(strength=10))
HYPERION = SwordType(rarity=Rarity.LEGENDARY, damage=260, stats=Stats(strength=150, intelligence=350, ferocity=30),
                     gemstone_slots={GemstoneSlot.SAPPHIRE, GemstoneSlot.COMBAT})
# TODO: Add all sword types
