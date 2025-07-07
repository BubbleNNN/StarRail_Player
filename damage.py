import random
class Direct_Damage:
    def __init__(self, attacker, target, base_damage):
        self.attacker = attacker
        self.target = target
        self.base_damage = base_damage
    
    def cause_damage(self):
        '''
        直伤公式：
        基础伤害 = 面板属性*倍率
        防御乘区 = (攻击者等级*10+200)/(目标防御+攻击者等级*10+200)
        破盾乘区 = 0.9 if not break else 1
        抗性乘区 = 1(有弱点)or 0.8(无弱点) - 敌人抗性 + 角色无视抗性（尚未碰到，没有对应的类）.穿透、减抗都属于这个乘区
        暴击乘区 = 1+ 暴击伤害
        增伤乘区 = 1+所有增伤效果
        易伤乘区 = 1+所有易伤效果
        相同乘区内部计算系数的时候加减,不同乘区之间计算的时候乘除
        先结算直接伤害,再结算破韧
        '''
        defence_coe = (self.attacker.level * 10+200)/(max(0,self.target.defense) + self.attacker.level * 10+200)#没有负防御
        breakshield_coe = 1 if self.target.in_break else 0.9#破盾乘区，这样命名是为了和破韧乘区区分开
        resist_coe = (1 if self.attacker.attr in self.target.weakness else 0.8) - getattr(self.target, f"{self.attacker.attr}_RES_boost") #这里抗性的计算是逆着计算，也就是直接计算减去抗性之后造成的伤害的系数。抗性的叠加没有上限，也就是可以被减到负抗性
        critical_coe = 1 + (0 if random.random()> self.attacker.critical_chance else self.attacker.critical_damage)
        damage_boost_coe = 1 + getattr(self.attacker,f'{self.attacker.attr}_DMG_boost')
        damage_vunerability_coe = 1 + getattr(self.attacker,f'{self.attacker.attr}_DMG_vunerability')
        direct_damage = self.base_damage * defence_coe * breakshield_coe * resist_coe * critical_coe * damage_boost_coe * damage_vunerability_coe
        self.target.hp -= direct_damage
        return {'direct': direct_damage}
class Break_Damage:
    def __init__(self, attacker, target, base_damage = 1):
        self.attacker = attacker
        self.target = target
        self.base_coe = {'phisical':4, 'fire':4, 'wind':3, 'lightning':2, 'ice':2, 'quantum':1, 'imaginary':1} #破韧倍率,
        self.base_damage = 1 * 1883.8 * self.base_coe[self.attacker.attr] #破韧倍率是1.8838倍的面板属性,这里的面板属性是攻击力
    
    def cause_damage(self):
        '''
        击破瞬间伤害公式：
        基础伤害*防御乘区*抗性乘区*破盾乘区(1) * 易伤乘区*击破乘区*韧性乘区
        基础伤害= 等级固定伤害*属性倍率
        韧性乘区 = (敌人韧性值+20)/40
        击破乘区 = 1+击破特攻
        '''
        defence_coe = (self.attacker.level * 10+200)/(max(0,self.target.defense) + self.attacker.level * 10+200)
        resist_coe = (1 if self.attacker.attr in self.target.weakness else 0.8) - getattr(self.target, f"{self.attacker.attr}_RES_boost")
        damage_vunerability_coe = 1 + getattr(self.attacker,f'{self.attacker.attr}_DMG_vunerability')
        break_coe = 1 + self.attacker.break_effect
        toughness_coe = (self.target.toughness + 20)/40
        break_damage = self.base_damage * defence_coe * resist_coe * damage_vunerability_coe * break_coe * toughness_coe
        self.target.hp -= break_damage
        return {'break': break_damage}
    
class Super_Break_Damage:
    def __init__(self, attacker, target, buff = None, base_damage = 1, toughness_delta = 0):
        self.attacker = attacker
        self.target = target
        self.base_coe = 1.5#超击破统一了不同属性的倍率，都是1.5
        self.base_damage = 1 * 1883.8 * self.base_coe
        self.buff_coe =1 if buff == None else buff #buff乘区，暂时没有实现buff的叠加效果，直接用1表示没有buff
        self.toughness_delta  = toughness_delta #韧性削减值，
    def cause_damage(self):
        '''
        超击破瞬间伤害公式：
        基础伤害*防御乘区*抗性乘区*破盾乘区(1) * 易伤乘区*击破乘区*韧性乘区*buff乘区
        基础伤害= 等级固定伤害*属性倍率
        韧性乘区：削韧数值
        击破乘区 = 1+击破特攻
        buff乘区: 同协主“伴舞”等buff
        '''
        defence_coe = (self.attacker.level * 10+200)/(max(0,self.target.defense) + self.attacker.level * 10+200)
        resist_coe = (1 if self.attacker.attr in self.target.weakness else 0.8) - getattr(self.target, f"{self.attacker.attr}_RES_boost")
        damage_vunerability_coe = 1 + getattr(self.attacker,f'{self.attacker.attr}_DMG_vunerability')
        break_coe = 1 + self.attacker.break_effect
        toughness_coe = self.toughness_delta
        super_break_damage = self.base_damage * defence_coe * resist_coe * damage_vunerability_coe * break_coe * toughness_coe * self.buff_coe
        self.target.hp -= super_break_damage
        return {'super_break': super_break_damage}
class Continuous_Damage:
    def __init__(self, attacker, target, base_damage , level = 1):#持续伤害可以叠层，level表示层数
        self.attacker = attacker
        self.target = target
        self.base_damage = base_damage
        self.level = level
    def cause_damage(self):
        '''
        持续伤害公式：（不吃双爆）
        基础伤害 = 面板属性*倍率
        防御乘区 = (攻击者等级*10+200)/(目标防御+攻击者等级*10+200)
        破盾乘区 = 0.9 if not break else 1
        抗性乘区 = 1(有弱点)or 0.8(无弱点) - 敌人抗性 + 角色无视抗性（尚未碰到，没有对应的类）.穿透、减抗都属于这个乘区
        增伤乘区 = 1+所有增伤效果
        易伤乘区 = 1+所有易伤效果
        相同乘区内部计算系数的时候加减,不同乘区之间计算的时候乘除
        先结算直接伤害,再结算破韧
        '''
        defence_coe = (self.attacker.level * 10+200)/(max(0,self.target.defense) + self.attacker.level * 10+200)#没有负防御
        breakshield_coe = 1 if self.target.in_break else 0.9#破盾乘区，这样命名是为了和破韧乘区区分开
        resist_coe = (1 if self.attacker.attr in self.target.weakness else 0.8) - getattr(self.target, f"{self.attacker.attr}_RES_boost") #这里抗性的计算是逆着计算，也就是直接计算减去抗性之后造成的伤害的系数。抗性的叠加没有上限，也就是可以被减到负抗性
        damage_boost_coe = 1 + getattr(self.attacker,f'{self.attacker.attr}_DMG_boost')
        damage_vunerability_coe = 1 + getattr(self.attacker,f'{self.attacker.attr}_DMG_vunerability')
        continuous_damage = self.base_damage * defence_coe * breakshield_coe * resist_coe* damage_boost_coe * damage_vunerability_coe
        self.target.hp -= continuous_damage
        return {'continuous': continuous_damage}
    
