from abc import ABC, abstractmethod

from damagizer.entities.stats.stats import Stats


class BaseStatsMultiplier(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        raise NotImplementedError()
