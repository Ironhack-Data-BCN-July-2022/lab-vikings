
# Soldier


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
    pass
