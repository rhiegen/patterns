from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class OverrideChain(ABC):

    def __init__(self):
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next_obj: OverrideChain = None):
        self.next = next_obj

    @abstractmethod
    def get_parameters(self, data: str, __retorno = []) -> List:
        if __retorno is None:
            __retorno = []

    @abstractmethod
    def make_override(self, gerada: List = [], existente: List = [], resultado: str = None) -> str:
        pass





