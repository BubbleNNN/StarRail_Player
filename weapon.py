from debuff import Routed

class weapon:
    def __init__ (self, name, level, HP, ATK, DEF, superimposition,owner):
        self.name = name
        self.level = level
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.superimposition = superimposition
        self.owner = owner

class whereabouts_should_the_dreams_rest(weapon):
    def __init__(self, level, owner):
        super().__init__(
            name = 'Whereabouts Should the Dreams Rest',
            level = level,
            HP = 1164,
            ATK = 476,
            DEF = 529,
            superimposition = 1,
            owner = owner
        )
        self.weapon_default_effect()
    def weapon_default_effect(self):
        self.owner.break_effect += 0.6 
        self.owner.hp += self.HP
        self.owner.attack += self.ATK
        self.owner.defense += self.DEF
         
    def weapon_take_effect(self,target):
        routed = Routed(target)
        routed.take_effect()
        
    