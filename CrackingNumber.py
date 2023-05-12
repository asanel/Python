import random

zufallzahl: int = random.randint(0, 100)

print("Spiel CrackingNumber wurde gestartet...")

for i in range(5):
    eingabe = input(f"Rate die Zahl! Du hast {5 - i} Eingabeversuche: ")
    if(eingabe.isdigit()):
        if int(eingabe) < zufallzahl:
            print("Die eingegebene Zahl ist kleiner")
        elif int(eingabe) > zufallzahl:
            print("Die eingegebene Zahl ist größer")
        elif int(eingabe) == zufallzahl:
            print("Glückwunsch! Du hast die Zahl eraten")
            break
    else:
        print("Das ist keine Zahl!")


print(f"Ende des Spiels... Die Zufallzahl ist {zufallzahl}")