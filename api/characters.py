class Characters():
    def __init__(self):
        self.characters = []
    
    def add_character(self, character):
        self.characters.append(character)

    def get_characters_by_names(self):
        """Return a list of the names of the characters"""
        t = []
        for i in self.characters:
            t.append(i.name)
        return t
    
    def get_characters_by_ids(self):
        """Return a list of the ids of the characters"""
        t = []
        for i in self.characters:
            t.append(i.id)
        return t