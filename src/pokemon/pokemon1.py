from attack import Attack

a = 1
b = 2
    
print("ברוך הבא למשחק הפוקימון של נועם לוי")

pokemons = [
    {"name": "פיקאצ'ו", "hp": 100, "type":"lightning"},
    {"name": "צ'רמנדר", "hp": 100, "type":"fire"},
    {"name": "סקורתל",  "hp": 150, "type":"water"}
    ]
for p in pokemons:
    print(p)

a = input(" בחר פוקמון ")
b = input(" בחר פוקמון ")
pokemon1 = pokemons[int(a)-1]
pokemon2 = pokemons[int(b)-1]
print("pokemon1", pokemon1)
print("pokemon2", pokemon2)
last_attack = ""

attacks = {
    "ice":      Attack("ice",   10, "ice"),
    "fire":     Attack("fire",  15, "fire"),
    "shadow":   Attack("shadow",20, "shadow"),
    "boom":     Attack("boom",  25, "fire"),
    "lightning": Attack("lightning", 15, "lightning"),
    "water":    Attack ("water", 10, "water"),
}
print("Attacks:")
for a in attacks:
    print(a)

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
