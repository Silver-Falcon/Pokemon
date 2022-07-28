class Pokemon:
    name = ""
    hp = 50
    _type = ""
    weak = ""
    level = 1
    last_attack = ""
    
    def __init__(self, name = "", hp = "",
                 _type = "", weak = "", level = 1):
        self.name = name
        self.hp = hp*level
        self._type = _type
        self.weak = weak
        self.level = level
        
    def __str__(self):
        return self.name+", ("+str(self.hp)+", Level: "+str(self.level)+")"
    
    def __repr__(self):
        return str(self)
    
    def attack(self, pokemon, attacks):
        global last_attack
        
        if Pokemon.last_attack == "snow":
            print("!הפוקימון קפוא בגלל התקפת קרח")
            Pokemon.last_attack = "";
            return

        selected = input("בחר מתקפה נגד: "+pokemon.name+": ").lower()
        if (selected in attacks):
            if (attacks[selected].damage < 0):
                pokemon = self
            pokemon.hp = pokemon.hp - attacks[selected].get_damage(pokemon)
        else:
            print("התקפה לא קיימת")
        Pokemon.last_attack = selected
        print("pokemon: ", pokemon) 
