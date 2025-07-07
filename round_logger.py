import logging
class round_logger:
    def __init__(self, **kwargs):
        for key in kwargs:
            self.__dict__[key] = kwargs[key]
        self.logger = logging.getLogger(__name__)
    def after_round_log(self):
        info = {}
        if hasattr(self, 'damage'):
            info['damage'] = self.damage
        if hasattr(self, 'toughness_delta'):
            info['toughness_delta'] = self.toughness_delta
        if hasattr(self, 'energy_delta'):
            info['energy_delta'] = self.energy_delta
        if hasattr(self,'mover'):
            info['mover']=self.mover
        if hasattr(self, 'skill_points_delta'):
            info['skill_points_delta'] = self.skill_points_delta
        self.logger.info(info)
    