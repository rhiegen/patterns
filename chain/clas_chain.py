from __future__ import annotations
import enum
import re
from typing import List
from chain.params_enum import Parameters
from chain.overrideChain import OverrideChain
from chain.utils import get_needed_comma, get_useful_parameters


class ClasChain(OverrideChain):
    __XDEFCOMP = 'XDEFCOMP'
    __list_clas_parameters = [
        Parameters.DATACLAS,
        Parameters.STORCLAS,
        Parameters.AVGREC
    ]

    def get_parameters(self, data, retorno: List = []) -> List:
        print('processando _clas...')
        data = get_useful_parameters(data,4)
        for param in self.__list_clas_parameters:
            reg_expr = f'({param.value}=)(\w+)'
            ret_expr = re.search(reg_expr, data)
            if ret_expr is not None:
                retorno.append(ret_expr.group())

        if self.get_next() is not None:
            return self.get_next().get_parameters(data, retorno)
        return retorno

    def make_override(self, data: List, existente: List = [], resultado: str = None) -> str:
        print('gerando override _clas...')
        ovr = ''
        for param in self.__list_clas_parameters:
            ret_param_gerada = [x for x in data if x is not None and param.value in x]
            ret_param_existente = [x for x in existente if x is not None and param.value in x]
            if len(ret_param_gerada) > 0:
                ovr = get_needed_comma(ovr, resultado)
                if param.value == Parameters.DATACLAS.value:
                    ovr = self.get_defcomp(ovr, ret_param_existente, ret_param_gerada)
                else:
                    ovr += ''.join(ret_param_gerada)
            elif len(ret_param_existente) > 0:
                ovr = get_needed_comma(ovr, resultado)
                if param.value == Parameters.DATACLAS.value:
                    ovr = self.get_defcomp(ovr, ret_param_gerada, ret_param_existente)
                else:
                    ovr += ''.join(ret_param_existente)

        resultado += ovr
        if self.get_next() is not None:
            return self.get_next().make_override(data, existente, resultado)
        return resultado

    def get_defcomp(self, ovr, ret_param1, ret_param2):
        ovr += f'{Parameters.DATACLAS.value}={self.__XDEFCOMP}' \
            if ''.join(ret_param1) == \
               f'{Parameters.DATACLAS.value}={self.__XDEFCOMP}' \
            else ''.join(ret_param2)
        return ovr
