from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from enemy import Enemy
    
class debuff:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.passing_round = 0
        self.target: Optional[Enemy] = None
    def after_round(self):
        self.passing_round += 1
        if self.duration - self.passing_round <= 0:
            self.target.debuff.remove(self)


class Routed(debuff):
    def __init__(self,target:Optional[Enemy]):
        super().__init__(
            name = 'Routed',
            duration = 2,
            target = target
        )
    def take_effect(self):
        if self not in self.target.get_state()['debuff']:
            self.target.debuff.append(self)
            self.target.beaking_DMG_vunerability *= 0.24
            self.target.speed -= self.target.speed * 0.2

        