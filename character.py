from weapon import whereabouts_should_the_dreams_rest
from abc import ABC, abstractmethod
from damage import Direct_Damage
from round_logger import round_logger
class Character(ABC):
    '''
    角色基类
    '''
    def __init__(self, name, attr,level, hp, attack, defense, speed, energy,critical_chance, critical_damage, break_effect, outgoing_healing_boost, max_energy, energy_regeneration_rate, effect_hit_rate, effect_resistance, physical_DMG_boost, fire_DMG_boost, ice_DMG_boost, lightning_DMG_boost, wind_DMG_boost, quantum_DMG_boost, imaginary_DMG_boost, phisical_RES_boost, fire_RES_boost, ice_RES_boost, lightning_RES_boost, wind_RES_boost, quantum_RES_boost, imaginary_RES_boost):
        self.name = name
        self.attr = attr
        self.level = level
        self.hp = hp#当前生命
        self.max_hp = hp#生命上限    
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.energy = energy
        self.critical_chance = critical_chance #暴击率
        self.critical_damage = critical_damage #暴击伤害
        self.break_effect = break_effect #击破特攻
        self.break_efficiency = 1 #击破效率，默认为1
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
            "max_hp":self.max_hp,
            "attr":self.attr,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
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
    @abstractmethod
    def talent_buff(self):
        pass
    @abstractmethod
    def yiqi(self):
        pass
    @abstractmethod
    def talent_effect(self):#天赋效果，每回合检查
        pass
    @abstractmethod
    def talent_buff(self):
        """
        角色天赋加成,一次性加成
        """
        pass
    @abstractmethod
    def normal_attack(self, target):
        """
        普通攻击
        """

    @abstractmethod
    def skill_attack(self, target):
        """
        技能攻击
        """
        pass
    @abstractmethod
    def ult_attack(self, target):
        """
        大招攻击
        """
        pass
    @abstractmethod
    def yiqi_effect(self):#遗器效果，每回合检查
        pass
class Firefly(Character):
    def __init__(self, level):
        super().__init__(
            name = 'Firefly',
            attr = 'fire',
            level = level,
            hp = 815,
            attack = 524,
            defense = 777,
            speed = 104,
            energy = 120,#流萤天赋：进入战斗恢复一半能量
            critical_chance = 0.05,
            critical_damage = 0.5,
            break_effect = 0,
            outgoing_healing_boost = 0,
            max_energy = 240,
            energy_regeneration_rate = 1,
            effect_hit_rate = 0,
            effect_resistance = 0,
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
        self.weapon = whereabouts_should_the_dreams_rest(level = 80,owner = self)
        self.state = 'normal' #是否变身，未变身用'normal' ，变身后用'full_burn'
        self.talent_buff()
        self.yiqi()
        self.talent_effect()
    def talent_buff(self):#固定的天赋增益
        self.speed += 5
        self.break_effect +=  0.373
        self.effect_resistance += 0.18
    def talent_effect(self): #每一轮的天赋二次伤害转换，但是二次转换不能被天赋二次转换，因此需要好好衡量顺序，比如知更鸟的buff什么时候加上去
        if self.attack >=1800:
            self.break_effect += (self.attack-1800)/10 * 0.008
    def yiqi(self):#遗器的基本词条和一些固定的效果
        self.speed += 60
        self.hp += 930
        self.attack += 1390
        self.defense += 151
        self.critical_chance += 0.029
        self.critical_damage += 0.129
        self.break_effect += 1.404
        self.effect_resistance += 0.233
        self.effect_hit_rate += 0.073
    def normal_attack(self, target):
        caused_damage = None
        toughness_delta = 0
        skill_point_delta = 0
        energy_delta = 0
        if self.state == 'normal':
            self.energy += 20 * self.energy_regeneration_rate
            energy_delta = 20 * self.energy_regeneration_rate
            #TODO:战技点+1
            caused_damage = Direct_Damage(attacker= self, target= target,base_damage= self.attack * 1).cause_damage()#默认满级，倍率100%
            target.toughness -= 10* self.break_efficiency
            toughness_delta = -10 * self.break_efficiency
        elif self.state == 'full_burn':
            self.hp += self.hax_hp * 0.2
            caused_damage = Direct_Damage(attacker = self, target=target,base_damage= self.attack * 2).cause_damage()
            target.toughness -= 15* self.break_efficiency
            toughness_delta = -15 * self.break_efficiency
            self.energy += 0 #强化平A不回能
            #TODO：战技点+1
        else:
            return f"invalid_state {self.state}"
        return {'damage':caused_damage, 'toughness_delta' :toughness_delta, 'skill_point_delta':skill_point_delta,'energy_delta':energy_delta}#debug或者logger用
    def skill_attack(self, target):
        pass
    def ult_attack(self, target):
        pass
    def yiqi_effect(self):#每回合需要重新计算是否触发的遗器效果
        pass

firefly = Firefly(level=80)
print(firefly.get_state())

   
    
        
    
