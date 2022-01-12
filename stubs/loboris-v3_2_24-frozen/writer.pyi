from typing import Any

class Writer:
    text_row: int
    text_col: int
    row_clip: bool
    col_clip: bool
    @classmethod
    def set_textpos(cls, row, col) -> None: ...
    @classmethod
    def set_clip(cls, row_clip, col_clip) -> None: ...
    device: Any
    font: Any
    map: Any
    screenwidth: Any
    screenheight: Any
    def __init__(self, device, font, verbose: bool = ...) -> None: ...
    def _newline(self) -> None: ...
    def printstring(self, string) -> None: ...
    def _printchar(self, char) -> None: ...
    def _printchar_bitwise(self, char) -> None: ...