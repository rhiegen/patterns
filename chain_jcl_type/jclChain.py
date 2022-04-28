from __future__ import annotations
from abc import ABC, abstractmethod


class JCLChain(ABC):

    def __init__(self):
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next_obj: JCLChain = None):
        self.next = next_obj

    @abstractmethod
    def get_parameters(self, data: str, __retorno=None) -> list:
        if __retorno is None:
            __retorno = []

    @abstractmethod
    def make_override(self, gerada=None, existente=None, resultado=None) -> str:
        pass





