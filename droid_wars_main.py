from random import randint
from functools import reduce

class Base_droid:
	def __init__(self, name, strength, defense, AI):
		self.name = name
		self.strength = strength
		self.defense = defense
		self.AI = AI
		self.durability = self.defense * 4
		self.maneuvering = self.AI * 2
		self.damage = self.strength * 2

	def show_status(self):
		print("Droid Type: ", self.name)
		print("Strength: ", self.strength)
		print("Defense: ", self.defense)
		print("AI: ", self.AI)
		print("Durability: ", self.durability)
		print("Maneuvering: ", self.maneuvering)
		print("Damage: ", self.damage)

	def check_operativity(self):
		return self.durability > 0

	def droid_destroyed(self):
		self.durability = 0
		print(self.name, "was destroyed.")

	def restore_durability(self):
		self.durability = self.defense * 4

	def attack(self, target):
		skip_level = randint(0, target.maneuvering)
		atack_level = randint(0, self.AI)
		if atack_level >= skip_level:
			damage_done = self.damage - target.defense
			print(self.name, "did", damage_done, "damage points to", target.name)
			target.durability = target.durability -  damage_done
			if target.check_operativity():
				print(target.name, "still has", target.durability, "durability points.")
			else:
				target.droid_destroyed()
		else:
			print("failed attack")

class Fight_droid(Base_droid):
	def __init__(self, name, strength, defense, AI, mele):
		super().__init__(name, strength, defense, AI)
		self.mele = mele
		self.durability = self.defense * 6
		self.maneuvering = self.AI * 3
		self.damage = (self.strength + self.mele) * 2

	def show_status(self):
		super().show_status()
		print("Mele: ", self.mele)



fight_droid_1 = Fight_droid("Sawing Droid", 6, 4, 2, 1)


base_droid_1 = Base_droid("Cleaning Droid", 6, 4, 2)
base_droid_2 = Base_droid("Data Droid", 7, 2, 3)
base_droid_3 = Base_droid("Droid.Exe", 5, 3, 4)

print("\n",base_droid_1.name,"\n")
base_droid_1.show_status()
print("\n",base_droid_2.name,"\n")
base_droid_2.show_status()
print("\n",base_droid_3.name,"\n")
base_droid_3.show_status()
print("\n",fight_droid_1.name,"\n")
fight_droid_1.show_status()

def fight(droid1, droid2):
	droid1.restore_durability()
	droid2.restore_durability()
	while droid1.durability > 0 and droid2.durability > 0:
		droid1.attack(droid2)
		if droid2.durability > 0:
			droid2.attack(droid1)
		else:
			continue

print("\nFirst fight")
fight(base_droid_1, base_droid_2)
print("\nsecond fight")
fight(base_droid_1, base_droid_3)
print("\nthird fight")
fight(base_droid_3, base_droid_2)
print("\n4 fight")
fight(fight_droid_1, base_droid_2)
print("\n5 fight")
fight(fight_droid_1, base_droid_2)
print("\n6 fight")
fight(fight_droid_1, base_droid_2)