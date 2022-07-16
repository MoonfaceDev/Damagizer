from damagizer.entities.enchantments.armor.armor import ArmorEnchantments
from damagizer.entities.enchantments.enchantment_type import EnchantmentType


class LeggingsEnchantments(ArmorEnchantments):
    bane_of_arthropods: EnchantmentType(max_level=7) = 0
    # TODO: Add all leggings-specific enchantments
