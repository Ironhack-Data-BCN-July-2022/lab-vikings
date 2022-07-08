import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        pass

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health-damage
        return

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health-damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health-damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        combatant = random.choice(self.saxonArmy)
        temp = combatant.receiveDamage(random.choice(self.vikingArmy).strength)
        if combatant.health < 1: # if saxon died, remove from army
            self.saxonArmy.remove(combatant)
        return temp

    def saxonAttack(self):
        combatant = random.choice(self.vikingArmy)
        temp = combatant.receiveDamage(random.choice(self.saxonArmy).strength)
        if combatant.health < 1: # if viking died, remove from army
            self.vikingArmy.remove(combatant)
        return temp

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
