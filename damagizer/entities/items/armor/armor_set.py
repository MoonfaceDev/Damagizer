from pydantic import BaseModel

from damagizer.entities.items.armor.boots import Boots
from damagizer.entities.items.armor.chestplate import Chestplate
from damagizer.entities.items.armor.helmet import Helmet
from damagizer.entities.items.armor.leggings import Leggings


class ArmorSet(BaseModel):
    helmet: Helmet
    chestplate: Chestplate
    leggings: Leggings
    boots: Boots
