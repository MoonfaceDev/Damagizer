from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.stats import Stats
from damagizer.entities.types.pet import PetType
from damagizer.entities.types.pet_item import PetItemType


class Pet:
    type: PetType
    rarity: Rarity
    level: int
    item: PetItemType

    def get_stats(self) -> Stats:
        return self.type.stats[self.rarity] * (self.level / 100) + self.item.stats
