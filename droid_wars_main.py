from random import randint
"""mejoras en los droides superiores, por ejemplo que los puedan reparar)
La segunda idea es hacer que el daño sea tambien aleatorio sergfun los status de los robots (de momento es un randint de 1 a 4
pero habria que cambiarlo por un factor propio o del arma
La tercera idea es agregar un bloque de accion extra en el ataque para ejecutar acciones bonus o algo asi (como implementaciones de los droides superiores
Otra idea es un counteraction
La ultima idea podria ser que el combate tuviese que ocurrir en varias fases, del droide mas avanzado al mas flojo y que se gane por una puntuación conjuntaç
Falta tambien implementar unos status maxcimos y minimos para que no se vayan de madre"""

class Droid:
	def __init__(self, name, strength, defense, AI):
		self.name = name
		self.strength = strength
		self.defense = defense
		self.AI = AI

class Support_droid(Droid):
	def __init__(self, name, strength, defense, AI):
		super().__init__(name, strength, defense, AI)	
		self.tank_support = self.defense 
		self.mobility_support = self.AI 
		self.attack_support = self.strength


class Base_droid(Droid):
	def __init__(self, name, strength, defense, AI):
		super().__init__(name, strength, defense, AI)	
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
			damage_done = (self.damage * randint(1, 2))  - (target.defense * randint(1,4))
			if damage_done > 0:
				target.durability = target.durability - damage_done
				if target.check_operativity():
					print(self.name, "did", damage_done, "damage points to", target.name)
					print(target.name, "still has", target.durability, "durability points.")
					return True
				else:
					print(self.name, "did", damage_done, "damage points to", target.name)
					target.droid_destroyed()
			else:
				print(self.name, "did no damage to", target.name)
				return True
		else:
			print(self.name + " failure.")

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

class Super_droid(Fight_droid):
	def __init__(self, name, strength, defense, AI, mele, Support_droid):
		super().__init__(name, strength, defense, AI, mele)
		self.AI = AI + Support_droid.AI
		self.Support_droid = Support_droid
		self.durability = (self.defense + Support_droid.tank_support) * 8
		self.maneuvering = (self.AI + Support_droid.mobility_support) * 4 
		self.damage = (self.strength + self.mele + Support_droid.attack_support) * 2

class Humandroid(Super_droid):
	def __init__(self, name, strength, defense, AI, mele, Support_droid, Extension_droid):
		super().__init__(name, strength, defense, AI, mele, Support_droid)
		self.AI = AI + Support_droid.AI
		self.support_droid = Support_droid
		self.extension_droid = Extension_droid 
		self.durability = (self.defense + Support_droid.tank_support) * 12
		self.maneuvering = (self.AI + Support_droid.mobility_support) * 5 
		self.damage = (self.strength + self.mele + Support_droid.attack_support) * 2	

	def attack(self, target):
		if Base_droid.attack(self, target) == True:
			Extension_droid.attack_ext(self.extension_droid, target)

class Extension_droid(Droid):
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




support_droid_1 = Support_droid("Tanke", 0, 4, 0)
support_droid_2 = Support_droid("Stinger", 2, 0, 2)
support_droid_3 = Support_droid("Equilibrer", 1, 1, 2)

extension_droid_1 = Extension_droid("Chumbawamba", 2, 1, 1)
extension_droid_2 = Extension_droid("Tubthumper", 1, 1, 2)

humandroid_1 = Humandroid("C3PO", 7, 5, 4, 3, support_droid_3, extension_droid_1)
humandroid_2 = Humandroid("BinealBoy33", 5, 7, 3, 4, support_droid_2, extension_droid_2)

super_droid_1 = Super_droid("Tumbler", 6, 5, 3, 2, support_droid_3)
super_droid_2 = Super_droid("The stiff", 7, 2, 4, 3, support_droid_2)
super_droid_3 = Super_droid("Wasp", 4, 5, 4, 3, support_droid_1) 

fight_droid_1 = Fight_droid("Sawing Droid", 6, 4, 2, 1)
fight_droid_2 = Fight_droid("Defibrillator Droid", 4, 5, 3, 1)

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
print("-------------second gen droids-------------")
fight(fight_droid_1, fight_droid_2)
print("\n\n\n------------------third gen droids-----------------")
fight(super_droid_1, super_droid_2)
print("-------------------------------")
fight(super_droid_2, super_droid_3)
print("------------------------")
fight(super_droid_3, super_droid_1)
print("\n\n\n------------------fourth gen droids-----------------")
fight(humandroid_1, humandroid_2)

humandroid_1.show_status()
humandroid_2.show_status()

droidctionary = "esto es solo para acordarme del droidctionary"
attributes = [i for i in dir(base_droid_1) if not i.startswith("__")]
print(attributes)
