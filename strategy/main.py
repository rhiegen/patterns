from pattern_chain import *



def get_parameter(__ovr:str)-> List:
        __chain = None
        __chain2 = None
        __chain = Unit_chain()
        __chain2 = Clas_chain()
        __chain.set_proximo(__chain2)

        return __chain.get_parameters(__ovr,[])


        
if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    ovr_gerado = 'STEP.DDNAME DD UNIT=(SYSDA,25),DATACLAS=XDEFAULT,STORCLAS=EXTNOST3'
    ovr_existente = 'STEP.DDNAME DD UNIT=(SYSDA,25)'

    


    


    # chain = Unit_chain()
    # chain2 = Clas_chain()
    # chain.set_proximo(chain2)


    # lista_gerada = chain.get_parameters(ovr_gerado)
    lista_gerada = get_parameter(ovr_gerado)
    print(f'Lista gerada {lista_gerada}')
    lista_existente = get_parameter(ovr_existente)


    # lista_existente = chain.get_parameters(ovr_existente)
    print(f'Lista existente {lista_existente}')

    
    resultado = chain.validate(lista_gerada, lista_existente)
   




    # clas = []
    # context.strategy = Unit_Strategy()

    # context.set_data(ovr_gerado,ovr_existente)
    # retorno = context.processa() 
    # unit = retorno if retorno != None else ''

    # context.strategy = GenericClas_Strategy()
    # clas = context.processa()
    # dataclas = clas[0] if clas[0] != None else ''
    # storclas = clas[1] if clas[1] != None else ''


    # ovr_total = ''



    # ovr_total+=unit 
    # if ovr_total != '':
    #     if dataclas != '':
    #         ovr_total+=','

    #     ovr_total+=dataclas

    #     if storclas != '':
    #         ovr_total+=','

    #     ovr_total+=storclas

    # print(f'ovr_total {ovr_total}')


