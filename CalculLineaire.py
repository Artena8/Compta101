date = input("Entrez votre date sous forme : jj/mm ")
prix = int(input("Entrez votre prix : "))
tva = int(input("Entrez le montant de la TVA : "))
durée = int(input("Entre votre durée d'amortissement : "))

data = date.split("/")
pro_rata = (30 - int(data[0])) + (12 - int(data[1])) * 30
HT = prix / (1 + (tva / 100))
pr_annuité = HT * (100 / durée / 100) * (pro_rata / 360)
print(f"{pr_annuité:.2f}")
pourcent = 100 / durée / 100

print("|   N   |   VNC Début   |   Amortissement   |   Amortissement cumulé   |   VNC Fin   |")
print("-" * 86)

for N in range(durée + 1):
    if N == 0:
        VNC_Début = HT
        VNC_Fin = HT - pr_annuité
        Amort_Cumulé = pr_annuité
        print(f"|   {N}   |   {VNC_Début:>9.2f}   |   {pr_annuité:>13.2f}   |   {Amort_Cumulé:>20.2f}   |   {VNC_Fin:>7.2f}   |")
    elif N == durée:
        VNC_Début = VNC_Fin
        Amort_Cumulé += HT * pourcent - pr_annuité
        Amort = HT * pourcent - pr_annuité
        VNC_Fin = VNC_Début - Amort
        print(f"|   {N}   |   {VNC_Début:>9.2f}   |   {Amort:>13.2f}   |   {Amort_Cumulé:>20.2f}   |   {VNC_Fin:>7.2f}   |")
    else:
        VNC_Début = VNC_Fin
        Amort_Cumulé += HT * pourcent
        Amort = HT * pourcent
        VNC_Fin = VNC_Début - Amort
        print(f"|   {N}   |   {VNC_Début:>9.2f}   |   {Amort:>13.2f}   |   {Amort_Cumulé:>20.2f}   |   {VNC_Fin:>7.2f}   |")
