# PODMÍNKY

print("Vítejte na horské dráze.\n")
height = int(input("Jaká je vaše výška v cm?\n"))

# podmínka pro výšku´- if je podmínka,něco co končí pravda nebo nepravda height je proměnná a poté následuje je vyšší nebo rovno a zvolená hodnota. Po podmínce musí být dvojtečka.

if height >= 87: #končí datovým typem boolean (pravda/nepravda)
    print("Můžete jet na horské dráze.")
    age=int(input("Jaký je váš věk?\n")) # bez int by to bylo jako string a ne jako číslo.
    if age < 18:
        print("Cena lístku je 100 Kč.")
    else:
        print("Cena lístku je 200 Kč.")
else:   #toto znamená JINAK - čili pokud není splněna podmínka, tak se provede tato část kódu
    print("Nemůžete jet na horské dráze.")
# print musí být správně odsazený, jinak to nebude fungovat