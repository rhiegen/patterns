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