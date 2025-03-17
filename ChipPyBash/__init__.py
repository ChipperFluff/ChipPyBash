from .parse_file import FileParser as _FileParser
from .jump import Goto as _Goto

_file_parser = _FileParser()
goto = _Goto(_file_parser)