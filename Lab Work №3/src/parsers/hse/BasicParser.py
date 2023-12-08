from parsers.protocols import ParserProtocol
from typing import override

class BasicParser(ParserProtocol):
    """There will be HSE Basic Parser"""

    @override
    def parse(self, payload) -> dict:
        pass

    def __init__(self):
        pass
