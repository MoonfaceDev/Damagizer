from damagizer.entities.reforges.base_reforge import BaseReforge
from damagizer.entities.stats.rarity_stat import RarityStat
from damagizer.entities.stats.rarity_stats import RarityStats


class BowReforge(BaseReforge):
    pass


HASTY = BowReforge(stats=RarityStats(
    strength=RarityStat(common=3, uncommon=5, rare=7, epic=10, legendary=15, mythic=20),
    crit_chance=RarityStat(common=20, uncommon=25, rare=30, epic=40, legendary=50, mythic=60),
))
