# F-string
from ssl import HAS_NEVER_CHECK_COMMON_NAME
from turtledemo.minimal_hanoi import hanoi

x = 5
# print("Proměnná x má hodnotu: " + x) - tohle nám nepůjde protože x je int

print(f"Proměnná x má hodnotu: {x}") # převedeme proměnnou na string | f se píše hned po závorce a poté uvozovky.  po ukonceni musi byt uvozovky a zavorky
print("\n")
age = 28 # int nemusí být uvozovka
name = "JAN"  # string musí být uvozovka
print(f"Uživatel se jmenuje {name} a je mu {age} let.") #F-string nám to cele převádí na string takže age může být int a stejně to bude fungovat

