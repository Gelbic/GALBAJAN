# PODMÍNKY

print("Vítejte na horské dráze.\n")
height = int(input("Jaká je vaše výška v cm?\n"))

# podmínka pro výšku´- if je podmínka,něco co končí pravda nebo nepravda height je proměnná a poté následuje je vyšší nebo rovno a zvolená hodnota. Po podmínce musí být dvojtečka.

if height >= 87: #končí datovým typem boolean (pravda/nepravda)
    print("Můžete jet na horské dráze.")
    age=int(input("Jaký je váš věk?\n")) # bez int by to bylo jako string a ne jako číslo.
    if age <5:
        print("Nemáte věk na to, abyste mohli jet na horské dráze.")
    elif age <12: # pokud je věk menší než 10
        print("Cena lístku je 50 Kč.")
    elif age <18:
        print("Cena lístku je 100 Kč.")
    else:
        print("Cena lístku je 200 Kč.")
else:   #toto znamená JINAK - čili pokud není splněna podmínka, tak se provede tato část kódu
    print("Nemůžete jet na horské dráze.")
# print musí být správně odsazený, jinak to nebude fungovat
# musíme jít od nejnižšího věku k nejvyššímu, jinak by to nefungovalo. Pokud bychom dali 18 a 12, tak by to nefungovalo, protože by to vzalo 18 a ne 12. Protože je to podmínka, která se musí splnit.
# START
#  |
#  |-- age <= 5 ? --> Ano --> "Nemůžete jet."
#  |                 |
#  |                 Ne
#  |
#  |-- age <= 10 ? --> Ano --> "Cena lístku je 50 Kč."
#  |                 |
#  |                 Ne
#  |
#  |-- age <= 12 ? --> Ano --> "Cena lístku je 100 Kč."
#  |                 |
#  |                 Ne
#  |
#  |--> "Cena lístku je 200 Kč."
