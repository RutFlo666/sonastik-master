from Modul import *
from random import *

rus=[] #vene sonad
est=[] #eesti sonad
rus=loe_failist("Rus.txt")
est=loe_failist("Est.txt")
print(rus)
print(est)
while True:
    v=input("\n1-Tolkimine\n2-Sonade lisamine\n3-Muutmine\n4-Kontroll\n5-Lopp\n")
    if v=="1":
        print("Tolkimine")
        sona=input("Sisesta sona tolkimiseks: ")
        tolke=tolkinine(sona,rus,est)
        print(tolke)
    elif v=="2":
        print("Sonade lisamine")
        est_sona=input("Sisesta sona eesti keeles: ")
        rus_sona=input("Sisesta sona vene keeles: ")
        teksti_lisamine_failisse("Est.txt",est_sona,est)
        teksti_lisamine_failisse("rus.txt",rus_sona,rus)
    elif v=="3":  
        print("Sonade muutmine")
        sona=input("Sisesta sona muutmiseks: ")
        muutm=muutmine(sona,rus,est)
        print(muutm)
    elif v=="4":  
        print("Teadmiste kontroll")
        k=int(input("Kui palju sonad? "))
        q=0
        for i in range (0, k):
            h=randint(0,1)
            t=randint(0,len(rus)-1)
            if h==0:
                sona=rus[t]
                tolk=est[t]
            else:
                sona=est[t]
                tolk=rus[t]
            kusimus="kusimus "+str(i+1)+": mis tahendab "+sona+"? "    
            vastus=input(kusimus)
            if vastus==tolk:
                q+=1
                print(" Oige!")
            else:
                print(" Vale! Oige vastus:", tolk)
        h=(q*100)/k
        print("Teie hinne:", str(int(h))+"%")
    else:
        print("Koike head!")
        break