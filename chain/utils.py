def get_useful_parameters(data, qt: int):
    return data[data.find('DD') + qt:]


def get_cab(texto: str):
    return texto[0:texto.find(' DD') + 4]


def get_needed_comma(ovr, resultado):
    if ovr != '' or resultado != '':
        ovr += ','
    return ovr



