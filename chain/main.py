from chain.override import OverrideImpl
import util_funcs

if __name__ == "__main__":
    ovr_gerado = 'STEP.DDNAME DD UNIT=(SYSDA,25),STORCLAS=EXTNOST5,DATACLAS=XDEFCOMP'
    ovr_existente = 'STEP.DDNAME DD UNIT=(SYSDA,25),AVGREC=K,DATACLAS=XDEFAULT,BUF=40'
    ovr = OverrideImpl()
    override = ovr.get_overrides(ovr_existente, ovr_gerado)
    adjusted_ovr = util_funcs.adjust_override(override, 71)
    print(adjusted_ovr)

