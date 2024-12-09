from abc import ABC, abstractmethod

class Interface(ABC):
    """Base interface for all user interfaces."""

    @abstractmethod
    def run(self) -> None:
        """Runs the interface"""

        pass

def run_interface(interface: Interface) -> None:
    interface.run()
