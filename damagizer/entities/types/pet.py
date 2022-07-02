from pydantic import BaseModel

from damagizer.entities.stats.rarity_stat import RarityStat
from damagizer.entities.stats.rarity_stats import RarityStats


class PetType(BaseModel):
    stats: RarityStats = RarityStats()


BLUE_WHALE = PetType(stats=RarityStats(
    health=RarityStat(legendary=200)
))

BABY_YETI = PetType(stats=RarityStats(
    strength=RarityStat(legendary=40),
    intelligence=RarityStat(legendary=75)
))

SHEEP = PetType(stats=RarityStats(
    intelligence=RarityStat(legendary=100),
    ability_damage=RarityStat(legendary=20)
))

GRIFFIN = PetType(stats=RarityStats(
    strength=RarityStat(legendary=25),
    crit_chance=RarityStat(legendary=10),
    crit_damage=RarityStat(legendary=50),
    intelligence=RarityStat(legendary=10)
))

MITHRIL_GOLEM = PetType()

BLACK_CAT = PetType(stats=RarityStats(
    speed=RarityStat(legendary=25),
    intelligence=RarityStat(legendary=100)
))

# TODO: Add all pet types
