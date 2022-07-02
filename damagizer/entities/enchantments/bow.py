from enum import Enum

from damagizer.entities.enchantments.enchantment import Enchantment


class BowEnchantment(Enum):
    BANE_OF_ARTHROPODS = Enchantment(max_level=7)


class BowUltimateEnchantment(Enum):
    CHIMERA = Enchantment()
