class Characters():
    def __init__(self):
        self.characters = []
    
    def add_character(self, character):
        self.characters.append(character)

    def get_characters_by_names(self):
        t = []
        for i in self.characters:
            t.append(i.name)
        return t