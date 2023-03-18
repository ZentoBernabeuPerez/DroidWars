from random import randint

class Droid_Core:
	def __init__(self, name, strength, defense, AI):
		self.name = name
		self.strength = strength
		self.defense = defense
		self.AI = AI

class Support_droid(Droid_Core):
	def __init__(self, name, strength, defense, AI):
		super().__init__(name, strength, defense, AI)	
		self.tank_support = self.defense 
		self.mobility_support = self.AI 
		self.attack_support = self.strength

class Base_droid(Droid_Core):
	def __init__(self, name, strength, defense, AI, Droid_Core):
		super().__init__(name, strength, defense, AI)
		self.name = Droid_Core.name + name	
		self.strength = strength + Droid_Core.strength
		self.defense = defense + Droid_Core.defense
		self.AI = AI + Droid_Core.AI
		self.damage = (strength + Droid_Core.strength) * 2
		self.durability = (defense + Droid_Core.defense) * 2
		self.maneuvering = (AI + Droid_Core.AI) * 2


	def show_status(self):
		print("Droid Name: ", self.name)
		print("Strength: ", self.strength)
		print("Defense: ", self.defense)
		print("AI: ", self.AI)
		print("Damage: ", self.damage)
		print("Durability: ", self.durability)
		print("Maneuvering: ", self.maneuvering)


	def check_operativity(self):
		return self.durability > 0

	def droid_destroyed(self):
		self.durability = 0
		print(self.name, "was destroyed.")

	def restore_durability(self):
		self.durability = self.defense * 4

	def is_winner(self):
		if self.durability > 0:
			return self.name

	def attack(self, target):
		skip_level = randint(0, target.maneuvering)
		atack_level = randint(0, self.AI)
		if atack_level >= skip_level:
			damage_done = (randint(int(self.damage / randint(2, 3)), self.damage))  - (randint(0, target.defense))
			if damage_done > 0:
				target.durability = target.durability - damage_done
				if target.check_operativity():
					print(self.name, "did", damage_done, "damage points to", target.name)
					print(target.name, "still has", target.durability, "durability points.")
					return True
				else:
					print(self.name, "did", damage_done, "damage points to", target.name)
					target.droid_destroyed()
					self.is_winner()
			else:
				print(self.name, "did no damage to", target.name)
				return True
		else:
			print(self.name + " failure.")

class Fighter_droid(Base_droid):
		def __init__(self, name, strength, defense, AI, Droid_Core, Base_droid):
			super().__init__(name, strength, defense, AI, Droid_Core)	
			self.name = Base_droid.name + name
			self.strength = strength + Droid_Core.strength + Base_droid.strength
			self.defense = defense + Droid_Core.defense + Base_droid.defense
			self.AI = AI + Droid_Core.AI + Base_droid.AI
			self.damage = (strength + Droid_Core.strength) * Base_droid.strength
			self.durability = (defense + Droid_Core.defense) * Base_droid.defense
			self.maneuvering = (AI + Droid_Core.AI) * Base_droid.AI

class Super_droid(Fighter_droid):
	def __init__(self, name, strength, defense, AI, Droid_Core, Base_droid, Fighter_droid, Support_droid):
		super().__init__(name, strength, defense, AI, Droid_Core, Base_droid)
		self.name = Fighter_droid.name + " feat. " + Support_droid.name + " " + name
		self.strength = Fighter_droid.strength + strength
		self.defense = Fighter_droid.defense + defense
		self.AI = Fighter_droid.AI + AI
		self.damage = Fighter_droid.damage * Support_droid.attack_support
		self.durability = Fighter_droid.durability * Support_droid.tank_support
		self.maneuvering = Fighter_droid.maneuvering * Support_droid.mobility_support

class Humandroid(Super_droid):
	def __init__(self, name, strength, defense, AI, Droid_Core, Base_droid, Fighter_droid, Support_droid, Super_droid, Extension_droid):
		super().__init__(name, strength, defense, AI, Droid_Core, Base_droid, Fighter_droid, Support_droid)
		self.name = name + " with " + Extension_droid.name
		self.strength = Super_droid.strength + strength
		self.defense = Super_droid.defense + defense
		self.AI = Super_droid.AI + AI
		self.damage = Super_droid.damage * Support_droid.attack_support
		self.durability = Super_droid.durability * Support_droid.tank_support
		self.maneuvering = Super_droid.maneuvering * Support_droid.mobility_support
		self.extension_droid = Extension_droid

	def attack(self, target):
		if Base_droid.attack(self, target) == True:
			Extension_droid.attack_ext(self.extension_droid, target)

class Extension_droid(Droid_Core):
	def __init__(self, name, strength, defense, AI):
		super().__init__(name, strength, defense, AI)	
		self.defense_extension = defense
		self.maneuvering_extension = AI
		self.attack_extension = strength

	def attack_ext(self, target):
		target.durability = target.durability - self.attack_extension
		if target.check_operativity():
			print(f"Attack extended did", self.attack_extension, "points of damage")
			print(f"Durability of", target.name, "is now", target.durability)
		else:
			print(f"Attack extended did", self.attack_extension, "points of damage extended")
			target.droid_destroyed()





def fight(droid1, droid2):
	droid1.restore_durability()
	droid2.restore_durability()
	while droid1.durability > 0 and droid2.durability > 0:
		droid1.attack(droid2)
		if droid2.durability > 0:
			droid2.attack(droid1)
		else:
			continue


