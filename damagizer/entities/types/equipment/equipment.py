from pydantic import BaseModel

from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.stats import Stats


class EquipmentType(BaseModel):
    rarity: Rarity
    stats: Stats
