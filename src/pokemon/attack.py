class Attack:
    name = ""
    _type = ""
    damage = 0
    weak = ""

    def __init__(self, name = "", damage = "",
                 _type = "", weak = ""):
        self.name = name
        self.damage = damage
        self._type = _type
        self.weak = weak
        
    def __str__(self):
        return self.name+", "+str(self.damage)+", (Type: "+self._type+")"
    
    def __repr__(self):
        return str(self)
    
    def print2(self):
        str(self)
    
    def get_damage(self, pokemon):
        result = self.damage
        if (pokemon._type == self._type):
            result = 0
            print("!המתקפה לא השפיעה")
        if (pokemon.weak == self._type):
            result = result*2
            print("!המתכפה כן השפיעה ")
        return result



