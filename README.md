## 开发日志
#### 6.30
- 完成了基本的utils.py，基类包括Character（角色），Enemy(敌人), Team(队伍), weapon(武器)，debuff(负面效果),buff(正面效果)，damage(伤害)
- 编写了Firefly的类、武器“梦应归于何处”的类和负面效果“溃败”的类

TODO：
- 思考一下伤害应该怎么分类
- 思考一下debuff什么时候挂上、什么时候消失、检验逻辑放在debuff内部还是放在挂debuff的对象（武器、角色）的逻辑里面
- 补全流萤的类，武器的类和负面效果的类
- 思考一下要不要把角色、武器、负面效果等写成自己独有的文件
#### 7.6
- 把各种类拆开，基本逻辑：所有debuff的判断、伤害类型的判断，削韧的判断全部由角色进行，debuff负责把自己挂在对方身上；伤害类只负责计算伤害
- 实现了四种基本的伤害类型

## Document
### 伤害类
#### class Direct_Damage:
init params: 
- attacker:执行攻击者
- target：被攻击者
- base_damage:面板x倍率计算的基础伤害
method：
- cause_damage(no param):对target造成伤害，返回字典{'direct':伤害值}