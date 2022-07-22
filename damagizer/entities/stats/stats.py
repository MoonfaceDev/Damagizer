from typing import Union

from pydantic import BaseModel


class Stats(BaseModel):
    health: float = 0
    defense: float = 0
    true_defense: float = 0
    strength: float = 0
    speed: float = 0
    crit_chance: float = 0
    crit_damage: float = 0
    attack_speed: float = 0
    intelligence: float = 0
    ferocity: float = 0
    ability_damage: float = 0

    def __str__(self) -> str:
        return '\n'.join([f"{stat_name}: {round(stat_value)}" for stat_name, stat_value in self.dict().items()])

    def __add__(self, other: 'Stats') -> 'Stats':
        if not isinstance(other, Stats):
            raise TypeError("Second operand must be of type 'Single Stats'")
        self_dict = self.dict()
        other_dict = other.dict()
        result_dict = {stat_name: stat_value + other_dict[stat_name] for stat_name, stat_value in self_dict.items()}
        return Stats(**result_dict)

    def __sub__(self, other: 'Stats') -> 'Stats':
        if not isinstance(other, Stats):
            raise TypeError("Second operand must be of type 'Single Stats'")
        self_dict = self.dict()
        other_dict = other.dict()
        result_dict = {stat_name: stat_value - other_dict[stat_name] for stat_name, stat_value in self_dict.items()}
        return Stats(**result_dict)

    def __mul__(self, factor: Union[int, float]) -> 'Stats':
        if not isinstance(factor, (int, float)):
            raise TypeError("Second operand must be a number")
        self_dict = self.dict()
        result_dict = {stat_name: stat_value * factor for stat_name, stat_value in self_dict.items()}
        return Stats(**result_dict)

    def __rmul__(self, factor: Union[int, float]) -> 'Stats':
        return self * factor

    def __truediv__(self, factor: Union[int, float]) -> 'Stats':
        if not isinstance(factor, (int, float)):
            raise TypeError("Second operand must be a number")
        self_dict = self.dict()
        result_dict = {stat_name: stat_value / factor for stat_name, stat_value in self_dict.items()}
        return Stats(**result_dict)

    def __rtruediv__(self, factor: Union[int, float]) -> 'Stats':
        return self / factor

    def round(self) -> 'Stats':
        self_dict = self.dict()
        result_dict = {stat_name: round(stat_value) for stat_name, stat_value in self_dict.items()}
        return Stats(**result_dict)
