# PODMÍNKY

print("Vítejte na horské dráze.\n")
height = int(input("Jaká je vaše výška v cm?\n"))

# podmínka pro výšku´- if je podmínka,něco co končí pravda nebo nepravda height je proměnná a poté následuje je vyšší nebo rovno a zvolená hodnota. Po podmínce musí být dvojtečka.

if height >= 87: #končí datovým typem boolean (pravda/nepravda)
    print("Můžete jet na horské dráze.")
else:   #toto znamená JINAK - čili pokud není splněna podmínka, tak se provede tato část kódu
    print("Nemůžete jet na horské dráze.")
# print musí být správně odsazený, jinak to nebude fungovat