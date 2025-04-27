print("Vítejte v kalkulačce na výpočet plateb.\n")
input("Chcete výpočítat částku na osobu?\nStiskněte Enter pro pokračování.\n")

celkem = float(input("Kolik máte celkem zaplatit?\n"))
spropitne = float(input("Kolik % chcete dát spropitné?\n"))
pocet = int(input("Mezi kolik lidí se chcete rozdělit?\n"))
#celý výpočet může vypadat takto pocet1 = (celkem+(celkem*spropitne/100)) / pocet
# nebo takto
spropitne1= (spropitne / 100) * celkem
celek2=celkem + spropitne1
pocet1 = celek2 / pocet
zaokrouhleno = round(pocet1, 2)
zaokrouhleno2 = round(spropitne1, 2)
zaokrouhleno3="{:.2f}".format(zaokrouhleno)  # zaokrouhleno a naformátováno na 2 desetinná místa | "{:.2f}".format - toto je formátovací řetězec -https://mkaz.blog/working-with-python/string-formatting
print(f"Po započtení spropitného by měl každý zaplatit - {pocet1} a to je zaokrouhleno {zaokrouhleno3} Kč.\n Spropitné činí {spropitne1} a to je zaokrouhleno: {zaokrouhleno2} Kč.")
