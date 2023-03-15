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
		self.damage = strength + Droid_Core.strength
		self.durability = defense + Droid_Core.defense
		self.maneuvering = AI + Droid_Core.AI


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
		self.name = Fighter_droid.name + " featuring " + Support_droid.name + " A.K.A " + name
		self.strength = Fighter_droid.strength + strength
		self.defense = Fighter_droid.defense + defense
		self.AI = Fighter_droid.AI + AI
		self.damage = Fighter_droid.damage * Support_droid.attack_support
		self.durability = Fighter_droid.durability * Support_droid.tank_support
		self.maneuvering = Fighter_droid.maneuvering * Support_droid.mobility_support
		


def fight(droid1, droid2):
	droid1.restore_durability()
	droid2.restore_durability()
	while droid1.durability > 0 and droid2.durability > 0:
		droid1.attack(droid2)
		if droid2.durability > 0:
			droid2.attack(droid1)
		else:
			continue


droid_Core1 = Droid_Core("Pure ", 4, 1, 1)
base_droid1 = Base_droid("Fucking ", 3, 2, 1, droid_Core1)
fighter_droid1 = Fighter_droid("Metal", 2, 2, 2, droid_Core1, base_droid1)
support_droid1 = Support_droid("PLOWINK", 2, 1, 1)
super_droid1 = Super_droid("The Killer!", 3, 3, 2, droid_Core1, base_droid1, fighter_droid1, support_droid1)

droid_Core2 = Droid_Core("Young ", 2, 2, 2)
base_droid2 = Base_droid("Naive ", 2, 2, 2, droid_Core2)
fighter_droid2 = Fighter_droid("Sucker ", 2, 2, 2, droid_Core2, base_droid2) 
support_droid2 = Support_droid("CHANTILLY", 1, 1, 2)
super_droid2 = Super_droid("True Motherfucker!", 2, 3, 3, droid_Core2, base_droid2, fighter_droid2, support_droid2)



base_droid1.show_status()
base_droid2.show_status()
print("--------------------")
fighter_droid1.show_status()
fighter_droid2.show_status()

print("______FIGHTS__________")
print("___BASE FIGHTS_______")
counter_a = 0
counter_b = 0
for i in range(0, 20):
	fight(base_droid1, base_droid2)
	if base_droid1.is_winner():
		counter_a = counter_a + 1
	else:
		counter_b = counter_b + 1
	print("-------------------------")
	base_droid1.restore_durability()
	base_droid2.restore_durability()
print(f"a= ",counter_a)
print(f"b= ",counter_b)
print("____Fighters Fights____")
counter_a = 0
counter_b = 0
for i in range(0, 20):
	fight(fighter_droid1, fighter_droid2)
	if fighter_droid1.is_winner():
		counter_a = counter_a + 1
	else:
		counter_b = counter_b + 1
	print("-------------------------")
	fighter_droid1.restore_durability()
	fighter_droid2.restore_durability()
print(f"a= ",counter_a)
print(f"b= ",counter_b)
print("____Super Fights____")
counter_a = 0
counter_b = 0
for i in range(0, 20):
	fight(super_droid1, super_droid2)
	if super_droid1.is_winner():
		counter_a = counter_a + 1
	else:
		counter_b = counter_b + 1
	print("-------------------------")
	super_droid1.restore_durability()
	super_droid2.restore_durability()
print(f"a= ",counter_a)
print(f"b= ",counter_b)

super_droid1.show_status()
super_droid2.show_status()