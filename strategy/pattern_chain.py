from __future__ import annotations
from abc import ABC, abstractmethod,abstractproperty
from typing import List
import re


class Chain_pattern(ABC):

    def __init__(self):
        self.proximo =  None

    def get_proximo(self):
        return self.proximo

    def set_proximo(self,proximo:Chain_pattern = None):
        self.proximo = proximo

    @abstractmethod
    def get_parameters(self,data:str,__retorno: List=[])->List:
        pass

    @abstractmethod
    def validate(self, gerada: List=[], existente: List= [], resultado: str = None)-> str:
        pass

class Unit_chain(Chain_pattern):
    def __del__(self):
        print('destruido unit')
        retorno = None

    def get_parameters(self, data, retorno: List=[])-> List:
        unit = None
        print('peguei unit')
        indice = data.find('DD')
        data = data[indice+3:]
        
        pattern_unit_simple = '(UNIT=SYSDA)'
        pattern_unit_number = '(UNIT=\(SYSDA\,)(\d+)(\))' 
        match_unit_simple = re.search(pattern_unit_simple, data) 
        match_unit_number = re.search(pattern_unit_number, data) 
        if match_unit_number != None:
            unit = match_unit_number.group()
        elif match_unit_simple != None:
            unit = match_unit_simple.group()
        
        retorno.append(unit)

        if self.get_proximo()  != None:
            return  self.get_proximo().get_parameters(data, retorno)
        return retorno
    
    def validate(self, gerada: List=[], existente: List= [], resultado: str = None)-> str:
        print('validei unit')
        if self.get_proximo()  != None:
            return  self.get_proximo().validate(gerada, existente, resultado)
        return resultado

class Clas_chain(Chain_pattern):

    def __del__(self):
        print('destruido clas')
        retorno = None

    def get_parameters(self, data, retorno: List=[])-> List:
        indice = data.find('DD')
        data = data[indice+3:]
        pattern_dataclas='(DATACLAS=)(\w+)'
        pattern_storclas='(STORCLAS=)(\w+)'
        dataclas = None
        storclas = None

        # match variable contains a Match object.
        match_dataclas = re.search(pattern_dataclas, data) 
        match_storclas = re.search(pattern_storclas, data) 

        if match_dataclas != None:
            dataclas = match_dataclas.group()
        if match_storclas != None:
            storclas = match_storclas.group()
            
        clas =  dataclas,storclas
        retorno.append(clas)

        if self.get_proximo()  != None:
            return  self.get_proximo().get_parameters(data, retorno)
        return retorno

    def validate(self, gerada: List=[], existente: List= [], resultado: str = None)-> str:
        print('validei clas')
        if self.get_proximo()  != None:
            return  self.get_proximo().validate(gerada, existente, resultado)
        return resultado

