from abc import ABC, abstractmethod

class Interface(ABC):
    """Base interface for all user interfaces."""

    @abstractmethod
    def on_enter(self) -> None:
        """The display is called when entering the interface."""
        pass

    @abstractmethod
    def handle_input(self, input) -> None:
        """Handles the user's input."""
        pass

def run_interface(interface: Interface) -> None:
    interface.run()
