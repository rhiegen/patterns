from __future__ import annotations
from abc import ABC, abstractmethod,abstractproperty
from typing import List
import re



class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy


    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def set_data(self, data:str) -> None:
        self.data = data

    def processa(self) -> List:
        return self._strategy.do_algorithm(self.data)



class Strategy(ABC):

    @abstractmethod
    def get_data(source: str)->str:
        pass

    @abstractmethod
    def do_algorithm(self, data: str)->List:
        pass

class Chain_pattern(ABC):

    def __init__(self):
        self.proximo =  None

    def get_proximo(self):
        return self.proximo

    def set_proximo(self,proximo:Chain_pattern = None):
        self.proximo = proximo

    @abstractmethod
    def get_parameters(self,data:str, retorno: List=[])->List:
        pass

    @abstractmethod
    def validate(self, gerada: List=[], existente: List= [], resultado: str = None)-> str:
        pass

class Unit_chain(Chain_pattern):

    def get_parameters(self, data, retorno: List=[])-> List:
        print('peguei unit')
        retorno.append('unit_lista')
        if self.get_proximo()  != None:
            return  self.get_proximo().get_parameters(data, retorno)
        return retorno
    
    def validate(self, gerada: List=[], existente: List= [], resultado: str = None)-> str:
        print('validei unit')
        if self.get_proximo()  != None:
            return  self.get_proximo().validate(gerada, existente, resultado)
        return resultado

class Clas_chain(Chain_pattern):


    def get_parameters(self, data, retorno: List=[])-> List:
        print('peguei clas')
        retorno.append('clas_lista')
        if self.get_proximo()  != None:
            return  self.get_proximo().get_parameters(data, retorno)
        return retorno

    def validate(self, gerada: List=[], existente: List= [], resultado: str = None)-> str:
        print('validei clas')
        if self.get_proximo()  != None:
            return  self.get_proximo().validate(gerada, existente, resultado)
        return resultado

class Clas_Strategy(Strategy):
    def __init__(self):
        self.proximo: Chain_pattern

    def get_data(self,source: str)->str:
        indice = source.find('DD')
        ovr = source[indice+3:]
        return ovr

    def set_data(self,data:str):
        self.data = data

    def do_algorithm(self,data:str) -> List:

        string = self.get_data(data)
        pattern_dataclas='(DATACLAS=)(\w+)'
        pattern_storclas='(STORCLAS=)(\w+)'
        dataclas = None
        storclas = None

        # match variable contains a Match object.
        match_dataclas = re.search(pattern_dataclas, string) 
        match_storclas = re.search(pattern_storclas, string) 

        if match_dataclas != None:
            dataclas = match_dataclas.group()
        if match_storclas != None:
            storclas = match_storclas.group()
        print(f'dataclas {dataclas} storclas {storclas}')
        return dataclas,storclas

class Unit_Strategy(Strategy):
    def get_data(self,source: str)->str:
        indice = source.find('DD')
        ovr = source[indice+3:]
        return ovr

    def set_data(self,data:str):
        self.data = data

    def do_algorithm(self, data: str) -> List:
        unit = None
        string = self.get_data(data)
        pattern_unit_simple = '(UNIT=SYSDA)'
        pattern_unit_number = '(UNIT=\(SYSDA\,)(\d+)(\))' 
        match_unit_simple = re.search(pattern_unit_simple, string) 
        match_unit_number = re.search(pattern_unit_number, string) 
        if match_unit_number != None:
            unit = match_unit_number.group()
        elif match_unit_simple != None:
            unit = match_unit_simple.group()
        
        print(f'unit {unit}')
        return unit



