from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.stats import Stats
from damagizer.entities.types.weapon import WeaponType


class BowType(WeaponType):
    pass


WITHER_BOW = BowType(rarity=Rarity.UNCOMMON, damage=30, stats=Stats())
JUJU_SHORTBOW = BowType(rarity=Rarity.EPIC, damage=310, stats=Stats(strength=40, crit_chance=10, crit_damage=110))
# TODO: Add all bow types
