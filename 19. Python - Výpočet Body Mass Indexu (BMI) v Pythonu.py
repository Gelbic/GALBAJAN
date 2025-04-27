vyska = input("zadejte svou výšku v metrech:\n")    # musime urcit promennou - zatím je to string
vaha = input("zadejte svou váhu v kilogramech:\n")

bmi = float(vaha) / float(vyska) ** 2 # jelikož píšeme v metrech a to bude 1.8 tak musíme dát float
bmi1 = int(bmi) # převedeme na int aby to nebylo s desetinnou čárkou
print ("Váš BMI je:" + str(bmi1)) # převedeme na string aby to šlo vyprintovat
# print (f"Váš BMI je: {bmi1}") # nebo použijeme f-string
