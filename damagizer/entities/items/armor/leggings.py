from damagizer.entities.enchantments.armor.leggings import LeggingsEnchantment
from damagizer.entities.items.armor.armor import Armor
from damagizer.entities.reforges.armor.leggings import LeggingsReforge
from damagizer.entities.types.armor.leggings import LeggingsType


class Leggings(Armor):
    type: LeggingsType
    reforge: LeggingsReforge
    enchantments: dict[LeggingsEnchantment, int] = {}
