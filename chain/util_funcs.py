import re
from chain.params_enum import Parameters


def get_useful_parameters(data):
    start_in = data.find(' DD ') + 4
    return data[start_in:]


def get_cab(texto: str) -> str:
    start_in = texto.find(' DD ') + 4
    return texto[:start_in]


def get_needed_comma(ovr, resultado):
    if ovr != '' or resultado != '':
        ovr += ','
    return ovr


def adjust_override(ovr: str, cab: str, max_len: int) -> list:
    # cab = get_cab(ovr)
    ovr = get_useful_parameters(ovr)
    unit = get_unit(ovr)
    len_cab = len(cab)
    a_retirar = ovr[ovr.find(unit):len(unit) + ovr.find(unit) + 1]
    ovr = get_ovr_without_unit(ovr, a_retirar)
    a_retirar = a_retirar[:-1]
    # particiona o restante
    part_size = 0
    new_ovr = ''
    ovr_list = []
    qt_vezes = 0
    partes = ovr.split(',')
    for i in range(len(partes)):
        new_ovr = get_new_ovr(partes[i], len_cab, max_len, new_ovr, ovr_list, part_size, qt_vezes)
    compose_ovr(a_retirar, cab, max_len, ovr_list, unit, new_ovr)
    return ovr_list


def compose_ovr(a_retirar, cab, max_len, ovr_list, unit, new_ovr):
    if len(ovr_list) > 1:
        ovr_list.append('                 ' + new_ovr)
    else:
        ovr_list.append(new_ovr + '\n')

    if len(ovr_list[len(ovr_list) - 1]) + len(a_retirar) + 2 > max_len:
        ovr_list.append(unit)
    else:
        ovr_list[len(ovr_list) - 1] += '                 ' + a_retirar
    for i in range(len(ovr_list)):
        ovr_list[i] = "//" + cab + ovr_list[i] if i == 0 else ovr_list[i]


def get_new_ovr(partes, len_cab, max_len, new_ovr, ovr_list, part_size, qt_vezes):
    part_size += len(partes)
    tamanho = part_size + len_cab if qt_vezes == 0 else part_size
    if tamanho > max_len:
        qt_vezes += 1
        if qt_vezes == 1:
            ovr_list.append(new_ovr + '\n')
        else:
            ovr_list.append('                 ' + new_ovr + '\n')
        new_ovr = ''
        # part_size = len(partes)
    else:
        new_ovr += partes + ','
    return new_ovr


def get_unit(ovr):
    unit = ''
    pattern_unit_simple = f'({Parameters.UNIT.value}=SYSDA)'
    pattern_unit_number = f'({Parameters.UNIT.value}=\(SYSDA\,)(\d+)(\))'
    match_unit_simple = re.search(pattern_unit_simple, ovr)
    match_unit_number = re.search(pattern_unit_number, ovr)
    if match_unit_number is not None:
        unit = match_unit_number.group()
    elif match_unit_simple is not None:
        unit = match_unit_simple.group()
    return unit


def get_ovr_without_unit(ovr, a_retirar):
    ovr = ovr.replace(a_retirar, '')
    return ovr
