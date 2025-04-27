from datetime import datetime  # Načteme si knihovnu pro práci s datem

# Zeptáme se na jméno
jmeno = input("Jak se jmenuješ? ")

# Zeptáme se na datum narození (ve formátu RRRR-MM-DD, např. 2000-04-18)
narozeni_text = input("Zadej datum narození (RRRR-MM-DD): ")

# Převedeme text na datum
narozeni = datetime.strptime(narozeni_text, "%Y-%m-%d")

# Zjistíme dnešní datum
dnes = datetime.now()

# Spočítáme rozdíl mezi dneškem a narozením
rozdil = dnes - narozeni

# Výpis výsledku
print(f"Ahoj, {jmeno}, žiješ už {rozdil.days} dní! 🎉")




