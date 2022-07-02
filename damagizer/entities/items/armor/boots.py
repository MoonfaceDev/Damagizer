from damagizer.entities.enchantments.armor.boots import BootsEnchantment
from damagizer.entities.items.armor.armor import Armor
from damagizer.entities.reforges.armor.boots import BootsReforge
from damagizer.entities.types.armor.boots import BootsType


class Boots(Armor):
    type: BootsType
    reforge: BootsReforge
    enchantments: dict[BootsEnchantment, int] = {}
