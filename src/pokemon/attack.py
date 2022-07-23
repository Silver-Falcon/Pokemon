class Attack:
    name = ""
    damage = 0


    def __init__(self, name = "שם המתקפה", damage = "כמה נזק היא מורידה"):
        self.name = name
        self.damage = damage

    def __str__(self):
        return str(vars(self))

    def get_damage(self, pokemon):
        result = self.damage
        if (pokemon["type"] == self.name):
            result = result-5
        return result
        
