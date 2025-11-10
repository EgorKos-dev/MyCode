class Monster(object):
    def __init__(self, name, health, speech):
        self.name = name
        self.health = int(health)
        self.speech = speech

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_speech(self):
        return self.speech

    def set_health(self, health):
        self.health = int(health)

    def take_damage(self, damage):
        self.health -= int(damage)
        if self.health < 0:
            self.health = 0

class Friend(Monster):
    
    def __init__(self, name, health, speech, highfive_dialogue, gift): 
        super().__init__(name, health, speech)
        
        self.highfive_dialogue = highfive_dialogue 
        self.gift = gift
    
    def highfive(self):
        print(self.name + " raises their hand and says…")
        print(self.highfive_dialogue)
        print(self.name + "gives you " + self.gift)