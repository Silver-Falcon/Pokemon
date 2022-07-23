from attack import Attack


    
print("ברוך הבא למשחק הפוקימון של נועם לוי")

pokemon1 = {"name": "פיקאצ'ו", "hp": 100, "type":"lightning"}
pokemon2 = {"name": "צ'רמנדר", "hp": 100, "type":"fire"}

print("pokemon1:", pokemon1)
print("pokemon2:", pokemon2)


last_attack = ""

attacks = {
    "ice":      Attack("ice", 10),
    "fire":     Attack("fire", 15),
    "shadow":   Attack("shadow",20),
    "boom":     Attack("boom",25),
    "lightning": Attack("lightning", 15),
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

    selected = input("בחר מתקפה נגד: "+pokemon["name"]+": ")
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
