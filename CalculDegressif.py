date = input("Entrez votre date sous forme : jj/mm ")
prix = int(input("Entrez votre prix : "))
tva = int(input("Entrez le montant de la TVA : "))
durée = int(input("Entre votre durée d'amortissement : "))

if (durée < 5 and durée > 3):
    coeff = 1.25
elif (durée > 4 and durée < 7):
    coeff = 1.75
elif (durée > 6):
    coeff = 2.25

data = date.split("/")
pro_rata = (12-int(data[1])+1)/12
HT = prix / (1 + (tva / 100))
pourcent = 100 / durée / 100
taux = pourcent * coeff
TL = 100/(durée)
pr_annuité = HT * taux * pro_rata

print("|   N   |   VNC Début   |   Amortissement   |   Amortissement cumulé   |   VNC Fin   |   Taux Linéaire   |")
print("-" * 106)

for N in range(1,durée + 1):
    TL = 100/(durée+1-N)
    #print(TL,taux)
    if N == 1:
        VNC_Début = HT
        VNC_Fin = HT - pr_annuité
        Amort_Cumulé = pr_annuité
        print(f"|   {N}   |   {VNC_Début:>9.2f}   |   {pr_annuité:>13.2f}   |   {Amort_Cumulé:>20.2f}   |   {VNC_Fin:>7.2f}   |     {TL:>8.2f}%     |")
    elif TL > taux*100 :
        VNC_Début = VNC_Fin
        Amort = VNC_Début * (TL/100)
        Amort_Cumulé += Amort
        VNC_Fin = VNC_Début - Amort
        print(f"|   {N}   |   {VNC_Début:>9.2f}   |   {Amort:>13.2f}   |   {Amort_Cumulé:>20.2f}   |   {VNC_Fin:>7.2f}   |     {TL:>8.2f}%     |")
    else:
        VNC_Début = VNC_Fin
        Amort = VNC_Début * taux
        Amort_Cumulé += Amort
        VNC_Fin = VNC_Début - Amort
        print(f"|   {N}   |   {VNC_Début:>9.2f}   |   {Amort:>13.2f}   |   {Amort_Cumulé:>20.2f}   |   {VNC_Fin:>7.2f}   |     {TL:>8.2f}%     |")
