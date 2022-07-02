from enum import Enum

from damagizer.entities.gemstones.type import GemstoneType


class GemstoneSlot(Enum):
    JADE = {GemstoneType.JADE}
    AMBER = {GemstoneType.AMBER}
    TOPAZ = {GemstoneType.TOPAZ}
    SAPPHIRE = {GemstoneType.SAPPHIRE}
    AMETHYST = {GemstoneType.AMETHYST}
    JASPER = {GemstoneType.JASPER}
    OPAL = {GemstoneType.OPAL}
    RUBY = {GemstoneType.RUBY}
    COMBAT = {GemstoneType.SAPPHIRE, GemstoneType.AMETHYST, GemstoneType.RUBY, GemstoneType.JASPER}
    OFFENSIVE = {GemstoneType.JASPER, GemstoneType.SAPPHIRE},
    DEFENSIVE = {GemstoneType.AMETHYST, GemstoneType.RUBY},
    MINING = {GemstoneType.JADE, GemstoneType.AMBER, GemstoneType.TOPAZ},
    UNIVERSAL = {GemstoneType.JADE, GemstoneType.AMBER, GemstoneType.TOPAZ, GemstoneType.SAPPHIRE,
                 GemstoneType.AMETHYST, GemstoneType.JASPER, GemstoneType.OPAL, GemstoneType.RUBY}
