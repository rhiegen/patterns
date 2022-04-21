from __future__ import annotations
from typing import List
from overrideChain import OverrideChain
import re
from chain.params_enum import Parameters
from chain.utils import get_useful_parameters


# def get_useful_parameters(data):
#     data = data[data.find('DD') + 3:]
#     return data


class UnitChain(OverrideChain):

    def get_parameters(self, data, retorno: list = []) -> List:
        unit = None
        print('processando unit...')
        data = get_useful_parameters(data,3)
        pattern_unit_simple = f'({Parameters.UNIT.value}=SYSDA)'
        pattern_unit_number = f'({Parameters.UNIT.value}=\(SYSDA\,)(\d+)(\))'
        match_unit_simple = re.search(pattern_unit_simple, data)
        match_unit_number = re.search(pattern_unit_number, data)
        if match_unit_number is not None:
            unit = match_unit_number.group()
        elif match_unit_simple is not None:
            unit = match_unit_simple.group()

        retorno.append(unit)

        if self.get_next() is not None:
            return self.get_next().get_parameters(data, retorno)
        return [retorno]

    def make_override(self, data: List, existente: List = [], resultado: str = None) -> str:
        print('Gerando override com unit...')
        ovr = ''
        ret_unit_gerada = [x for x in data if x is not None and Parameters.UNIT.value in x]

        if len(ret_unit_gerada) > 0:
            ovr += ''.join(ret_unit_gerada)

        resultado += ovr
        # print(f'override unit {resultado}')
        if self.get_next() is not None:
            return self.get_next().make_override(data, existente, resultado)
        return resultado
