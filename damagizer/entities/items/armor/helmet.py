from damagizer.entities.enchantments.armor.helmet import HelmetEnchantments
from damagizer.entities.items.armor.armor import Armor
from damagizer.entities.reforges.armor.helmet import HelmetReforge
from damagizer.entities.types.armor.helmet import HelmetType


class Helmet(Armor):
    type: HelmetType
    reforge: HelmetReforge
    enchantments: HelmetEnchantments = HelmetEnchantments()
