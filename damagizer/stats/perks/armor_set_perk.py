from damagizer.entities.items.armor.armor import Armor
from damagizer.entities.stats.stats import Stats
from damagizer.profile.profile import Profile
from damagizer.stats.base_stats_perk import BaseStatsPerk


class ArmorSetPerk(BaseStatsPerk):
    @staticmethod
    def evaluate_piece(piece: Armor) -> Stats:
        type_stats = piece.type.stats
        reforge_stats = piece.reforge.stats[piece.type.rarity + piece.recombobulated]
        protection_stats = Stats(defense=3 * piece.enchantments.protection)
        growth_stats = Stats(health=10 * piece.enchantments.growth)
        # TODO: Add other general armor enchantments...
        hot_potato_books_stats = Stats(health=2 * piece.hot_potato_books, defense=piece.hot_potato_books)
        attributes_stats = Stats() if piece.attributes is None else Stats()
        # TODO: Add attributes actual perk
        gemstone_stats = Stats()
        # TODO: Add gemstones actual perk
        ultimate_enchantment_stats = Stats()
        # TODO: Add ultimate enchant actual perk
        return sum([type_stats, reforge_stats, protection_stats, growth_stats, hot_potato_books_stats, attributes_stats,
                    gemstone_stats, ultimate_enchantment_stats])

    def evaluate(self, profile: Profile) -> Stats:
        armor_pieces = profile.armor.get_pieces()
        return sum(
            [profile.get_dungeon_stats(ArmorSetPerk.evaluate_piece(piece), piece.stars) for piece in armor_pieces]
        )
