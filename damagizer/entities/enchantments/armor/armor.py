from enum import Enum

from pydantic import BaseModel

from damagizer.entities.enchantments.enchantment_type import EnchantmentType


class ArmorEnchantments(BaseModel):
    protection: EnchantmentType(max_level=7) = 0
    growth: EnchantmentType(max_level=7) = 0
    # TODO: Add all general armor enchantments


class ArmorUltimateEnchantment(Enum):
    CHIMERA: EnchantmentType()
    # TODO: Add all general armor ultimate enchants
