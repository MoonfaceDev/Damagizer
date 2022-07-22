from damagizer.entities.gemstones.slot import GemstoneSlot
from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.stats import Stats
from damagizer.entities.types.weapon import WeaponType


class BowType(WeaponType):
    pass


BOW = BowType(rarity=Rarity.COMMON, damage=30, stats=Stats())
DECENT_BOW = BowType(rarity=Rarity.UNCOMMON, damage=45, stats=Stats())
ARTISANAL_SHORTBOW = BowType(rarity=Rarity.RARE, damage=40, stats=Stats())
WITHER_BOW = BowType(rarity=Rarity.UNCOMMON, damage=30, stats=Stats())
PRISMARINE_BOW = BowType(rarity=Rarity.UNCOMMON, damage=50, stats=Stats(strength=25))
SAVANA_BOW = BowType(rarity=Rarity.UNCOMMON, damage=50, stats=Stats())
ENDER_BOW = BowType(rarity=Rarity.RARE, damage=60, stats=Stats())
END_STONE_BOW = BowType(rarity=Rarity.EPIC, damage=140, stats=Stats())
SLIME_BOW = BowType(rarity=Rarity.EPIC, damage=100, stats=Stats(crit_damage=50))
HURRICANE_BOW = BowType(rarity=Rarity.EPIC, damage=120, stats=Stats(strength=50))
RUNAANS_BOW = BowType(rarity=Rarity.LEGENDARY, damage=160, stats=Stats(strength=50))
EXPLOSIVE_BOW = BowType(rarity=Rarity.EPIC, damage=100, stats=Stats(strength=20))
MAGMA_BOW = BowType(rarity=Rarity.EPIC, damage=120, stats=Stats(strength=120))
SULPHUR_BOW = BowType(rarity=Rarity.EPIC, damage=200, stats=Stats(strength=100), gemstone_slots={GemstoneSlot.COMBAT})
SPIDER_QUEENS_STINGER = BowType(rarity=Rarity.EPIC, damage=180, stats=Stats())
VENOMS_TOUCH = BowType(rarity=Rarity.EPIC, damage=200, stats=Stats(strength=100))
SOULS_REBOUND = BowType(rarity=Rarity.EPIC, damage=450, stats=Stats())
SCORPION_BOW = BowType(rarity=Rarity.EPIC, damage=110, stats=Stats(strength=10))
MOSQUITO_BOW = BowType(rarity=Rarity.LEGENDARY, damage=251, stats=Stats(strength=151, crit_damage=39))
JUJU_SHORTBOW = BowType(rarity=Rarity.EPIC, damage=310, stats=Stats(strength=40, crit_chance=10, crit_damage=110))
TERMINATOR = BowType(rarity=Rarity.LEGENDARY, damage=310, stats=Stats(strength=50, attack_speed=40, crit_damage=250))
UNDEAD_BOW = BowType(rarity=Rarity.RARE, damage=80, stats=Stats())
SUPER_UNDEAD_BOW = BowType(rarity=Rarity.EPIC, damage=220, stats=Stats())
DEATH_BOW = BowType(rarity=Rarity.EPIC, damage=300, stats=Stats())
ITEM_SPIRIT_BOW = BowType(rarity=Rarity.LEGENDARY, damage=210, stats=Stats(strength=100))
LAST_BREATH = BowType(rarity=Rarity.LEGENDARY, damage=200, stats=Stats(strength=180, crit_damage=50))
BONE_BOOMERANG = BowType(rarity=Rarity.LEGENDARY, damage=270, stats=Stats(strength=130))
# TODO: Add all bow types
