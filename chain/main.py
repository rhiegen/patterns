from pattern_chain import *

def get_overrides(ovr_existente:str, ovr_gerado:str)-> str:
    resultado = ''
    __chain = None
    __chain2 = None
    
    __chain = Unit_chain()
    __chain2 = Clas_chain()
    __chain.set_proximo(__chain2)

    lista_gerada = __chain.get_parameters(ovr_gerado,[])
    lista_existente = __chain.get_parameters(ovr_existente,[])
    resultado = __chain.montar_override(lista_gerada, lista_existente, resultado)
    
    #cria texto final do override
    indice = ovr_gerado.find(' DD')
    cab = ovr_gerado[0:indice+4]
    override = cab +  resultado
    return override


        
if __name__ == "__main__":
    override = ''
    ovr_gerado = 'STEP.DDNAME DD UNIT=(SYSDA,25),STORCLAS=EXTNOST3,DATACLAS=XDEFAULT'
    ovr_existente = 'STEP.DDNAME DD UNIT=(SYSDA,25),AVGREC=K,DATACLAS=XDEFAULT'
    override = get_overrides(ovr_existente, ovr_gerado)
    print(override)
   

