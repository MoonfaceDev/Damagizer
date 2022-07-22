from damagizer.entities.gemstones.slot import GemstoneSlot
from damagizer.entities.rarity import Rarity
from damagizer.entities.stats.stats import Stats
from damagizer.entities.types.weapon import WeaponType


class SwordType(WeaponType):
    attributable: bool = False


WOOD_SWORD = SwordType(rarity=Rarity.COMMON, damage=20, stats=Stats())
GOLD_SWORD = SwordType(rarity=Rarity.COMMON, damage=20, stats=Stats())
STONE_SWORD = SwordType(rarity=Rarity.COMMON, damage=25, stats=Stats())
IRON_SWORD = SwordType(rarity=Rarity.COMMON, damage=30, stats=Stats())
DIAMOND_SWORD = SwordType(rarity=Rarity.UNCOMMON, damage=35, stats=Stats())
ROUGE_SWORD = SwordType(rarity=Rarity.COMMON, damage=20, stats=Stats())
FANCY_SWORD = SwordType(rarity=Rarity.COMMON, damage=20, stats=Stats())
CLEAVER = SwordType(rarity=Rarity.UNCOMMON, damage=40, stats=Stats(strength=10))
HUNTER_KNIFE = SwordType(rarity=Rarity.UNCOMMON, damage=50, stats=Stats(speed=40))
FLAMING_SWORD = SwordType(rarity=Rarity.UNCOMMON, damage=50, stats=Stats(strength=20))
SQUIRE_SWORD = SwordType(rarity=Rarity.UNCOMMON, damage=50, stats=Stats(strength=10))
MERCENARY_AXE = SwordType(rarity=Rarity.RARE, damage=70, stats=Stats(strength=20))
TRIBAL_SPEAR = SwordType(rarity=Rarity.RARE, damage=0, stats=Stats(strength=100))
ASPECT_OF_THE_JERRY = SwordType(rarity=Rarity.COMMON, damage=1, stats=Stats())
UNDEAD_SWORD = SwordType(rarity=Rarity.COMMON, damage=30, stats=Stats())
SPIDER_SWORD = SwordType(rarity=Rarity.COMMON, damage=30, stats=Stats())
END_SWORD = SwordType(rarity=Rarity.UNCOMMON, damage=35, stats=Stats())
SILVER_FANG = SwordType(rarity=Rarity.UNCOMMON, damage=100, stats=Stats())
PRISMARINE_BLADE = SwordType(rarity=Rarity.UNCOMMON, damage=50, stats=Stats(strength=25))
END_STONE_SWORD = SwordType(rarity=Rarity.EPIC, damage=120, stats=Stats(strength=80))
GOLEM_SWORD = SwordType(rarity=Rarity.RARE, damage=80, stats=Stats(strength=125, defense=25))
EMBER_ROD = SwordType(rarity=Rarity.EPIC, damage=80, stats=Stats(strength=35, intelligence=50))
ZOMBIE_SWORD = SwordType(rarity=Rarity.RARE, damage=100, stats=Stats(strength=50, intelligence=50),
                         gemstone_slots={GemstoneSlot.SAPPHIRE})
ORNATE_ZOMBIE_SWORD = SwordType(rarity=Rarity.EPIC, damage=110, stats=Stats(strength=60, intelligence=50),
                                gemstone_slots={GemstoneSlot.SAPPHIRE, GemstoneSlot.RUBY})
FLORID_ZOMBIE_SWORD = SwordType(rarity=Rarity.LEGENDARY, damage=150, stats=Stats(strength=80, intelligence=100),
                                gemstone_slots={GemstoneSlot.SAPPHIRE, GemstoneSlot.RUBY})
JERRY_STAFF = SwordType(rarity=Rarity.EPIC, damage=0, stats=Stats(strength=80, intelligence=200))
INK_WAND = SwordType(rarity=Rarity.EPIC, damage=130, stats=Stats(strength=90))
FROZEN_SCYTHE = SwordType(rarity=Rarity.RARE, damage=80, stats=Stats())
SOUL_WHIP = SwordType(rarity=Rarity.LEGENDARY, damage=145, stats=Stats(strength=175))
EMERALD_BLADE = SwordType(rarity=Rarity.EPIC, damage=130, stats=Stats())
RAIDER_AXE = SwordType(rarity=Rarity.RARE, damage=80, stats=Stats(strength=50))
TACTICIAN_SWORD = SwordType(rarity=Rarity.RARE, damage=50, stats=Stats(crit_chance=20))
ASPECT_OF_THE_END = SwordType(rarity=Rarity.RARE, damage=100, stats=Stats(strength=100),
                              gemstone_slots={GemstoneSlot.SAPPHIRE})
ASPECT_OF_THE_DRAGON = SwordType(rarity=Rarity.LEGENDARY, damage=225, stats=Stats(strength=100),
                                 gemstone_slots={GemstoneSlot.JASPER})
LEAPING_SWORD = SwordType(rarity=Rarity.EPIC, damage=150, stats=Stats(strength=100, crit_damage=25))
SILK_EDGE_SWORD = SwordType(rarity=Rarity.LEGENDARY, damage=175, stats=Stats(strength=125, crit_damage=25))
PIGMAN_SWORD = SwordType(rarity=Rarity.LEGENDARY, damage=200,
                         stats=Stats(strength=100, crit_damage=30, intelligence=300, crit_chance=5))
YETI_SWORD = SwordType(rarity=Rarity.LEGENDARY, damage=150, stats=Stats(strength=170, intelligence=50),
                       gemstone_slots={GemstoneSlot.SAPPHIRE, GemstoneSlot.JASPER})
MIDAS_SWORD = SwordType(rarity=Rarity.LEGENDARY, damage=150, stats=Stats(),
                        gemstone_slots={GemstoneSlot.COMBAT, GemstoneSlot.JASPER})
MIDAS_STAFF = SwordType(rarity=Rarity.LEGENDARY, damage=130, stats=Stats(strength=150, intelligence=50))
SWORD_OF_REVELATIONS = SwordType(rarity=Rarity.EPIC, damage=180, stats=Stats(strength=50))
DAEDALUS_AXE = SwordType(rarity=Rarity.LEGENDARY, damage=0, stats=Stats(),
                         gemstone_slots={GemstoneSlot.COMBAT, GemstoneSlot.COMBAT})
GHOUL_BUSTER = SwordType(rarity=Rarity.EPIC, damage=140, stats=Stats(strength=90, crit_damage=25))
SWORD_OF_BAD_HEALTH = SwordType(rarity=Rarity.UNCOMMON, damage=200, stats=Stats(strength=50, crit_damage=50))
RAGNAROCK_AXE = SwordType(rarity=Rarity.RARE, damage=250, stats=Stats(strength=70),
                          gemstone_slots={GemstoneSlot.COMBAT})
BLADE_OF_THE_VOLCANO = SwordType(rarity=Rarity.RARE, damage=220, stats=Stats(strength=70, crit_damage=20))
FIRE_FREEZE_STAFF = SwordType(rarity=Rarity.EPIC, damage=50, stats=Stats(strength=20),
                              gemstone_slots={GemstoneSlot.SAPPHIRE})
FIRE_FURY_STAFF = SwordType(rarity=Rarity.EPIC, damage=100, stats=Stats(intelligence=300),
                            gemstone_slots={GemstoneSlot.SAPPHIRE})
ENRAGER = SwordType(rarity=Rarity.EPIC, damage=270, stats=Stats(strength=150),
                    gemstone_slots={GemstoneSlot.SAPPHIRE})
RUNIC_STAFF = SwordType(rarity=Rarity.LEGENDARY, damage=20, stats=Stats(intelligence=250),
                        gemstone_slots={GemstoneSlot.SAPPHIRE, GemstoneSlot.SAPPHIRE})
REVENANT_SWORD = SwordType(rarity=Rarity.RARE, damage=90, stats=Stats(strength=50, intelligence=100))
REAPER_SWORD = SwordType(rarity=Rarity.EPIC, damage=120, stats=Stats(strength=100, intelligence=200),
                         gemstone_slots={GemstoneSlot.JASPER})
REAPER_SCYTHE = SwordType(rarity=Rarity.LEGENDARY, damage=333, stats=Stats(speed=10))
AXE_OF_THE_SHREDDED = SwordType(rarity=Rarity.LEGENDARY, damage=140, stats=Stats(strength=115),
                                gemstone_slots={GemstoneSlot.JASPER, GemstoneSlot.COMBAT})
RECLUSE_FANG = SwordType(rarity=Rarity.RARE, damage=120, stats=Stats(strength=30, crit_damage=20))
SCORPION_FOIL = SwordType(rarity=Rarity.EPIC, damage=100, stats=Stats(strength=100))
SHAMAN_SWORD = SwordType(rarity=Rarity.EPIC, damage=100, stats=Stats(strength=20, speed=5))
EDIBLE_MACE = SwordType(rarity=Rarity.RARE, damage=125, stats=Stats(strength=25))
POOCH_SWORD = SwordType(rarity=Rarity.LEGENDARY, damage=120, stats=Stats(strength=20, speed=5),
                        gemstone_slots={GemstoneSlot.JASPER})
VOIDWALKER_KATANA = SwordType(rarity=Rarity.UNCOMMON, damage=80, stats=Stats(strength=40, crit_damage=10))
VOIDEDGE_KATANA = SwordType(rarity=Rarity.RARE, damage=125, stats=Stats(strength=60, crit_damage=20, intelligence=50),
                            gemstone_slots={GemstoneSlot.JASPER, GemstoneSlot.SAPPHIRE})
VORPAL_KATANA = SwordType(rarity=Rarity.EPIC, damage=155, stats=Stats(strength=80, crit_damage=25, intelligence=200),
                          gemstone_slots={GemstoneSlot.JASPER, GemstoneSlot.SAPPHIRE})
ATOMSPLIT_KATANA = SwordType(rarity=Rarity.LEGENDARY, damage=245,
                             stats=Stats(strength=100, crit_damage=30, intelligence=300),
                             gemstone_slots={GemstoneSlot.JASPER, GemstoneSlot.SAPPHIRE, GemstoneSlot.SAPPHIRE})
SINSEEKER_SCYTHE = SwordType(rarity=Rarity.EPIC, damage=100, stats=Stats(strength=100))
ASPECT_OF_THE_VOID = SwordType(rarity=Rarity.EPIC, damage=120, stats=Stats(strength=100),
                               gemstone_slots={GemstoneSlot.SAPPHIRE})
FIREDUST_DAGGER = SwordType(rarity=Rarity.RARE, damage=90, stats=Stats(strength=45, crit_damage=15),
                            gemstone_slots={GemstoneSlot.COMBAT})
MAWDUST_DAGGER = SwordType(rarity=Rarity.RARE, damage=90, stats=Stats(strength=45, crit_damage=15),
                           gemstone_slots={GemstoneSlot.COMBAT})
BURSTFIRE_DAGGER = SwordType(rarity=Rarity.EPIC, damage=130, stats=Stats(strength=55, crit_damage=20, attack_speed=10),
                             gemstone_slots={GemstoneSlot.COMBAT, GemstoneSlot.OPAL})
BURSTMAW_DAGGER = SwordType(rarity=Rarity.EPIC, damage=130, stats=Stats(strength=55, crit_damage=20, attack_speed=10),
                            gemstone_slots={GemstoneSlot.COMBAT, GemstoneSlot.OPAL})
HEARTFIRE_DAGGER = SwordType(rarity=Rarity.LEGENDARY, damage=160,
                             stats=Stats(strength=75, crit_damage=25, crit_chance=10, attack_speed=20),
                             gemstone_slots={GemstoneSlot.COMBAT, GemstoneSlot.OPAL})
HEARTMAW_DAGGER = SwordType(rarity=Rarity.LEGENDARY, damage=160,
                            stats=Stats(strength=75, crit_damage=25, crit_chance=10, attack_speed=20),
                            gemstone_slots={GemstoneSlot.COMBAT, GemstoneSlot.OPAL})
SUPER_CLEAVER = SwordType(rarity=Rarity.RARE, damage=85, stats=Stats(strength=20))
HYPER_CLEAVER = SwordType(rarity=Rarity.EPIC, damage=145, stats=Stats(strength=50))
GIANT_CLEAVER = SwordType(rarity=Rarity.EPIC, damage=170, stats=Stats(strength=60))
FLOWER_OF_TRUTH = SwordType(rarity=Rarity.LEGENDARY, damage=160, stats=Stats(strength=300),
                            gemstone_slots={GemstoneSlot.JASPER})
FEL_SWORD = SwordType(rarity=Rarity.EPIC, damage=190, stats=Stats(strength=135))
WITHER_CLOAK = SwordType(rarity=Rarity.EPIC, damage=190, stats=Stats(strength=135, defense=250))
BONZO_STAFF = SwordType(rarity=Rarity.RARE, damage=160, stats=Stats(intelligence=250),
                        gemstone_slots={GemstoneSlot.SAPPHIRE})
STONE_BLADE = SwordType(rarity=Rarity.EPIC, damage=170, stats=Stats(), gemstone_slots={GemstoneSlot.DEFENSIVE})
SPIRIT_SWORD = SwordType(rarity=Rarity.EPIC, damage=210, stats=Stats(strength=50))
BAT_WAND = SwordType(rarity=Rarity.LEGENDARY, damage=180, stats=Stats(intelligence=300),
                     gemstone_slots={GemstoneSlot.SAPPHIRE})
SHADOW_FURY = SwordType(rarity=Rarity.LEGENDARY, damage=300, stats=Stats(strength=125, speed=30),
                        gemstone_slots={GemstoneSlot.JASPER})
LIVID_DAGGER = SwordType(rarity=Rarity.LEGENDARY, damage=210,
                         stats=Stats(strength=60, crit_chance=100, crit_damage=50, attack_speed=100),
                         gemstone_slots={GemstoneSlot.JASPER})
GIANTS_SWORD = SwordType(rarity=Rarity.LEGENDARY, damage=500, stats=Stats(),
                         gemstone_slots={GemstoneSlot.JASPER, GemstoneSlot.JASPER})
NECROMANCER_SWORD = SwordType(rarity=Rarity.LEGENDARY, damage=250, stats=Stats(strength=125, defense=125))
NECRON_BLADE = SwordType(rarity=Rarity.LEGENDARY, damage=260, stats=Stats(strength=110, intelligence=50, ferocity=30))
VALKYRIE = SwordType(rarity=Rarity.LEGENDARY, damage=270, stats=Stats(strength=145, intelligence=60, ferocity=60),
                     gemstone_slots={GemstoneSlot.JASPER, GemstoneSlot.COMBAT})
HYPERION = SwordType(rarity=Rarity.LEGENDARY, damage=260, stats=Stats(strength=150, intelligence=350, ferocity=30),
                     gemstone_slots={GemstoneSlot.SAPPHIRE, GemstoneSlot.COMBAT})
SCYLLA = SwordType(rarity=Rarity.LEGENDARY, damage=270,
                   stats=Stats(strength=150, intelligence=50, ferocity=30, crit_chance=12, crit_damage=35),
                   gemstone_slots={GemstoneSlot.COMBAT, GemstoneSlot.COMBAT})
ASTRAEA = SwordType(rarity=Rarity.LEGENDARY, damage=270,
                    stats=Stats(strength=150, intelligence=50, ferocity=30, true_defense=20, defense=250),
                    gemstone_slots={GemstoneSlot.DEFENSIVE, GemstoneSlot.COMBAT})
DARK_CLAYMORE = SwordType(rarity=Rarity.LEGENDARY, damage=500, stats=Stats(strength=100))
# TODO: Add all sword types
