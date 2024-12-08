from enum import Enum

class Color(str, Enum):
    RED = '31'
    GREEN = '32'
    YELLOW = '34'
    VIOLET = '35'
    BLUE = '36'
    GREY = '30'

class ColorPrint:

    def _color_text(self, text: str, color: Color) -> str:
        return f'\033[{color}m{text}\033[0m'

    def _color_print(self, text: str, color: Color, end: str = '\n') -> None:
        print(self._color_text(text, color), end=end)

    def red(self, text: str, end: str = '\n') -> str:
        return self._color_print(text=text, color=Color.RED.value, end=end)

    def green(self, text: str, end: str = '\n') -> str:
        return self._color_print(text=text, color=Color.GREEN.value, end=end)

    def yellow(self, text: str, end: str = '\n') -> str:
        return self._color_print(text=text, color=Color.YELLOW.value, end=end)
    
    def violet(self, text: str, end: str = '\n') -> str:
        return self._color_print(text=text, color=Color.VIOLET.value, end=end)

    def blue(self, text: str, end: str = '\n') -> str:
        return self._color_print(text=text, color=Color.BLUE.value, end=end)
    
    def grey(self, text: str, end: str = '\n') -> str:
        return self._color_print(text=text, color=Color.GREY.value, end=end)

cprint = ColorPrint()
