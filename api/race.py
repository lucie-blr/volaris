       
class Race():
    def __init__(self, id):
        self.id = id

        self.race_data = yaml.safe_load(open(f"./database/Races/{id}.yml"))

        self.name = self.race_data["name"]
        self.bonus = self.race_data["bonus"]
        self.competence = self.race_data["competence"]
        self.average_age = self.race_data["average_age"]
        self.average_stats = self.race_data["average_stats"]

    def save(self):
        self.race_data["name"] = self.name
        self.race_data["bonus"] = self.bonus
        self.race_data["competence"] = self.competence
        self.race_data["average_age"] = self.average_age
        self.race_data["average_stats"] = self.average_stats

        with open (f"./database/Races/{self.id}.yml"):
            yaml.dump(self.race_data, f)
            print(f"Race data of {self.name} saved")
        