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
    def montar_override(self, gerada: List=[], existente: List= [], resultado: str = None)-> str:
        pass

class Unit_chain(Chain_pattern):
    def __del__(self):
        print('destruido unit')
        retorno = None

    def get_parameters(self, data, retorno: List=[])-> List:
        unit = None
        print('processando unit...')
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
        return [retorno]
    
    def montar_override(self, data: str, existente: List= [], resultado: str = None)-> str:
        print('Gerando override com unit...')
        ovr = ''
        ret_unit_gerada = [x for x in data if x != None and  'UNIT' in x]

        if len(ret_unit_gerada) > 0:
            ovr+=''.join(ret_unit_gerada)

        resultado+= ovr
        # print(f'override unit {resultado}')
        if self.get_proximo()  != None:
            return  self.get_proximo().montar_override(data, existente, resultado)
        return resultado

class Clas_chain(Chain_pattern):

    def __del__(self):
        print('destruido clas')
        retorno = None

    def get_parameters(self, data, retorno: List=[])-> List:
        print('processando _clas...')
        indice = data.find('DD')
        data = data[indice+3:]
        pattern_dataclas='(DATACLAS=)(\w+)'
        pattern_storclas='(STORCLAS=)(\w+)'
        pattern_avgrec='(AVGREC=)(\w+)'

        dataclas = None
        storclas = None
        avgrec = None

        # match variable contains a Match object.
        match_dataclas = re.search(pattern_dataclas, data) 
        match_storclas = re.search(pattern_storclas, data) 
        match_avgrec = re.search(pattern_avgrec, data) 

        if match_dataclas != None:
            dataclas = match_dataclas.group()
            retorno.append(dataclas)
        if match_storclas != None:
            storclas = match_storclas.group()
            retorno.append(storclas)
        if match_avgrec != None:
            avgrec = match_avgrec.group()
            retorno.append(avgrec)
        if self.get_proximo()  != None:
            return  self.get_proximo().get_parameters(data, retorno)
        return retorno

    def montar_override(self, data: str, existente: List=[], resultado: str = None)-> str:
        print('gerando override _clas...')
        ovr = ''
        ret_dataclas_gerada = [x for x in data if x != None and 'DATACLAS' in x]
        ret_dataclas_existente = [x for x in existente if x != None and 'DATACLAS' in x]
        ret_storclas_gerada = [x for x in data if x != None and 'STORCLAS' in x]
        ret_storclas_existente = [x for x in existente if x != None and 'STORCLAS' in x]
        ret_avgrec_existente = [x for x in existente if x != None and 'AVGREC' in x]
        ret_avgrec_gerada = [x for x in data if x != None and 'AVGREC' in x]

        # if len(ret_dataclas_gerada) > 0:
        #     if ovr != '' or resultado != '':
        #         ovr+=','
        #     ovr+=''.join(ret_dataclas_gerada)
        # elif len(ret_dataclas_existente) > 0:
        #     if ovr != '' or resultado != '':
        #         ovr+=','
        #     ovr+=''.join(ret_dataclas_existente)

        if len(ret_dataclas_gerada) > 0:
            if ovr != '' or resultado != '':
                ovr+=','
            ovr+='DATACLAS=XDEFCOMP' \
                if ''.join(ret_dataclas_existente) == 'DATACLAS=XDEFCOMP' \
                    else ''.join(ret_dataclas_gerada)
        elif len(ret_dataclas_existente) > 0:
            if ovr != '' or resultado != '':
                ovr+=','
            ovr+='DATACLAS=XDEFCOMP' \
                if ''.join(ret_dataclas_gerada) == 'DATACLAS=XDEFCOMP' \
                    else ''.join(ret_dataclas_existente)

            
        if len(ret_storclas_gerada) > 0:
            if ovr != '' or resultado != '':
                ovr+=','
            ovr+=''.join(ret_storclas_gerada)
        elif len(ret_storclas_existente) > 0:
            if ovr != '' or resultado != '':
                ovr+=','
            ovr+=''.join(ret_storclas_existente)

        if len(ret_avgrec_gerada) > 0:
            if ovr != '' or resultado != '':
                ovr+=','
            ovr+=''.join(ret_avgrec_gerada)
        elif len(ret_avgrec_existente) > 0:
            if ovr != '' or resultado != '':
                ovr+=','
            ovr+=''.join(ret_avgrec_existente)

        resultado+= ovr
        # print(f'override  {resultado}')
        if self.get_proximo()  != None:
            return  self.get_proximo().montar_override(data, existente, resultado)
        return resultado

