from enum import Enum

from damagizer.entities.enchantments.enchantment import Enchantment


class ArmorEnchantment(Enum):
    BLAST_PROTECTION = Enchantment(max_level=7)
    # TODO: Add all general armor enchantments


class ArmorUltimateEnchantment(Enum):
    CHIMERA = Enchantment()
    # TODO: Add all general armor ultimate enchants
