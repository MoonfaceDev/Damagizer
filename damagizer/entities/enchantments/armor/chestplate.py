from damagizer.entities.enchantments.armor.armor import ArmorEnchantments
from damagizer.entities.enchantments.enchantment_type import EnchantmentType


class ChestplateEnchantments(ArmorEnchantments):
    bane_of_arthropods: EnchantmentType(max_level=7) = 0
    # TODO: Add all chestplate-specific enchantments
