from pydantic import BaseModel

from damagizer.entities.items.equipment.belt import Belt
from damagizer.entities.items.equipment.cloak import Cloak
from damagizer.entities.items.equipment.gloves import Gloves
from damagizer.entities.items.equipment.necklace import Necklace


class EquipmentSet(BaseModel):
    belt: Belt
    cloak: Cloak
    necklace: Necklace
    gloves: Gloves
