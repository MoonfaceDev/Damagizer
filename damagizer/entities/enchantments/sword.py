from enum import Enum

from damagizer.entities.enchantments.enchantment import Enchantment


class SwordEnchantment(Enum):
    BANE_OF_ARTHROPODS = Enchantment(max_level=7)
    CLEAVE = Enchantment(max_level=6)
    CRITICAL = Enchantment(max_level=7)
    CUBISM = Enchantment(max_level=6)
    DRAGON_HUNTER = Enchantment()
    ENDER_SLAYER = Enchantment(max_level=7)
    EXECUTE = Enchantment(max_level=6)
    EXPERIENCE = Enchantment(max_level=4)
    FIRE_ASPECT = Enchantment(max_level=3)
    FIRST_STRIKE = Enchantment()
    GIANT_KILLER = Enchantment(max_level=7)
    IMPALING = Enchantment(max_level=3)
    KNOCKBACK = Enchantment(max_level=2)
    LETHALITY = Enchantment(max_level=6)
    LIFE_STEAL = Enchantment()
    LOOTING = Enchantment()
    LUCK = Enchantment(max_level=7)
    MANA_STEAL = Enchantment(max_level=3)
    PROSECUTE = Enchantment(max_level=6)
    SCAVENGER = Enchantment()
    SHARPNESS = Enchantment(max_level=7)
    SMITE = Enchantment(max_level=7)
    SMOLDERING = Enchantment()
    SYPHON = Enchantment()
    THUNDERBOLT = Enchantment(max_level=6)
    THUNDERLORD = Enchantment(max_level=7)
    TITAN_KILLER = Enchantment(max_level=7)
    TRIPLE_STRIKE = Enchantment()
    VAMPIRISM = Enchantment(max_level=6)
    VENOMOUS = Enchantment(max_level=6)
    VICIOUS = Enchantment(min_level=3)


class SwordUltimateEnchantment(Enum):
    CHIMERA = Enchantment()
    COMBO = Enchantment()
    INFERNO = Enchantment()
    ONE_FOR_ALL = Enchantment(max_level=1)
    SOUL_EATER = Enchantment()
    SWARM = Enchantment()
    ULTIMATE_JERRY = Enchantment()
    ULTIMATE_WISE = Enchantment()
