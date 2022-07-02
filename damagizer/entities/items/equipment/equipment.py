from pydantic import BaseModel

from damagizer.entities.attributes.armor import ArmorAttribute
from damagizer.entities.reforges.equipment import EquipmentReforge


class Equipment(BaseModel):
    reforge: EquipmentReforge
    stars: int = 0
    recombobulated: bool = False
    attributes: tuple[ArmorAttribute, ArmorAttribute] | None = None
