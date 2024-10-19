class Person:

    def __init__(self, age,gender,):
        self.age = age
        self.gender = gender
        self.hobby = "Gaming"

    def change_hobby(self, new_hobby):
        self.hobby = new_hobby
        print(f"francis age is {self.age} and {self.age} his new hobby is {self.hobby}")


francis = Person(20, "Male")
print(francis.hobby)
francis.change_hobby("singing")





class Character:
    def __init__(self, name , age, title):
        self.name = name
        self.age = age
        self.title = title
        self.level = 1
        self.health = 100
        self.skills = ["Slash", "Aggro"]
        self.experience = 0

    def introduce(self):
        print(f"My name is {self.name} Im a {self.title} with level {self.level}")

    def newSkill(self, new_skill):
        self.skills.append(new_skill)
        print(f"new skill Obtained - {new_skill}")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage! Health is now {self.health}")
        
    def gain_experience(self, exp):
        self.experience += exp
        print(f"{self.name} gained {exp} experience points!")
        while self.experience >= 100:
            self.experience -= 100
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health = 100
        print(f"{self.name} leveled up! Now at level {self.level} with full health.")


tigreal = Character("tigreal", 45, "Warrior")

tigreal.introduce()

tigreal.newSkill("Bash")
tigreal.introduce()

tigreal.take_damage(20)
tigreal.take_damage(70)

tigreal.gain_experience(20)
tigreal.gain_experience(200)


class Hero:
    def __init__(self, name, role, damage_type, basic_attack_type, passive_ability):
        self.name = name
        self.role = role
        self.level = 1
        self.damage_type = damage_type
        self.basic_attack_type = basic_attack_type
        self.passive_ability = passive_ability
        self.skill = ["Moon Arrow", "Arrow of Eclipse", "Hidden Moonlight"]
        self.skill_level = 1
        self.experience = 0
        self.health = 100 
        self.mana = 500
        self.physical_defense = 17
        self.magical_defense = 15
        self.skill_points = 0

    def hero_wiki(self):
        print(f"{self.name} is a {self.role} with {self.damage_type} damage and a {self.basic_attack_type} attack.")
        print(f"Passive Skill: {self.passive_ability}")
    
    def activate_passive(self):
        print(f"{self.name} activates their passive ability: {self.passive_ability}!")

    def taking_damage(self, damage):
        # Mitigate damage based on physical defense
        mitigated_damage = max(damage - self.physical_defense, 0)  # Damage reduced by defense, but not below 0
        self.health -= mitigated_damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {mitigated_damage} damage! Health is now {self.health}")

    def gain_experience(self, exp):
        self.experience += exp
        print(f"{self.name} gains {exp} experience points!")
        while self.experience >= 200:  # Increased threshold for leveling up
            self.experience -= 200
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health = 100  # Reset health on level up
        print(f"{self.name} leveled up! Now at level {self.level} with full health.")

    def skill_level_up(self, points):
        self.skill_points += points
        print(f"You gain {points} skill points...")
        while self.skill_points >= 1:
            self.skill_points -= 1
            # Placeholder for skill selection logic
            print(f"{self.name}'s skill leveled up! Remaining skill points: {self.skill_points}")

# Create and interact with the hero
miya = Hero("Miya", "Marksman", "Physical", "Ranged", "Moon Blessing")
miya.hero_wiki()
miya.activate_passive()
miya.taking_damage(90)
miya.gain_experience(80)
miya.gain_experience(20)





class Car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    def car_info(self):
        print(f"This {self.brand} is brand new with color {self.color} model {self.model}")


Tesla = Car("Tesla", "Blue", "cybertruck")
Tesla.car_info()


class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance


    def depost(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print(f"Insufficient funds for {self.owner}. Balance remains: ${self.balance}")



BDO = BankAccount("Francis")
BDO.depost(200)
BDO.withdraw(20)


class Book:
    def __init__(self, title, total_pages):
        self.title = title
        self.total_pages = total_pages
        self.pages_read = 0


    def read_pages(self, pages):
        self.pages_read += pages
        if self.pages_read > self.total_pages:
            self.pages_read = self.total_pages
        print(f"You have read {self.pages_read} out of {self.total_pages} pages of '{self.title}'.")    



my_book = Book("python", 300)
my_book.read_pages(30)


class Player:

    def __init__(self, name):
        self.name = name 
        self.health = 100
        self.coins = 0


    def take_damge(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} is dead!")
        else:
            print(f"{self.name} took {damage} damage! Health is now {self.health}")

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
        print(f"{self.name} healed for {amount} points! Health is now {self.health}")   

player1 = Player("test")

player1.take_damge(90)
player1.heal(100)




class Inventory:
    def __init__(self, owner):
        self.owner = owner
        self.items = []


    def add_items(self, item):
        self.items.append(item)
        print(f"{self.owner} add {item} successfully...")


    def remove_items(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{self.owner} removed {item} from the inventory.")
        else:
            print(f"{item} is not in the inventory.")

    def view_inventory(self):
        if self.items:
             print(f"{self.owner}'s Inventory: {', '.join(self.items)}")
        else:
            print(f"{self.owner}'s inventory is empty.")


player1 = Inventory("test")
player1.add_items("sword")     

player1.remove_items("test")



player2_inventory = Inventory("Luna")

player2_inventory.add_items("Magic Staff")
player2_inventory.view_inventory()  # Output: Luna's Inventory: Magic Staff





# Class Inheritance 


class Hero:  # Parent Class (Super Class)
    def __init__(self, name, role, health):
        self.name = name 
        self.role = role
        self.health = health
        

    def hero_info(self):
        print(f"{self.name} is a {self.role} with {self.health} health.")

class  Warrior(Hero):   # Child Class (Sub Class)
    def __init__(self, name):
        super().__init__(name, "warrior", 500)
        self.armor = 150
        self.mana = 200

            

class Mage(Hero):
    def __init__(self, name,):
        super().__init__(name, "Mage", 250)
        self.armor = 50
        self.mana = 500

    def cast_spell(self, spell_name, cost):
        if self.mana >= cost:
            self.mana -= cost
            print(f"{self.name} cast {spell_name}! Mana is now {self.mana}")
        else:
            print(f"Not enough mana to cast {spell_name}!")



chou = Warrior("Chou")


lunox = Mage("Lunox")
lunox.cast_spell("fireball", 200)