from pydantic import BaseModel

from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.rarity_stat import RarityStat
from damagizer.entities.stats.stats import Stats


class RarityStats(BaseModel):
    health: RarityStat = RarityStat()
    defense: RarityStat = RarityStat()
    strength: RarityStat = RarityStat()
    speed: RarityStat = RarityStat()
    crit_chance: RarityStat = RarityStat()
    crit_damage: RarityStat = RarityStat()
    attack_speed: RarityStat = RarityStat()
    intelligence: RarityStat = RarityStat()
    ferocity: RarityStat = RarityStat()
    ability_damage: RarityStat = RarityStat()

    def __getitem__(self, rarity: Rarity) -> Stats:
        self_dict = self.dict()
        result_dict = {stat_key: stat[rarity] for stat_key, stat in self_dict.items()}
        return Stats(**result_dict)
