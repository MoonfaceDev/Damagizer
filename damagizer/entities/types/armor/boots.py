from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.stats import Stats
from damagizer.entities.types.armor.armor import ArmorType


class BootsType(ArmorType):
    pass


RANCHER_BOOTS = BootsType(rarity=Rarity.EPIC, stats=Stats(health=100, defense=70, speed=50))
