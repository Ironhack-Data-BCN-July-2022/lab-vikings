
# Soldier


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack (self):
        return self.strength

    def receiveDamage (self, damage):
        self.damage = damage
        self.health -= self.damage


# Viking


class Viking(Soldier):
    def __init__ (self, name, health, strength):
#inherit values from Soldier
        Soldier.__init__(self, health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.name + " has received " +  str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"
    pass

# Saxon

class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received " +  str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"

# War

import random as randint

class War:
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, vik):
        self.vikingArmy.append(vik)

    def addSaxon(self, sax):
        self.saxonArmy.append(sax)

    def vikingAttack(self):
        self.vikingArmy[randint(len(self.saxonArmy))]
        self.Saxon.receiveDamage(Viking.strength)
        return self.Saxon.health

    def saxonAttack(self):
        self.saxonArmy[randint(len(self.vikingArmy))]
        self.Viking.receiveDamage(self.Saxon.strength)
        return self.Viking.health


    def showStatus(self):
        if len(self.saxonArmy) <= 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) <= 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy) == 1 and len(self.saxonArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle."
