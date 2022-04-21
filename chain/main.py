from chain.override import OverrideImpl

if __name__ == "__main__":
    ovr_gerado = 'STEP.DDNAME DD UNIT=(SYSDA,25),STORCLAS=EXTNOST5,DATACLAS=XDEFCOMP'
    ovr_existente = 'STEP.DDNAME DD UNIT=(SYSDA,25),AVGREC=K,DATACLAS=XDEFAULT'
    ovr = OverrideImpl()
    override = ovr.get_overrides(ovr_existente, ovr_gerado)
    print(override)
