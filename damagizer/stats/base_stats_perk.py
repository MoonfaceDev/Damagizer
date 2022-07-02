from abc import ABC, abstractmethod

from damagizer.entities.stats.stats import Stats


class BaseStatsPerk(ABC):
    @abstractmethod
    def evaluate(self) -> Stats:
        raise NotImplementedError()
