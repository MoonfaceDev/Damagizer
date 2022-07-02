from pydantic import BaseModel, Field

from damagizer.entities.rarity import Rarity


class RarityStat(BaseModel):
    common: float = Field(0)
    uncommon: float = Field(0)
    rare: float = Field(0)
    epic: float = Field(0)
    legendary: float = Field(0)
    mythic: float = Field(0)
    special: float = Field(0)
    very_special: float = Field(0)
    _rarity_to_value: dict[Rarity, float] = {}

    def __setitem__(self, key: Rarity, value: float):
        self._rarity_to_value[key] = value

    def __getitem__(self, rarity: Rarity) -> float:
        return self._rarity_to_value[rarity]
