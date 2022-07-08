
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage



# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.health = health
        self.strength = strength
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"
   

# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War


class War:
    import random
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)


    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)


    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        saxon.health -= viking.strength
        if saxon.health > 0:
            return f"A Saxon has received {viking.strength} points of damage"
        else:
            self.saxonArmy.remove(saxon)
            return f"A Saxon has died in combat"

    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        viking.health -= saxon.strength
        if viking.health >0:
            return f"{viking.name} has received {saxon.strength} points of damage"
        else:
            self.vikingArmy.remove(viking)
            return f"{viking.name} has died in act of combat"

    def showStatus(self):
        if not self.vikingArmy:
            return"Saxons have fought for their lives and survive another day..."
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        if len(self.saxonArmy) == 1 and len(self.vikingArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle."


         


    

