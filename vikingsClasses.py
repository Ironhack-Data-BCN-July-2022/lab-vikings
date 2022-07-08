
# Soldier

import random as rd

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack (self):
        return self.strength
    def receiveDamage (self,damage):
        self.damage = damage
        self.health -= self.damage
    
    pass

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"
    pass

# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
       self.health -= damage
       if self.health > 0:
           return f"A Saxon has received {damage} points of damage"

       else:
           return f"A Saxon has died in combat"

    pass

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, vik):
        if isinstance(vik,Viking):
            self.vikingArmy.append(vik)

    def addSaxon(self, sax):
        if isinstance(sax,Saxon):
            self.saxonArmy.append(sax)

    def vikingAttack(self):
        v = rd.choice(self.vikingArmy)
        s = rd.choice(self.saxonArmy)

        dam = s.receiveDamage(v.attack())

        if s.health <=0:
            self.saxonArmy.remove(s)

        return dam
    
    def saxonAttack(self):
        u = rd.choice(self.vikingArmy)
        i = rd.choice(self.saxonArmy)

        damr = u.receiveDamage(i.attack())

        if u.health <=0:
            self.vikingArmy.remove(u)
        return damr   

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
            
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
