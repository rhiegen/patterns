from __future__ import annotations
from overrideChain import OverrideChain
from chain.params_enum import Parameters
from chain.util_funcs import get_useful_parameters, get_unit


class UnitChain(OverrideChain):

    def get_parameters(self, data, retorno=None) -> list:
        if retorno is None:
            retorno = []
        unit = None
        print('processing unit...')
        data = get_useful_parameters(data)
        unit = get_unit(data)

        retorno.append(unit)

        if self.get_next() is not None:
            return self.get_next().get_parameters(data, retorno)
        return [retorno]

    def make_override(self, data=None, existente=None, resultado=None) -> str:
        print('generating unit override ...')
        if existente is None:
            existente = []

        if resultado is None:
            resultado = ''

        if data is None:
            data = []

        ovr = ''
        ret_generated_unit = [x for x in data if x is not None and Parameters.UNIT.value in x]

        if len(ret_generated_unit) > 0:
            ovr += ''.join(ret_generated_unit)

        resultado += ovr
        # print(f'override unit {resultado}')
        if self.get_next() is not None:
            return self.get_next().make_override(data, existente, resultado)
        return resultado
