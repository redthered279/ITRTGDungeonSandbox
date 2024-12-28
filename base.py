from random import randint
#from copy import deepcopy
from math import floor

class Equip:
    def __init__(self, element, tier, grade, upgrade, enchant):
        self.element = element
        # "water", "fire", "earth", "wind", "neutral"
        self.grade = grade
        # F = 0, D = 1 ... SSS = 8
        self.upgrade = upgrade
        self.tier = tier
        self.enchant = enchant
        
        # Temporary variables
        self.hp = 0
        self.attack = 0
        self.defense = 0
        self.speed = 0
        self.fire = 0
        self.water = 0
        self.earth = 0
        self.wind = 0
        
class SpecialEquip:
    def __init__(self):
        pass

class Entity:
    def __init__(self):
        self.id = None
        self.name = None
        self.growth = None
        self.element = None
        # "water", "fire", "earth", "wind", "neutral"
        self.dungeon_level = None
        self.evo_class = None
        # "blacksmith", "alchemist", "assassin", "adventurer"
        # "mage", "defender", "supporter", "rogue"
        self.class_level = None
        
        # temporary, will be replaced later
        self.growth_req = None
        self.speciality = None
        self.spec_bonus = None
        
        self.weapon = None
        self.armor = None
        self.acc = None
        
        self.fire = 0
        self.water = 0
        self.earth = 0
        self.wind = 0
        
        self.hp = None
        self.attack = None
        self.defense = None
        self.speed = None
        
        self.is_alive = True
    
    def calculate_stats(self):
        self.spec_bonus = 0.5 + (self.growth_req / 10000)
        if self.evo_class == "mage":
            hp_class_mod = 0.4
            attack_class_mod = 1.5
            defense_class_mod = 0.4
            speed_class_mod = 1.2
        elif self.evo_class == "assassin":
            hp_class_mod = 0.7
            attack_class_mod = 1.3
            defense_class_mod = 0.7
            speed_class_mod = 1.4
        elif self.evo_class == "rogue":
            hp_class_mod = 0.8
            attack_class_mod = 1.2
            defense_class_mod = 0.6
            speed_class_mod = 1.6
        elif self.evo_class == "supporter":
            hp_class_mod = 0.8
            attack_class_mod = 0.7
            defense_class_mod = 1
            speed_class_mod = 1.3
        elif self.evo_class == "defender":
            hp_class_mod = 1.2
            attack_class_mod = 0.4
            defense_class_mod = 1.5
            speed_class_mod - 0.4
        elif self.evo_class == "alchemist":
            hp_class_mod = 0.8
            attack_class_mod = 1
            defense_class_mod = 0.8
            speed_class_mod = 1.1
        elif self.evo_class == "blacksmith":
            hp_class_mod = 1.2
            attack_class_mod = 1.1
            defense_class_mod = 1.2
            speed_class_mod = 0.4
        else:
            hp_class_mod = 1
            attack_class_mod = 1
            defense_class_mod = 1
            speed_class_mod = 1
            
        hp_equip_mod = 100
        attack_equip_mod = 100
        defense_equip_mod = 100
        speed_equip_mod = 100
        
        if self.weapon != None:
            hp_equip_mod += self.weapon.hp * (0.5 + 0.1 * self.weapon.grade) * (1 + self.weapon.upgrade * 0.05)
            attack_equip_mod += self.weapon.attack * (0.5 + 0.1 * self.weapon.grade) * (1 + self.weapon.upgrade * 0.05)
            defense_equip_mod += self.weapon.defense * (0.5 + 0.1 * self.weapon.grade) * (1 + self.weapon.upgrade * 0.05)
            speed_equip_mod += self.weapon.speed * (0.5 + 0.1 * self.weapon.grade) * (1 + self.weapon.upgrade * 0.05)
        
        if self.armor != None:
            hp_equip_mod += self.armor.hp * (0.5 + 0.1 * self.armor.grade) * (1 + self.armor.upgrade * 0.05)
            attack_equip_mod += self.armor.attack * (0.5 + 0.1 * self.armor.grade) * (1 + self.armor.upgrade * 0.05)
            defense_equip_mod += self.armor.defense * (0.5 + 0.1 * self.armor.grade) * (1 + self.armor.upgrade * 0.05)
            speed_equip_mod += self.armor.speed * (0.5 + 0.1 * self.armor.grade) * (1 + self.armor.upgrade * 0.05)
            
        if self.acc != None:
            hp_equip_mod += self.acc.hp * (0.5 + 0.1 * self.acc.grade) * (1 + self.acc.upgrade * 0.05) / 100
            attack_equip_mod += self.acc.attack * (0.5 + 0.1 * self.acc.grade) * (1 + self.acc.upgrade * 0.05)
            defense_equip_mod += self.acc.defense * (0.5 + 0.1 * self.acc.grade) * (1 + self.acc.upgrade * 0.05)
            speed_equip_mod += self.acc.speed * (0.5 + 0.1 * self.acc.grade) * (1 + self.acc.upgrade * 0.05)
        
        self.hp = (10 + 24 * self.dungeon_level) * (1 + self.growth/200000) * hp_equip_mod * hp_class_mod / 100
        self.attack = (1 + 2.4 * self.dungeon_level) * (1 + self.growth/200000) * attack_equip_mod * attack_class_mod / 100
        self.defense = (1 + 2.4 * self.dungeon_level) * (1 + self.growth/200000) * defense_equip_mod * defense_class_mod / 100
        self.speed = (1 + 2.4 * self.dungeon_level) * (1 + self.growth/200000) * speed_equip_mod * speed_class_mod / 100
        
        if self.element == "neutral":
            self.fire = 0.75 * self.dungeon_level
            self.water = 0.75 * self.dungeon_level
            self.wind = 0.75 * self.dungeon_level
            self.earth = 0.75 * self.dungeon_level
        elif self.element == "fire":
            self.fire = 50 + 3 * self.dungeon_level
            self.water = -50
        elif self.element == "water":
            self.water = 50 + 3 * self.dungeon_level
            self.earth = -50
        elif self.element == "wind":
            self.wind = 50 + 3 * self.dungeon_level
            self.fire = -50
        elif self.element == "earth":
            self.earth = 50 + 3 * self.dungeon_level
            self.wind = -50
        
        if self.weapon != None:
            self.fire += self.weapon.fire * (0.5 + 0.1 * self.weapon.grade) * (1 + self.weapon.upgrade * 0.05) * (1 - 0.5 * self.weapon.enchant)
            self.water += self.weapon.water * (0.5 + 0.1 * self.weapon.grade) * (1 + self.weapon.upgrade * 0.05) * (1 - 0.5 * self.weapon.enchant)
            self.wind += self.weapon.wind * (0.5 + 0.1 * self.weapon.grade) * (1 + self.weapon.upgrade * 0.05) * (1 - 0.5 * self.weapon.enchant)
            self.earth += self.weapon.earth * (0.5 + 0.1 * self.weapon.grade) * (1 + self.weapon.upgrade * 0.05) * (1 - 0.5 * self.weapon.enchant)
            
        if self.armor != None:
            self.fire += self.armor.fire * (0.5 + 0.1 * self.armor.grade) * (1 + self.armor.upgrade * 0.05) * (1 - 0.5 * self.armor.enchant)
            self.water += self.armor.water * (0.5 + 0.1 * self.armor.grade) * (1 + self.armor.upgrade * 0.05) * (1 - 0.5 * self.armor.enchant)
            self.wind += self.armor.wind * (0.5 + 0.1 * self.armor.grade) * (1 + self.armor.upgrade * 0.05) * (1 - 0.5 * self.armor.enchant)
            self.earth += self.armor.earth * (0.5 + 0.1 * self.armor.grade) * (1 + self.armor.upgrade * 0.05) * (1 - 0.5 * self.armor.enchant)
            
        if self.acc != None:
            self.fire += self.acc.fire * (0.5 + 0.1 * self.acc.grade) * (1 + self.acc.upgrade * 0.05) * (1 - 0.5 * self.acc.enchant)
            self.water += self.acc.water * (0.5 + 0.1 * self.acc.grade) * (1 + self.acc.upgrade * 0.05) * (1 - 0.5 * self.acc.enchant)
            self.wind += self.acc.wind * (0.5 + 0.1 * self.acc.grade) * (1 + self.acc.upgrade * 0.05) * (1 - 0.5 * self.acc.enchant)
            self.earth += self.acc.earth * (0.5 + 0.1 * self.acc.grade) * (1 + self.acc.upgrade * 0.05) * (1 - 0.5 * self.acc.enchant)
    
    def hit(self, enemies):            
        result = f"{self.name} attacked: \n"
        hits = 3 + floor(self.class_level/20) if self.evo_class == "mage" else 1
        
        while (hits > 0):
            hits -= 1
            enemy = enemies[randint(0, len(enemies) - 1)]
            attacker = self.fire
            target = enemy.fire
            # negative value of "target" will be set to 0
            # and the value will be added to "attacker" as a positive
            # same is applied to the enemy elements
            attacker = attacker - target if target < 0 else attacker
            target = 0 if target < 0 else target
            fire_mod = (1 + attacker/100)/(1 + target/100)
        
            attacker = self.water
            target = enemy.water
            attacker = attacker - target if target < 0 else attacker
            target = 0 if target < 0 else target
            water_mod = (1 + attacker/100)/(1 + target/100)
        
            attacker = self.wind
            target = enemy.wind
            attacker = attacker - target if target < 0 else attacker
            target = 0 if target < 0 else target
            wind_mod = (1 + attacker/100)/(1 + target/100)
        
            attacker = self.earth
            target = enemy.earth
            attacker = attacker - target if target < 0 else attacker
            target = 0 if target < 0 else target
            earth_mod = (1 + attacker/100)/(1 + target/100)
            
            if self.element == "neutral":
                element_mod = max(fire_mod, water_mod, earth_mod, wind_mod)
            elif self.element == "water":
                element_mod = water_mod
            elif self.element == "wind":
                element_mod = wind_mod
            elif self.element == "fire":
                element_mod = fire_mod
            elif self.element == "earth":
                element_mod = earth_mod
            
            target_def_multi = 1 - enemy.defense/(enemy.defense + 200)
            
            speed_damage = (self.speed - enemy.speed)/2
            if self.evo_class == "mage":
                speed_damage /= 3
            
            speed_damage = 0 if speed_damage < 0 else speed_damage
            
            damage = (self.attack - enemy.defense/2) * element_mod * target_def_multi
            
            if self.evo_class == "mage":
                bonus = 1 + self.spec_bonus if self.speciality == "mage" else 1
                damage *= (35 + bonus * self.class_level)/100
                
            elif self.evo_class == "assassin":
                damage *= (1+ self.class_level * 5/100)
            
            damage = 1 if damage < 1 else damage
            final_damage = damage + speed_damage
            
            enemy.hp -= final_damage
            
            enemy_status_message = f"\n{enemy.name} has {round(enemy.hp)} HP left"
            
            if enemy.hp < 0:
                enemy.is_alive = False
                death_message = f"\n{enemy.name} died!"
            result += f"{enemy.name} for {round(damage)} + {round(speed_damage)} speeding damage!" + enemy_status_message
            
        return result
    
    def heal(self, allies):
        pass

player = Entity()
enemy = Entity()

player.name = "Mouse"
player.growth = 2848
player.element = "earth"
player.evo_class = "supporter"
player.dungeon_level = 52
player.class_level = 12
player.growth_req = 100
player.speciality = None

weapon = Equip("fire", 2, 6, 10, 0)
weapon.attack = 30
weapon.defense = -10
weapon.fire = 20
weapon.water = -30

armor = Equip("water", 2, 6, 10, 0)
armor.hp = 20
armor.defense = 10
armor.water = 40
armor.earth = -40

acc = Equip("fire", 2, 6, 10, 0)
acc.hp = -7
acc.attack = 21
acc.defense = -7
acc.speed = 7
acc.fire = 50
acc.water = -50

player.weapon = weapon
player.armor = armor
player.acc = acc

player.calculate_stats()

enemy.name = "Test dummy 1"
enemy.element = "water"

enemy.hp = 3000
enemy.attack = 300
enemy.defense = 200
enemy.speed = 180

enemy.fire = 60
enemy.water = 600
enemy.earth = -40
enemy.wind = 60

result = enemy.hit((player,))
print(result)

"""
knives formula
(tier/3)(grade/9)((1+upgrade)/21)
t4 has the same value as t3 btw

"""