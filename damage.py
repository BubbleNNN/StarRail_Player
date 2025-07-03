class Damage:
    def __init__(self, damage_type, value):
        self.damage_type = damage_type
        self.value = value
    
    def get_damage(self):
        return {
            "damage_type": self.damage_type,
            "value": self.value
        }
    
    def __str__(self):
        return f"{self.value} {self.damage_type} damage"