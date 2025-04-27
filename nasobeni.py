#print("Zadejte číslo k zdvojnásobení")
#s = input()
#a = int(s)
#a = a * 2
#print(a)

print("Vítejte v kalkulačce")
print("Zadejte první číslo:")   # Zkusme třeba pí, tedy 3.14
a = float(input())
print("Zadejte druhé číslo:")  # Zkusme třeba e, tedy 2.72
b = float(input())
soucet = a + b
rozdil = a - b
soucin = a * b
podil = a / b
print(f"Součet: {soucet}")
print(f"Rozdíl: {rozdil}")
print(f"Součin: {soucin}")
print(f"Podíl: {podil}")
print("Děkuji za použití kalkulačky!")

#input()	Získá text od uživatele
#int()	Převede text na číslo
#int(input())	Spojí obě – přečte vstup a převede
#print()	Vypíše něco na obrazovku