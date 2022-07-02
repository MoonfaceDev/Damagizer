from pydantic import BaseModel

from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.stats import Stats


class WeaponType(BaseModel):
    rarity: Rarity
    damage: float
    stats: Stats
