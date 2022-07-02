from pydantic import BaseModel

from damagizer.entities.gemstones.tier import GemstoneTier
from damagizer.entities.gemstones.type import GemstoneType


class Gemstone(BaseModel):
    type: GemstoneType
    tier: GemstoneTier
