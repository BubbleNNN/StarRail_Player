class Enemy:
    
    def __init__(self, name, level, hp, attack, defense, speed, energy_limit, critical_chance, critical_damage, break_effect, outgoing_healing_boost, max_energy, energy_regeneration_rate, effect_hit_rate, effect_resistance, physical_DMG_boost, fire_DMG_boost, ice_DMG_boost, lightning_DMG_boost, wind_DMG_boost, quantum_DMG_boost, imaginary_DMG_boost, phisical_RES_boost, fire_RES_boost, ice_RES_boost, lightning_RES_boost, wind_RES_boost, quantum_RES_boost, imaginary_RES_boost,toughness):
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
        self.in_break = False
        self.weakness = []
        self.fake_weakness = []#不减抗的弱点
        self.toughness = toughness#韧性
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
            "in_break": self.in_break
        }