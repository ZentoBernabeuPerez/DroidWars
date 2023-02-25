class Droid:
	def __init__(self, name, strength, AI, defense, durability):
		self.name = name
		self.strength = strength
		self.AI = AI
		self.defense = defense
		self.durability = durability

	def show_data(self):
		print(self.name, ":", sep="")
		print("Strength: ", self.strength)
		print("AI: ", self.AI)
		print("Defense: ", self.defense)
		print("Durability: ", self.durability)
		
	def level_up(self, strength, AI, defense):
		self.strength = self.strength + strength
		self.AI = self.AI + AI
		self.defense = self.defense + defense

	def check_operative(self):
		return self.durability > 0

	def destroyed_droid(self):
		self.durability = 0
		print(self.name, "has been destroyed")

	def damage(self, target):
		return self.strength - target.defense

	def attack(self, target):
		damage = self.damage(target)
		target.durability = target.durability - damage
		print(self.name, "did", damage, "damage points to", target.name)
		if target.check_operative():
			print("Durability of", target.name, "is", target.durability, "points")
		else:
			target.destroyed_droid()



base_droid1 = Droid("Cleaning Droid", 25, 10, 10, 100)
base_droid2 = Droid("Data Droid", 22, 11, 15, 100)

