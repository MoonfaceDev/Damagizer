from pydantic import BaseModel

from damagizer.entities.items.accessory import Accessory


class AccessoryBag(BaseModel):
    accessories: list[Accessory]
