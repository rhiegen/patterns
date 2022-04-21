import re

ovr = 'STEP.DDNAME DD UNIT=(SYSDA,30),DATACLAS=XDEFAULT,STORCLAS=EXTNOST3'
indice = ovr.find('DD ')
string = ovr[indice + 3:]
num = 10
if num > 9:
    print('maior que 9')
elif num == 10:
    print('numero = 10')


def transform(entrada: str) -> list:
    """
    Transforma a entrada em uma lista de strings
    """
    return re.split(r'\s*,\s*', entrada)


print(transform(ovr))

# join list elements to string with comma
print(','.join(transform(ovr)))
# add a number of spaces before each element
print(' '.join(transform(ovr)))
# add a number of tabs before each element
print('\t'.join(transform(ovr)))

# add spaces before a string
print(ovr.replace('DD ', 'DD '))
ovr = 'ola'


def set_filling_to_left_side(sp_qt: int, fill_char: str = ' ') -> str:
    return ovr.rjust(len(ovr) + sp_qt, fill_char)

def set_filling_to_right_side(sp_qt: int, fill_char: str = ' ') -> str:
    return ovr.ljust(len(ovr) + sp_qt, fill_char)

ljust = set_filling_to_left_side(20, '*')

print(ljust)
rjust = set_filling_to_right_side(20, '*')
print(rjust)
