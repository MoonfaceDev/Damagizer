from damagizer.entities.attributes.sword import SwordAttribute
from damagizer.entities.enchantments.sword import SwordEnchantments, SwordUltimateEnchantment
from damagizer.entities.items.weapon import Weapon
from damagizer.entities.reforges.sword import SwordReforge
from damagizer.entities.stats.rarity_stats import RarityStats
from damagizer.entities.types.sword import SwordType


class Sword(Weapon):
    type: SwordType
    reforge: SwordReforge = SwordReforge(stats=RarityStats())
    enchantments: SwordEnchantments = SwordEnchantments()
    ultimate_enchantment: tuple[SwordUltimateEnchantment | None, int] = (None, 0)
    attributes: tuple[SwordAttribute, SwordAttribute] | None = None
