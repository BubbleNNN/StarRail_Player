class Character:
    '''
    角色基类
    '''
    def __init__(self, name, level, hp, attack, defense, speed, critical_chance, critical_damage, break_effect, outgoing_healing_boost, max_energy, energy_regeneration_rate, effect_hit_rate, effect_resistance, physical_DMG_boost, fire_DMG_boost, ice_DMG_boost, lightning_DMG_boost, wind_DMG_boost, quantum_DMG_boost, imaginary_DMG_boost, phisical_RES_boost, fire_RES_boost, ice_RES_boost, lightning_RES_boost, wind_RES_boost, quantum_RES_boost, imaginary_RES_boost):
        self.name = name
        self.level = level
        self.hp = hp    
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.critical_chance = critical_chance #暴击率
        self.critical_damage = critical_damage #暴击伤害
        self.break_effect = break_effect #击破特攻
        self.outgoing_healing_boost = outgoing_healing_boost #治疗加成
        self.max_energy = max_energy #能量上限
        self.energy_regeneration_rate = energy_regeneration_rate #能量恢复效率
        self.effect_hit_rate = effect_hit_rate #效果命中
        self.effect_resistance = effect_resistance #效果抵抗
        self.physical_DMG_boost = physical_DMG_boost #增伤
        self.fire_DMG_boost = fire_DMG_boost
        self.ice_DMG_boost = ice_DMG_boost
        self.lightning_DMG_boost = lightning_DMG_boost
        self.wind_DMG_boost = wind_DMG_boost
        self.quantum_DMG_boost = quantum_DMG_boost
        self.imaginary_DMG_boost = imaginary_DMG_boost
        self.phisical_RES_boost = phisical_RES_boost #抗性
        self.fire_RES_boost = fire_RES_boost
        self.ice_RES_boost = ice_RES_boost
        self.lightning_RES_boost = lightning_RES_boost
        self.wind_RES_boost = wind_RES_boost
        self.quantum_RES_boost = quantum_RES_boost
        self.imaginary_RES_boost = imaginary_RES_boost
        self.debuff = []
        self.buff = []
    def get_state(self):
        return {
            "name": self.name,
            "level": self.level,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
            "energy_limit": self.energy_limit,
            "critical_chance": self.critical_chance,
            "critical_damage": self.critical_damage,
            "break_effect": self.break_effect,
            "outgoing_healing_boost": self.outgoing_healing_boost,
            "max_energy": self.max_energy,
            "energy_regeneration_rate": self.energy_regeneration_rate,
            "effect_hit_rate": self.effect_hit_rate,
            "effect_resistance": self.effect_resistance,
            "physical_DMG_boost": self.physical_DMG_boost,
            "fire_DMG_boost": self.fire_DMG_boost,
            "ice_DMG_boost": self.ice_DMG_boost,
            "lightning_DMG_boost": self.lightning_DMG_boost,
            "wind_DMG_boost": self.wind_DMG_boost,
            "quantum_DMG_boost": self.quantum_DMG_boost,
            "imaginary_DMG_boost": self.imaginary_DMG_boost,
            "phisical_RES_boost": self.phisical_RES_boost,
            "fire_RES_boost": self.fire_RES_boost,
            "ice_RES_boost": self.ice_RES_boost,
            "lightning_RES_boost": self.lightning_RES_boost,
            "wind_RES_boost": self.wind_RES_boost,
            "quantum_RES_boost": self.quantum_RES_boost,
            "imaginary_RES_boost": self.imaginary_RES_boost,
            'debuff': self.debuff,
            'buff': self.buff,
        }
    
class Team:
    def __init__(self, characters: list[Character]):
        self.characters = characters
    def get_number_of_characters(self):
        return len(self.characters)
    
class Enemy:
    
    def __init__(self, name, level, hp, attack, defense, speed, energy_limit, critical_chance, critical_damage, break_effect, outgoing_healing_boost, max_energy, energy_regeneration_rate, effect_hit_rate, effect_resistance, physical_DMG_boost, fire_DMG_boost, ice_DMG_boost, lightning_DMG_boost, wind_DMG_boost, quantum_DMG_boost, imaginary_DMG_boost, phisical_RES_boost, fire_RES_boost, ice_RES_boost, lightning_RES_boost, wind_RES_boost, quantum_RES_boost, imaginary_RES_boost):
        self.name = name
        self.level = level
        self.hp = hp    
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.physical_DMG_boost = physical_DMG_boost# 增伤
        self.fire_DMG_boost = fire_DMG_boost
        self.ice_DMG_boost = ice_DMG_boost
        self.lightning_DMG_boost = lightning_DMG_boost
        self.wind_DMG_boost = wind_DMG_boost
        self.quantum_DMG_boost = quantum_DMG_boost
        self.imaginary_DMG_boost = imaginary_DMG_boost
        self.phisical_RES_boost = phisical_RES_boost# 抗性
        self.fire_RES_boost = fire_RES_boost
        self.ice_RES_boost = ice_RES_boost
        self.lightning_RES_boost = lightning_RES_boost
        self.wind_RES_boost = wind_RES_boost
        self.quantum_RES_boost = quantum_RES_boost
        self.imaginary_RES_boost = imaginary_RES_boost
        self.physical_DMG_vunerability = 0 #易伤
        self.fire_DMG_vunerability = 0
        self.ice_DMG_vunerability = 0
        self.lightning_DMG_vunerability = 0
        self.wind_DMG_vunerability = 0
        self.quantum_DMG_vunerability = 0
        self.imaginary_DMG_vunerability = 0
        self.beaking_DMG_vunerability = 0 #击破易伤
        self.debuff = []
        self.buff = []
    def get_state(self):
        return {
            "name": self.name,
            "level": self.level,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
            "physical_DMG_boost": self.physical_DMG_boost,
            "fire_DMG_boost": self.fire_DMG_boost,
            "ice_DMG_boost": self.ice_DMG_boost,
            "lightning_DMG_boost": self.lightning_DMG_boost,
            "wind_DMG_boost": self.wind_DMG_boost,
            "quantum_DMG_boost": self.quantum_DMG_boost,
            "imaginary_DMG_boost": self.imaginary_DMG_boost,
            "phisical_RES_boost": self.phisical_RES_boost,
            "fire_RES_boost": self.fire_RES_boost,
            "ice_RES_boost": self.ice_RES_boost,
            "lightning_RES_boost": self.lightning_RES_boost,
            "wind_RES_boost": self.wind_RES_boost,
            "quantum_RES_boost": self.quantum_RES_boost,
            "imaginary_RES_boost": self.imaginary_RES_boost,
            'debuff': self.debuff,
            'buff': self.buff,
            "physical_DMG_vunerability": self.physical_DMG_vunerability,
            "fire_DMG_vunerability": self.fire_DMG_vunerability,
            "ice_DMG_vunerability": self.ice_DMG_vunerability,
            "lightning_DMG_vunerability": self.lightning_DMG_vunerability,
            "wind_DMG_vunerability": self.wind_DMG_vunerability,
            "quantum_DMG_vunerability": self.quantum_DMG_vunerability,
            "imaginary_DMG_vunerability": self.imaginary_DMG_vunerability,
            "beaking_DMG_vunerability": self.beaking_DMG_vunerability,
        }
        
class weapon:
    def __init__ (self, name, level, HP, ATK, DEF, superimposition):
        self.name = name
        self.level = level
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.superimposition = superimposition
        
class debuff:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.passing_round = 0
    def after_round(self, round_type):
        if round_type == 'normal':
            self.passing_round += 1
        if self.duration - self.passing_round <= 0:
            return False
        return True
    
class buff:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.passing_round = 0
    def after_round(self, round_type):
        if round_type == 'normal':
            self.passing_round += 1
        if self.duration - self.passing_round <= 0:
            return False
        return True

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