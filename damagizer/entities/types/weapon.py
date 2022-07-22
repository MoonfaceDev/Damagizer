from pydantic import BaseModel

from damagizer.entities.gemstones.slot import GemstoneSlot
from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.stats import Stats


class WeaponType(BaseModel):
    rarity: Rarity
    damage: float
    stats: Stats
    gemstone_slots: set[GemstoneSlot] = {}
