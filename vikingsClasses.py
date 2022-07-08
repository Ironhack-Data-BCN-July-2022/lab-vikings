import random as rd

class Soldier ():
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health-=damage 

# Viking
class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name
           
    def attack(self):
        return self.strength 

    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon
class Saxon (Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
            
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
# War
class War ():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking):
        if isinstance(viking,Viking):
            self.vikingArmy.append(viking)
        
    def addSaxon(self, saxon):
        if isinstance(saxon, Saxon):
            self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        v = rd.choice(self.vikingArmy)
        s = rd.choice(self.saxonArmy)
        
        s_damage=s.receiveDamage(v.strength)
        if s.health <= 0:
            self.saxonArmy.remove(s)
        return s_damage
        
    def saxonAttack(self):
        x = rd.choice(self.vikingArmy)
        y = rd.choice(self.saxonArmy)
        
        v_damage=x.receiveDamage(y.strength)
        if x.health <= 0:
            self.vikingArmy.remove(x)
        return v_damage
        
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


        