def loe_failist(fail:str)->list:
    """Loetakse informatsioon failist ja tagastatakse info nagu jarjend
    :param str fail: faili nimetus
    .rtype: list
    """
    f=open(fail,'r',encoding="utf-8")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def tolkinine(sona:str,sonad:list,tolked:list)->str: #sonad-rus, tolked-est
    if sona in sonad:
        indeks=sonad.index(sona)
        return tolked[indeks]
    elif sona in tolked:
        indeks=tolked.index(sona)
        return sonad[indeks]
    else:
        return "Sona "+sona+" puudub"
def teksti_lisamine_failisse(fail:str,sona:str,sonad:list):
    sonad.append(sona)
    f=open(fail,'a',encoding="utf-8")
    f.write(sona+'\n')
    f.close()
def muutmine(sona:str,sonad:list,tolked:list)->str:
     if sona in sonad:
        indeks=sonad.index(sona)
        oige=input("Sisesta oige sona: ")
        sonad[indeks]=oige
        return "ok!"
     elif sona in tolked:
        indeks=tolked.index(sona)
        oige=input("Sisesta oige sona: ")
        tolked[indeks]=oige
        return "ok!"
     else:
        return "Sona "+sona+" puudub" 