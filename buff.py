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