from __future__ import annotations
import re
from chain.params_enum import Parameters
from chain.overrideChain import OverrideChain
from chain.util_funcs import get_needed_comma, get_useful_parameters


class ClasChain(OverrideChain):
    __XDEFCOMP = 'XDEFCOMP'
    __list_clas_parameters = [
        Parameters.DATACLAS,
        Parameters.STORCLAS,
        Parameters.AVGREC
    ]

    def get_parameters(self, data, retorno=None) -> list:
        print('processing _clas...')
        if retorno is None:
            retorno = []
        data = get_useful_parameters(data, 4)
        for param in self.__list_clas_parameters:
            reg_expr = f'({param.value}=)(\w+)'
            ret_expr = re.search(reg_expr, data)
            if ret_expr is not None:
                retorno.append(ret_expr.group())

        if self.get_next() is not None:
            return self.get_next().get_parameters(data, retorno)
        return retorno

    def make_override(self, data=None, existente=None, result=None) -> str:
        print('generating _clas override ...')
        if data is None:
            data = []

        if existente is None:
            existente = []

        if result is None:
            result = ''

        ovr = ''
        for param in self.__list_clas_parameters:
            ret_generated_param = [x for x in data if x is not None and param.value in x]
            ret_existent_param = [x for x in existente if x is not None and param.value in x]
            if len(ret_generated_param) > 0:
                ovr = self.__get_concatenated_params(ovr, param, result, ret_existent_param, ret_generated_param)
            elif len(ret_existent_param) > 0:
                ovr = self.__get_concatenated_params(ovr, param, result, ret_generated_param, ret_existent_param)

        result += ovr
        if self.get_next() is not None:
            return self.get_next().make_override(data, existente, result)
        return result

    def __get_concatenated_params(self, ovr, param, result, ret_param1, ret_param2):
        ovr = get_needed_comma(ovr, result)
        if param.value == Parameters.DATACLAS.value:
            ovr = self.__get_defcomp(ovr, ret_param1, ret_param2)
        else:
            ovr += ''.join(ret_param2)
        return ovr

    def __get_defcomp(self, ovr, ret_param1, ret_param2):
        ovr += f'{Parameters.DATACLAS.value}={self.__XDEFCOMP}' \
            if ''.join(ret_param1) == \
               f'{Parameters.DATACLAS.value}={self.__XDEFCOMP}' \
            else ''.join(ret_param2)
        return ovr
