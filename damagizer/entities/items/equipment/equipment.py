from pydantic import BaseModel

from damagizer.entities.attributes.armor import ArmorAttribute
from damagizer.entities.reforges.equipment import EquipmentReforge
from damagizer.entities.types.equipment.equipment import EquipmentType


class Equipment(BaseModel):
    type: EquipmentType
    reforge: EquipmentReforge
    stars: int = 0
    recombobulated: bool = False
    attributes: tuple[ArmorAttribute, ArmorAttribute] | None = None
