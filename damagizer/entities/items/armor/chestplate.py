from damagizer.entities.enchantments.armor.chestplate import ChestplateEnchantments
from damagizer.entities.items.armor.armor import Armor
from damagizer.entities.reforges.armor.chestplate import ChestplateReforge
from damagizer.entities.types.armor.chestplate import ChestplateType


class Chestplate(Armor):
    type: ChestplateType
    reforge: ChestplateReforge
    enchantments: ChestplateEnchantments = ChestplateEnchantments()
