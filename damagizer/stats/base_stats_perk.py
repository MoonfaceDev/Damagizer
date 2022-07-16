from abc import ABC, abstractmethod

from damagizer.entities.stats.stats import Stats
from damagizer.profile.profile import Profile


class BaseStatsPerk(ABC):
    @abstractmethod
    def evaluate(self, profile: Profile) -> Stats:
        raise NotImplementedError()
