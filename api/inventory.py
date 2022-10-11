import yaml

class Inventory():
    def __init__(self):
        self.inventory = {}
    
    def add_item(self, item):
        self.inventory[item.get_id()] = item
        