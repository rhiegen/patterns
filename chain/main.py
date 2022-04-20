from pattern_chain import UnitChain, ClasChain


def get_cab(ovr_gerado):
    index = ovr_gerado.find(' DD')
    cab = ovr_gerado[0:index + 4]
    return cab

def get_overrides(ovr_existente: str, ovr_gerado: str) -> str:
    resultant = ''
    __chain = None
    __chain2 = None

    __chain = UnitChain()
    __chain2 = ClasChain()
    __chain.set_proximo(__chain2)

    lista_gerada = __chain.get_parameters(ovr_gerado, [])
    lista_existente = __chain.get_parameters(ovr_existente, [])
    resultant = __chain.montar_override(lista_gerada, lista_existente, resultant)
    # cria texto final do override
    cab = get_cab(ovr_gerado)
    return cab + resultant


if __name__ == "__main__":
    override = ''
    ovr_gerado = 'STEP.DDNAME DD UNIT=(SYSDA,25),STORCLAS=EXTNOST3,DATACLAS=XDEFAULT'
    ovr_existente = 'STEP.DDNAME DD UNIT=(SYSDA,25),AVGREC=K,DATACLAS=XDEFAULT'
    override = get_overrides(ovr_existente, ovr_gerado)
    print(override)
