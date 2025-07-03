from character import Character
class Team:
    def __init__(self, characters: list[Character]):
        self.characters = characters
    def get_number_of_characters(self):
        return len(self.characters)