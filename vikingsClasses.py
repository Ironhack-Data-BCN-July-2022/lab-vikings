
# Soldier


class Soldier:
    def __init__(self,health,strength):
        #Attributes
        self.health=health
        self.strength=strength

    #Methods
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health=self.health - damage
        pass


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name

    #Methods
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health=self.health - damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

    pass

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    #Methods
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health=self.health - damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

    pass

# War

import random
class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking= random.choice(self.vikingArmy)

        random_saxon.receiveDamage(random_viking.attack())
        
        if random_saxon.health<=0:
            self.saxonArmy.remove(random_saxon) 
        
        return random_saxon.receiveDamage(random_viking.attack())
    
    def saxonAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking= random.choice(self.vikingArmy)

        random_viking.receiveDamage(random_saxon.attack())

        if random_viking.health<=0:
            self.vikingArmy.remove(random_viking) 
        
        return random_viking.receiveDamage(random_saxon.attack())
        
    def showStatus(self):
        if len(self.saxonArmy)<=0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy)<=0:
            return "Saxons have fought for their lives and survived another day..."
        if len(self.saxonArmy) >0 and len(self.vikingArmy) >0:
            return "Vikings and Saxons are still in the thick of battle."
