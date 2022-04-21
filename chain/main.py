from abc import ABC, abstractmethod
from chain.utils import get_cab
from clas_chain import ClasChain
from unit_chain import UnitChain


class Override(ABC):
    @abstractmethod
    def get_overrides(self, ovr_existente: str, ovr_gerado: str) -> str:
        pass


class OverrideImpl(Override, ABC):

    def get_overrides(self,ovr_existente: str, ovr_gerado: str) -> str:
        resultant = ''
        # __chain = None
        # __chain2 = None

        __unit = UnitChain()
        __clas = ClasChain()
        __unit.set_next(__clas)

        lista_gerada = __unit.get_parameters(ovr_gerado, [])
        lista_existente = __unit.get_parameters(ovr_existente, [])
        resultant = __unit.make_override(lista_gerada, lista_existente, resultant)
        # cria texto final do override
        cab = get_cab(ovr_gerado)
        return cab + resultant


if __name__ == "__main__":
    override = ''
    ovr_gerado = 'STEP.DDNAME DD UNIT=(SYSDA,25),STORCLAS=EXTNOST5,DATACLAS=XDEFCOMP'
    ovr_existente = 'STEP.DDNAME DD UNIT=(SYSDA,25),AVGREC=K,DATACLAS=XDEFAULT'
    ovr = OverrideImpl()
    override = ovr.get_overrides(ovr_existente, ovr_gerado)
    print(override)


