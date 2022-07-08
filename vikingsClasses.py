
# Soldier


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    


# Viking


class Viking(Soldier):
    def __init__(self,name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        while self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"


 #Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        while self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# War

import random
class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        v = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)
        dam_sa = s.receiveDamage(v.attack()) 
        if s.health <= 0:
            self.saxonArmy.remove(s)
        return dam_sa

    def saxonAttack(self):
        v2 = random.choice(self.vikingArmy)
        s2 = random.choice(self.saxonArmy)
        dam_vi = v2.receiveDamage(s2.attack()) 
        if v2.health <= 0:
            self.vikingArmy.remove(v2)
        return dam_vi

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."