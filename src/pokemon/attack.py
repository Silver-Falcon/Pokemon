class Attack:
    name = ""
    _type = ""
    damage = 0


    def __init__(self, name = "שם המתקפה", damage = "כמה נזק היא מורידה", _type = "סוג"):
        self.name = name
        self.damage = damage
        self._type = _type

    def __str__(self):
        return str(vars(self))
    
    def __repr__(self):
        return str(self)
    
    def get_damage(self, pokemon):
        result = self.damage
        if (pokemon["type"] == self._type):
            result = result-5
        return result
        
