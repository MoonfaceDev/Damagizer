from pydantic import BaseModel

from damagizer.entities.stats.rarity_stat import RarityStat
from damagizer.entities.stats.rarity_stats import RarityStats


class AccessoryType(BaseModel):
    stats: RarityStats = RarityStats()


VACCINE_TALISMAN = AccessoryType()

SPEED_TALISMAN = AccessoryType(stats=RarityStats(
    speed=RarityStat(common=1, uncommon=3, rare=5)
))

# TODO: Add all talismans types
