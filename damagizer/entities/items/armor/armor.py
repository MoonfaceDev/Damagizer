from pydantic import BaseModel

from damagizer.entities.attributes.armor import ArmorAttribute
from damagizer.entities.enchantments.armor.armor import ArmorUltimateEnchantment
from damagizer.entities.gemstones.gemstone import Gemstone


class Armor(BaseModel):
    hot_potato_books: int = 0
    stars: int = 0
    recombobulated: bool = False
    attributes: tuple[ArmorAttribute, ArmorAttribute] | None = None
    gemstones: set[Gemstone] = {}
    ultimate_enchantment: tuple[ArmorUltimateEnchantment | None, int] = (None, 0)
