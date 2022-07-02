from damagizer.entities.enchantments.armor.armor import ArmorEnchantment
from damagizer.entities.enchantments.enchantment import Enchantment


class HelmetEnchantment(ArmorEnchantment):
    BANE_OF_ARTHROPODS = Enchantment(max_level=7)
    # TODO: Add all helmet-specific enchantments
