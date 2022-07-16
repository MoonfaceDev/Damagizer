from abc import ABC, abstractmethod

from damagizer.profile.profile import Profile


class BaseStatsMultiplier(ABC):
    @abstractmethod
    def evaluate(self, profile: Profile) -> float:
        raise NotImplementedError()
