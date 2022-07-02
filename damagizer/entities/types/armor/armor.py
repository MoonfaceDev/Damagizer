from pydantic import BaseModel

from damagizer.entities.gemstones.slot import GemstoneSlot
from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.stats import Stats


class ArmorType(BaseModel):
    rarity: Rarity
    stats: Stats
    gemstone_slots: set[GemstoneSlot] = {}
