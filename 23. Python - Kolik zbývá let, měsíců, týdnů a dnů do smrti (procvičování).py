age=int(input("Zadejte svůj věk:\n")) # proměnná se píše jako první!  funkce input az jako druhá !!!!
vek=age
zbyva=90-vek
mesic=age*12
tyden=age*52
den=age*365
print(f"Do 90 let ti zbývá? {zbyva} let, {mesic} měsíců, {tyden} týdnů, {den} dní.")

print("https://kalendar.beda.cz/rocni-planovaci?type=s1")
odpracovano=int(input("Kolik týdnů jsi odpracoval?\n"))
tydny=int(input("Kolik pracovních týdnů má tento rok?\n"))

zbyva=tydny-odpracovano
print(f"Do konce roku zbývá {zbyva} pracovních týdnů.")