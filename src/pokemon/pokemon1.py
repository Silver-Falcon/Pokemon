from attack import Attack
from pprint import pprint

player1 = 1
player2 = 2
    
print("ברוך הבא למשחק הפוקימון של נועם לוי")

pokemons = [
    {"name": "פיקאצ'ו", "hp": 90, "type":"lightning","weak": "shadow"},
    {"name": "צ'רמנדר", "hp": 85, "type":"fire","weak": ""},
    {"name": "סקורתל",  "hp": 100, "type":"water","weak": ""},
    {"name": "גנגר",    "hp": 90, "type":"shadow","weak": ""},
    {"name": "גרדוס",   "hp": 115, "type":"dragon","weak": ""},
    ]
for p in pokemons:
    print(p)

player1 = input(" בחר פוקמון ")
player2 = input(" בחר פוקמון ")
pokemon1 = pokemons[int(player1)-1]
pokemon2 = pokemons[int(player2)-1]
print("pokemon1", pokemon1)
print("pokemon2", pokemon2)

last_attack = ""

attacks = {
    "ice":      Attack("snow",   15, "ice"),
    "fire":     Attack("fire ball",  20, "fire"),
    "shadow":   Attack("darkness",20, "shadow"),
    "spark": Attack("lightning", 25, "lightning"),
    "Aqua Tail":    Attack ("water", 15, "water"),
    "dragon claw": Attack ("dragon claw", 25, "dragon"),
    "gesr":     Attack ("gesr", 20, "water"),
    "ice bomb": Attack ("ice bomb", 20, "ice"),
}

print("Attacks:")
for item in attacks.values():
    print(item)

def enter_attack(pokemon):
    global last_attack
    
    if last_attack == "ice":
        print("!הפוקימון קפוא בגלל התקפת קרח")
        last_attack = "";
        return

    selected = input("בחר מתקפה נגד: "+pokemon["name"]+": ").lower()
    if (selected in attacks):
        pokemon["hp"] = pokemon["hp"] - attacks[selected].get_damage(pokemon)
    else:
        print("התקפה לא קיימת")
    last_attack = selected
    print("pokemon: ", pokemon)  
        
while (pokemon2["hp"] > 0 and pokemon1["hp"] > 0):
    enter_attack(pokemon1)
    if (pokemon1["hp"] > 0):
        enter_attack(pokemon2)
    
print("!המשחק הסתיים. כל הכבוד")

#פוקמון יוכל להישתמש רק במכות מהסוג שלו


