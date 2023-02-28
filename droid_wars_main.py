from random import randint
"""La primera idea es ahora crear una clase mas basica aun que solo contenga los atributos base (name, strength, defense, AI)
para asi diverger la clase base entre droides de servicio y droides de pelea basicos, los de servicio serviran para
implementar mejoras en los droides superiores, por ejemplo que les den bonus o los puedan reparar)
La segunda idea es hacer que el daño sea tambien aleatorio sergfun los status de los robots (de momento es un randint de 1 a 4
pero habria que cambiarlo por un factor propio o del arma
La tercera idea es agregar un bloque de accion extra en el ataque para ejecutar acciones bonus o algo asi (como implementaciones de los droides superiores"""
class Droid:
	def __init__(self, name, strength, defense, AI):
		self.name = name
		self.strength = strength
		self.defense = defense
		self.AI = AI



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

	"""def attack(self, target):
		skip_level = randint(0, target.maneuvering)
		atack_level = randint(0, self.AI)
		if atack_level >= skip_level:
			damage_done = (self.damage * randint(1, 2))  - (target.defense * randint(1,4))
			if damage_done > 0:
				print(self.name, "did", damage_done, "damage points to", target.name)
				target.durability = target.durability -  damage_done
				if target.check_operativity():
					print(target.name, "still has", target.durability, "durability points.")
				else:
					target.droid_destroyed()
			else:
				damage = 0
				print(self.name, "did", damage_done, "damage points to", target.name)
				target.durability = target.durability -  damage_done"""

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
print("\n4 fight")
fight(fight_droid_1, base_droid_2)
print("\n5 fight")
fight(fight_droid_1, base_droid_2)
print("\n6 fight")
fight(fight_droid_1, base_droid_2)
print("-------------second gen droids-------------")
fight(fight_droid_1, fight_droid_2)