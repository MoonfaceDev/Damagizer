from enum import Enum

from pydantic import BaseModel

from damagizer.entities.enchantments.enchantment_type import EnchantmentType


class BowEnchantments(BaseModel):
    bane_of_arthropods: EnchantmentType(max_level=7) = 0


class BowUltimateEnchantment(Enum):
    CHIMERA: EnchantmentType()
