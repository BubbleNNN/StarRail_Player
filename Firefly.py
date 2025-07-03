from utils import Character, Team, weapon, debuff, buff, Enemy

class Routed(debuff):
    def __init__(self):
        super().__init__(
            name = 'Routed',
            duration = 2,
        )
    def take_effect(self,target:list[Enemy]):
        for enemy in target:
            if self not in enemy.get_state()['debuff']:
                enemy.debuff.append(self)
                enemy.beaking_DMG_vunerability *= 0.24
                enemy.speed -= enemy.speed * 0.2
            

class whereabouts_should_the_dreams_rest(weapon):
    def __init__(self, level):
        super().__init__(
            name = 'Whereabouts Should the Dreams Rest',
            level = level,
            HP = 1164,
            ATK = 476,
            DEF = 529,
            superimposition = 1,
        )

class Fierfly(Character):
    def __init__(self, level):
        super().__init_(
            name = 'Firefly',
            level = level,
            hp = 3068,
            attack = 2329,
            defense = 1366,
            speed = 169,
            critical_chance = 7.9,
            cricital_damage = 61.6,
            break_effect = 243.5,
            outgoing_healing_boost = 0,
            max_energy = 240,
            energy_regeneration_rate = 100,
            effect_hit_rate = 19,
            effect_resistance = 37,
            physical_DMG_boost = 0,
            fire_DMG_boost = 0,
            ice_DMG_boost = 0,
            lightning_DMG_boost = 0,
            wind_DMG_boost = 0,
            quantum_DMG_boost = 0,
            imaginary_DMG_boost = 0,
            phisical_RES_boost = 0,
            fire_RES_boost = 0,
            ice_RES_boost = 0,
            lightning_RES_boost = 0,
            wind_RES_boost = 0,
            quantum_RES_boost = 0,
            imaginary_RES_boost = 0
        )
        