from enum import Enum

from pydantic import BaseModel

from damagizer.entities.enchantments.enchantment_type import EnchantmentType


class SwordEnchantments(BaseModel):
    bane_of_arthropods: EnchantmentType(max_level=7) = 0
    cleave: EnchantmentType(max_level=6) = 0
    critical: EnchantmentType(max_level=7) = 0
    cubism: EnchantmentType(max_level=6) = 0
    dragon_hunter: EnchantmentType() = 0
    ender_slayer: EnchantmentType(max_level=7) = 0
    execute: EnchantmentType(max_level=6) = 0
    experience: EnchantmentType(max_level=4) = 0
    fire_aspect: EnchantmentType(max_level=3) = 0
    first_strike: EnchantmentType() = 0
    giant_killer: EnchantmentType(max_level=7) = 0
    impaling: EnchantmentType(max_level=3) = 0
    knockback: EnchantmentType(max_level=2) = 0
    lethality: EnchantmentType(max_level=6) = 0
    life_steal: EnchantmentType() = 0
    looting: EnchantmentType() = 0
    luck: EnchantmentType(max_level=7) = 0
    mana_steal: EnchantmentType(max_level=3) = 0
    prosecute: EnchantmentType(max_level=6) = 0
    scavenger: EnchantmentType() = 0
    sharpness: EnchantmentType(max_level=7) = 0
    smite: EnchantmentType(max_level=7) = 0
    smoldering: EnchantmentType() = 0
    syphon: EnchantmentType() = 0
    thunderbolt: EnchantmentType(max_level=6) = 0
    thunderlord: EnchantmentType(max_level=7) = 0
    titan_killer: EnchantmentType(max_level=7) = 0
    triple_strike: EnchantmentType() = 0
    vampirism: EnchantmentType(max_level=6) = 0
    venomous: EnchantmentType(max_level=6) = 0
    vicious: EnchantmentType(min_level=3) = 0


class SwordUltimateEnchantment(Enum):
    CHIMERA: EnchantmentType() = 0
    COMBO: EnchantmentType() = 0
    INFERNO: EnchantmentType() = 0
    ONE_FOR_ALL: EnchantmentType(max_level=1) = 0
    SOUL_EATER: EnchantmentType() = 0
    SWARM: EnchantmentType() = 0
    ULTIMATE_JERRY: EnchantmentType() = 0
    ULTIMATE_WISE: EnchantmentType() = 0
