import re
from chain.params_enum import Parameters


def get_useful_parameters(data):
    start_in = data.find(' DD ') + 4
    return data[start_in:]


def get_cab(texto: str) -> str:
    start_in = texto.find(' DD ') + 4
    return texto[:start_in]


def add_needed_comma(ovr, result) -> str:
    if ovr != '' or result != '':
        ovr += ','
    return ovr


def adjust_override(ovr: str, cab: str, max_len: int) -> list:
    ovr = get_useful_parameters(ovr)
    unit = get_unit(ovr)
    len_cab = len(cab)
    start_pos = start_position_of_substring(ovr, unit)  # this one
    end_pos = end_position_of_substring(ovr, unit)  # this one
    substring_to_remove = ovr[start_pos:end_pos + 1]  # this one
    ovr = get_ovr_without_unit(ovr, substring_to_remove)
    substring_to_remove = substring_to_remove[:-1]
    # partition the rest
    part_size = 0
    new_ovr = ''
    ovr_list = []
    times = 0
    parts = ovr.split(',')
    for i in range(len(parts)):
        new_ovr = get_new_ovr(parts[i], len_cab, max_len, new_ovr, ovr_list, part_size, times)
    compose_ovr(substring_to_remove, cab, max_len, ovr_list, unit, new_ovr)
    return ovr_list


def compose_ovr(substring_to_remove, cab, max_len, ovr_list, unit, new_ovr):
    if len(ovr_list) > 1:
        ovr_list.append(add_chars_to_string_side(new_ovr, 18, ' ', 'left'))  # this one
    else:
        ovr_list.append(new_ovr + '\n')

    if len(ovr_list[len(ovr_list) - 1]) + len(substring_to_remove) + 2 > max_len:
        ovr_list.append(unit)
    else:
        ovr_list[len(ovr_list) - 1] += add_chars_to_string_side(substring_to_remove, 18, ' ', 'left')  # this one

    for i in range(len(ovr_list)):
        ovr_list[i] = "//" + cab + ovr_list[i] if i == 0 else ovr_list[i]


def get_new_ovr(parts, len_cab, max_len, new_ovr, ovr_list, part_size, times):
    part_size += len(parts)
    size = part_size + len_cab if times == 0 else part_size
    if size > max_len:
        times += 1
        if times == 1:
            ovr_list.append(new_ovr + '\n')
        else:
            ovr_list.append(add_chars_to_string_side(new_ovr, 18, ' ', 'left') + '\n')  # this one
        new_ovr = ''
    else:
        new_ovr += parts + ','
    return new_ovr


def get_unit(ovr):
    unit = ''
    pattern_unit_simple = f'({Parameters.UNIT.value}=SYSDA)'
    pattern_unit_number = f"({Parameters.UNIT.value}=\(SYSDA\,)(\d+)(\))"
    match_unit_simple = re.search(pattern_unit_simple, ovr)
    match_unit_number = re.search(pattern_unit_number, ovr)
    if match_unit_number is not None:
        unit = match_unit_number.group()
    elif match_unit_simple is not None:
        unit = match_unit_simple.group()
    return unit


def get_ovr_without_unit(ovr, to_remove):
    ovr = ovr.replace(to_remove, '')
    return ovr


# this one
def add_chars_to_string_side(string, qty, chars, side):
    if side == 'left':
        return qty * chars + string
    elif side == 'right':
        return string + qty * chars
    else:
        return string


# this one
def start_position_of_substring(string, substring) -> int:
    return string.find(substring)


# this one
def end_position_of_substring(string, substring) -> int:
    return string.find(substring) + len(substring)
