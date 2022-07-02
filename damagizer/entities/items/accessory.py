from pydantic import BaseModel

from damagizer.entities.rarity import Rarity
from damagizer.entities.reforges.accessory import AccessoryReforge
from damagizer.entities.types.accessory import AccessoryType

RARITY_TO_MAGICAL_POWER = {
    Rarity.COMMON: 3,
    Rarity.UNCOMMON: 5,
    Rarity.RARE: 8,
    Rarity.EPIC: 12,
    Rarity.LEGENDARY: 16,
    Rarity.MYTHIC: 22,
    Rarity.SPECIAL: 3,
    Rarity.VERY_SPECIAL: 5
}


class Accessory(BaseModel):
    type: AccessoryType
    rarity: Rarity
    reforge: AccessoryReforge
    recombobulated: bool = False

    def get_magical_power(self) -> float:
        return RARITY_TO_MAGICAL_POWER[self.rarity]
