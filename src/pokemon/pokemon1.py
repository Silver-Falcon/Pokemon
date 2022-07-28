from attack import Attack
from pokemon import Pokemon
from pprint import pprint
import json

player1 = 1
player2 = 2

print("ברוך הבא למשחק הפוקימון של נועם לוי")

pokemons = [
    Pokemon("פיקאצ'ו", 50, "lightning", "shadow",1),
    Pokemon("צ'רמנדר", 50, "fire",   "water", 2),
    Pokemon("סקורתל",  50, "water",  "lightning",2),
    Pokemon("גנגר",    50, "shadow", "fire", 1),
    Pokemon("גרדוס",   50, "dragon", "levi", 3),
    Pokemon("noam",    100,"levi",   "",1),
    Pokemon("dad",     10, "levi",   "",1),
]

i = 0
for p in pokemons:
    i = i+1
    print(str(i)+": "+str(p))
    #print(p.__dict__)

player1 = input(" בחר פוקמון ")
player2 = input(" בחר פוקמון ")
pokemon1 = pokemons[int(player1)-1]
pokemon2 = pokemons[int(player2)-1]
print("pokemon1", pokemon1)
print("pokemon2", pokemon2)

attacks = {
    "snow":         Attack("snow",   10, "ice"),
    "fire ball":    Attack("fire ball",  20, "fire"),
    "darkness":     Attack("darkness",20, "shadow"),
    "spark":        Attack("spark", 35, "lightning"),
    "aqua tail":    Attack("aqua tail", 20, "water"),
    "dragon claw":  Attack("dragon claw", 25, "dragon"),
    "gesr":         Attack("gesr", 25, "water"),
    "ice bomb":     Attack("ice bomb", 25, "ice"),
    "or":           Attack("or", 50, "levi"),
    "hp":           Attack("hp", -20, "life")
}

print("Attacks:")
for item in attacks.values():
    print(item)
        
while (pokemon2.hp > 0 and pokemon1.hp > 0):
    pokemon2.attack(pokemon1, attacks)
    if (pokemon1.hp > 0):
        pokemon1.attack(pokemon2, attacks)
    
print("!המשחק הסתיים. כל הכבוד")

#פוקמון יוכל להישתמש רק במכות מהסוג שלו


