# print("Chcete vědět zda jste dospělí?")
# print("Pokud ano, stiskněte Enter.")
# input("")
#
# vek=int(input("Kolik je vám let?\n"))
#
# if vek >=18:
#     print("Jste dospělý.")
# else: print("Nejste dospělý.")
# print("Děkujeme za vyplnění.")


# # Úkol - ceny lístků v kině

print("Vítejte v kině.\nJste studentem?\n")
student = input("Zadejte ANO nebo NE.\n").lower() # vytvořímě proměnnou student a poté ho vyzveme inputem, aby zadal ANO nebo NE a.lower() - převede na malá písmena, aby se to dalo porovnat s podmínkou níže. Pokud uživatel zadá něco jiného, tak se to neprovede.
if student == "ANO" or student == "ano": # pokud Uživatel zadá ANO - podmínka or je nebo, čili pokud je splněna jedna z podmínek, tak se provede tato část kódu - jestli je opravdu rovno tak ==
    print("Cena lístku je 100 Kč.")
elif student == "NE" or student == "ne": print("Vstupenka stojí 200kč.")#pokud Uživatel zadá NE
else: print("Můžete zadat pouze ano nebo ne, opakujte akci.") # pokud Uživatel zadá NE
print("Přistupte k pokladně a zaplaťte.")
