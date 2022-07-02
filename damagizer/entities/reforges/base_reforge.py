from pydantic import BaseModel

from damagizer.entities.stats.rarity_stats import RarityStats


class BaseReforge(BaseModel):
    stats: RarityStats
