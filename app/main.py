from .user_interfaces.base import run_interface
from .user_interfaces.cli import MainMenu

def main():
    run_interface(interface=MainMenu())

if __name__ == '__main__':
    main()