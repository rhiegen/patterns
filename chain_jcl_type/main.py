from chain.override import OverrideImpl
import util_funcs

if __name__ == "__main__":
    generated_ovr = 'STEP.DDNAME DD UNIT=(SYSDA,25),STORCLAS=EXTNOST5,DATACLAS=XDEFCOMP'
    actual_ovr = 'STEP.DDNAME DD UNIT=(SYSDA,25),AVGREC=K,DATACLAS=XDEFAULT,BUF=40'
    ovr = OverrideImpl()
    override = ovr.get_overrides(actual_ovr, generated_ovr)
    cab = util_funcs.get_cab(override)
    adjusted_ovr = util_funcs.adjust_override(override, cab, 71)
    print(adjusted_ovr)
