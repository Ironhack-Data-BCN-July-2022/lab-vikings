
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength
        
    def attack(self):
        return self.strength

#remove the received damage from the health property
    def receiveDamage(self, damage):
        self.health = self.health - damage
        
# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            return (f"{self.name} has died in act of combat")
        else:
            return (f"{self.name} has received {damage} points of damage")
        
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
     def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
        
     def receiveDamage(self, damage):
        self.health = self.health - (damage)
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return (f"A Saxon has received {damage} points of damage")

# War

class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        a_saxon = random.choice(self.saxonArmy)
        a_viking = random.choice(self.vikingArmy)
        result = a_saxon.receiveDamage(a_viking.strength)
        if a_saxon.health <= 0:
            self.saxonArmy.remove(a_saxon)
        return result
    
    def saxonAttack(self):
        
        a_saxon = random.choice(self.saxonArmy)
        a_viking = random.choice(self.vikingArmy)
        res = a_viking.receiveDamage(a_saxon.strength)
        if a_viking.health <= 0:
            self.vikingArmy.remove(a_viking)
        return res

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
