class Character:
    name = ""
    attack = 0
    defense = 0
    maxHitPoints = 0
    abilities = None
    currentHitPoints = 0

    def __init__(self, name, attack, maxHitPoints, defense, abilities):
        self.name = name
        self.attack = attack
        self.maxHitPoints = maxHitPoints
        self.defense = defense
        self.abilities = abilities
        self.currentHitPoints = self.maxHitPoints
        
    def takeDamage(self, damage):
        print(self.name + " takes " + str(damage) + " damages.")
        self.changeHitPoints(-(damage - self.defense))

    def changeHitPoints(self, hitPointsChange):
        self.currentHitPoints += hitPointsChange
        if (hitPointsChange < 0): 
            print(self.name + " loses " + str(-hitPointsChange) + " hitpoints!")
        else:
            print(self.name + " has been healed by " + str(hitPointsChange) + " hitpoints!")

        if (self.isDead()):
            self.currentHitPoints = 0
            print(self.name + " is dead!!!")
        else:
            if (self.currentHitPoints > self.maxHitPoints):
                self.currentHitPoints = self.maxHitPoints

            print(self.name + " is now at " + self.currentHitPointsAndMaxHitPointsString())

    def isDead(self):
        return (self.currentHitPoints <= 0)

    def currentHitPointsAndMaxHitPointsString(self):
        return str(self.currentHitPoints) + "/" + str(self.maxHitPoints)

    def displayInfo(self):
        print(self.name)
        print("Attack: " + str(self.attack))
        print("Defense: " + str(self.defense))
        print("Hitpoints: " + self.currentHitPointsAndMaxHitPointsString())
        if (self.abilities):
            print(', '.join(self.abilities))
        else:
            print("No ability learnt")

print()

warrior = Character(name = "Warrior", attack = 10, maxHitPoints = 100, defense = 10, abilities = [])
print(warrior.displayInfo())
print()

wizard = Character(name = "Wizard", attack = 6, maxHitPoints = 60, defense = 6, abilities = ["Fireball", "Thunder"])
print(wizard.displayInfo())
print()

warrior.takeDamage(70)
print()

wizard.takeDamage(70)
print()
