import yaml, os
from time import sleep

class Item():
    def __init__(self):
        self.name = None
        self.id = None
        self.type_id = None
        self.bonus = None
        self.effects = None
    
    def create(self, name, id, type_id, bonus = None, effects = None):
        self.name = name
        self.id = id
        self.type_id = type_id
        self.bonus = bonus
        self.effects = effects
    
    def load(self, type_id, id):
        self.type_id = type_id
        self.id = id

        self.item_data = yaml.safe_load(open(f"./database/Item/{self.type_id}/{self.id}.yml"))

        self.name = self.item_data.get("name")
        self.bonus = self.item_data.get("bonus")
        self.effects = self.item_data.get("effects")

    def get_id(self):
        return self.id
    
    def get_type_id(self):
        return self.type_id
    
    def get_bonus(self):
        return self.bonus
    
    def get_effects(self):
        return self.effects

    def save(self):
        data = {
            'name': self.name,
            'id': self.id,
            'type_id': self.type_id,
            'bonus': self.bonus,
            'effects': self.effects
        }
        if not os.path.exists(f"./database/Items/{self.type_id}"):
            os.mkdir(f"./database/Items/{self.type_id}")
        sleep(1)
        with open (f"./database/Items/{self.type_id}/{self.id}.yml", "w") as f:
            yaml.dump(data, f)
        print(f"item data of {self.name} saved")