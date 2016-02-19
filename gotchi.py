import uuid

class Gotchi:


    def __init__(self):
        self.uuid = uuid.uuid1()
        self.name = ""
        self.age = 0
        self.health = 100
        self.happiness = 100
        print self.uuid

    def update_health(self, health):
        self.health += health

    def update_happiness(self,happiness):
        pass
    def update_age(self, age):
        pass
    def set_name(self,name):
        pass


