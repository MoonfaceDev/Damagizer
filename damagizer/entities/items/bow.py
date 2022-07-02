from pydantic import BaseModel

from damagizer.entities.attributes.sword import SwordAttribute
from damagizer.entities.enchantments.bow import BowEnchantment, BowUltimateEnchantment
from damagizer.entities.enchantments.sword import SwordEnchantment
from damagizer.entities.gemstones.gemstone import Gemstone
from damagizer.entities.items.weapon import Weapon
from damagizer.entities.reforges.bow import BowReforge
from damagizer.entities.reforges.sword import SwordReforge
from damagizer.entities.stats.rarity_stats import RarityStats
from damagizer.entities.types.bow import BowType
from damagizer.entities.types.sword import SwordType


class Bow(Weapon):
    type: BowType
    reforge: BowReforge = BowReforge(stats=RarityStats())
    enchantments: dict[BowEnchantment, int] = {}
    ultimate_enchantment: tuple[BowUltimateEnchantment | None, int] = (None, 0)
