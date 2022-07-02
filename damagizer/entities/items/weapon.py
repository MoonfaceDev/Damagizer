from pydantic import BaseModel


class Weapon(BaseModel):
    hot_potato_books: int = 0
    stars: int = 0
    recombobulated: bool = False
    art_of_war: bool = False
