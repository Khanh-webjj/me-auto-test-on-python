from abc import ABC, abstractmethod

from components.base_component import BaseComponent

class Panel(BaseComponent, ABC):
    @abstractmethod
    def check_active(self, *args, **kwargs):
        """
        Return True if the requested control/state is active.
        """
        pass