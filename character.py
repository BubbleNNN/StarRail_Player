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
    

    
