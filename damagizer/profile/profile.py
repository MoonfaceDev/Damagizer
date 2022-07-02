from pydantic import BaseModel

from damagizer.entities.dungeon_classes import DungeonClass
from damagizer.entities.items.accessory_bag import AccessoryBag
from damagizer.entities.items.armor.armor_set import ArmorSet
from damagizer.entities.items.equipment.equipment_set import EquipmentSet
from damagizer.entities.items.pet import Pet
from damagizer.entities.items.sword import Sword
from damagizer.entities.skill import Skill
from damagizer.entities.slayer import Slayer
from damagizer.entities.stats.stats import Stats
from damagizer.entities.undead_essence import UndeadEssence
from damagizer.entities.wither_essence import WitherEssence


class Environment(BaseModel):
    dungeon: bool = False
    master_mode: bool = False
    dungeon_class_unique: bool = False
    enemy_hp: float = 0
    enemy_current_hp: float = 0
    first_hit: bool = False
    undead: bool = False
    mythological: bool = False
    mythological_kills: int = 0


class Profile(BaseModel):
    god_potion: bool
    dungeon_potion: bool
    cakes: int
    fairy_souls: int
    melody_level: int
    hoes_speed: float
    dungeon_class: DungeonClass
    dungeon_class_level: int
    defuse_kit: bool
    bestiary: int
    blood_god_crest_bonus: int
    skill_levels: dict[Skill, int]
    slayer_levels: dict[Slayer, int]
    wither_essence: dict[WitherEssence, int]
    undead_essence: dict[UndeadEssence, int]
    pet: Pet
    sword: Sword
    armor: ArmorSet
    equipment: EquipmentSet
    accessories: AccessoryBag
    environment: Environment

    def get_catacombs_level_bonus(self):
        return sum([
            ((self.skill_levels[Skill.CATACOMBS] - k) // 5 + 1) * (8 + (self.skill_levels[Skill.CATACOMBS] - k) // 5)
            for k
            in range(1, 6)]) / 200

    def get_dungeon_stats(self, normal_stats: Stats, dungeon_item: bool, stars: int):
        if self.environment.dungeon and dungeon_item:
            return normal_stats * (1 + self.get_catacombs_level_bonus() + stars / 10)
        return normal_stats

    def get_dungeon_sword_damage(self, sword_damage: Stats, dungeon_item: bool, stars: int):
        if self.environment.dungeon and dungeon_item:
            return sword_damage * (1 + self.get_catacombs_level_bonus() + stars / 10)
        return sword_damage
