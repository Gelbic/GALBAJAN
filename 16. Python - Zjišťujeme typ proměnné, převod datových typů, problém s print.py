age = 40
# chceme to vyprintovat ale to nejde protoze to neni string. Takže zjistime co je to za proměnnou
# a to takto : print(type(age))
# v terminálu nám vyjelo -  <class 'int'>  # což je integer

# a máme dvě varianty.  Bud převedeme proměnnou na string
# age = str(age) - # převedeme proměnnou na string
# nebo použijeme funkci str() přímo v printu a nebo použijeme f-string
print (str(age))
print (f"{age}")