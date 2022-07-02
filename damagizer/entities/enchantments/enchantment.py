from pydantic import BaseModel


class Enchantment(BaseModel):
    min_level: int = 1
    max_level: int = 5
