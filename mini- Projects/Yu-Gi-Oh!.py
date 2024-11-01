import random

class Card:
    def __init__(self, name, attack_points, defense_points, card_type):
        self.name = name
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.card_type = card_type  # e.g., "Monster", "Spell"
        
    def __str__(self):
        return f"{self.name} | ATK: {self.attack_points} | DEF: {self.defense_points} | Type: {self.card_type}"


class Player:
    def __init__(self, name, life_points=4000):
        self.name = name
        self.life_points = life_points
        self.hand = []
        self.field = []

    def draw_card(self, deck):
        if deck:
            card = deck.pop()
            self.hand.append(card)
            print(f"{self.name} drew a card: {card.name}")
        else:
            print("Deck is empty! Cannot draw any more cards.")
    
    def summon_monster(self, monster_card):
        if monster_card.card_type == "Monster" and monster_card in self.hand:
            self.field.append(monster_card)
            self.hand.remove(monster_card)
            print(f"{self.name} summoned {monster_card.name} to the field!")
        else:
            print(f"{self.name} cannot summon {monster_card.name}. It's either not a monster or not in hand.")

    def attack(self, opponent, attacker, defender):
        if attacker in self.field and defender in opponent.field:
            if attacker.attack_points > defender.defense_points:
                damage = attacker.attack_points - defender.defense_points
                opponent.life_points -= damage
                opponent.field.remove(defender)
                print(f"{self.name}'s {attacker.name} destroyed {opponent.name}'s {defender.name} and dealt {damage} damage!")
            else:
                print(f"{self.name}'s {attacker.name} couldn't defeat {opponent.name}'s {defender.name}.")
        else:
            print("Invalid attack. One or both monsters are not on the field.")


# Sample deck creation
def create_deck():
    return [
        Card("Blue-Eyes White Dragon", 3000, 2500, "Monster"),
        Card("Dark Magician", 2500, 2100, "Monster"),
        Card("Mystical Elf", 800, 2000, "Monster"),
        Card("Raigeki", 0, 0, "Spell"),
    ]

# Example gameplay
deck = create_deck()
player1 = Player("Yugi")
player2 = Player("Kaiba")

# Draw starting hand
for _ in range(3):
    player1.draw_card(deck)
    player2.draw_card(deck)

# Summon and attack example
if player1.hand:
    player1.summon_monster(player1.hand[0])  # Yugi attempts to summon the first card in hand

if player2.hand:
    player2.summon_monster(player2.hand[0])  # Kaiba attempts to summon the first card in hand

# Check if both players have monsters on the field before attacking
if player1.field and player2.field:
    player1.attack(player2, player1.field[0], player2.field[0])  # Yugi attacks Kaiba's monster
else:
    print("One or both players have no monsters on the field. Attack cannot be performed.")
