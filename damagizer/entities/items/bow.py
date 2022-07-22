from damagizer.entities.enchantments.bow import BowEnchantments, BowUltimateEnchantment
from damagizer.entities.items.weapon import Weapon
from damagizer.entities.reforges.bow import BowReforge
from damagizer.entities.stats.rarity_stats import RarityStats
from damagizer.entities.types.bow import BowType


class Bow(Weapon):
    type: BowType
    reforge: BowReforge = BowReforge(stats=RarityStats())
    enchantments: BowEnchantments = BowEnchantments()
    ultimate_enchantment: tuple[BowUltimateEnchantment | None, int] = (None, 0)
