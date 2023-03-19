from new_droid_classes_aproach import *
from random import *



def create_team():
	punk_list = [[4, 1, 1], [3, 2, 1], [2, 2, 2]]
	name_list = ["algo","otra cosa", "no", "nose", "quizás", "yes", "palapaokja"] 
	
	"""base + core"""
	punctuation = choice(punk_list)
	shuffle(punctuation)
	droidcoreobject = Droid_Core(choice(name_list), punctuation[0], punctuation[1], punctuation[2])
	
	punctuation = choice(punk_list)
	shuffle(punctuation)
	basedroidobject = Base_droid(choice(name_list), punctuation[0], punctuation[1], punctuation[2], droidcoreobject)

	"""fighter"""
	punctuation = choice(punk_list)
	shuffle(punctuation)
	fighterdroidobject = Fighter_droid(choice(name_list), punctuation[0], punctuation[1], punctuation[2], droidcoreobject, basedroidobject)

	"""super + support"""
	punctuation = choice(punk_list)
	shuffle(punctuation)
	supportdroidobject = Support_droid(choice(name_list), punctuation[0], punctuation[1], punctuation[2])
	
	punctuation = choice(punk_list)
	shuffle(punctuation)
	superdroidobject = Super_droid(choice(name_list), punctuation[0], punctuation[1], punctuation[2], droidcoreobject, basedroidobject, fighterdroidobject, supportdroidobject)

	"""humandroid"""
	punctuation = choice(punk_list)
	shuffle(punctuation)
	extensiondroidobject = Extension_droid(choice(name_list), punctuation[0], punctuation[1], punctuation[2])
	
	punctuation = choice(punk_list)
	shuffle(punctuation)
	humandroidobject = Humandroid(
		choice(name_list), 
		punctuation[0], punctuation[1], punctuation[2], 
		droidcoreobject, basedroidobject, fighterdroidobject, supportdroidobject, superdroidobject, extensiondroidobject
		)


	return [droidcoreobject, basedroidobject, fighterdroidobject, supportdroidobject, superdroidobject, extensiondroidobject, humandroidobject]



"""the order of the return objects is
0 droidcore
1 basedroid
2 fighter
3 support
4 super
5 extension
6 humandroid
"""
	
team_1 = create_team()
basedroid_1 = team_1[1]
fighter_droid_1 = team_1[2]
super_droid_1 = team_1[4]
humandroid_1 = team_1[6]


team_2 = create_team()
basedroid_2 = team_2[1]
fighter_droid_2 = team_2[2]
super_droid_2 = team_2[4]
humandroid_2 = team_2[6]



print("______FIGHTS__________")
num_of_fights = 10
print("___BASE FIGHTS_______")
bcounter_a = 0
bcounter_b = 0
for i in range(0, num_of_fights):
	fight(basedroid_1, basedroid_2)
	if basedroid_1.is_winner():
		bcounter_a = bcounter_a + 1
	else:
		bcounter_b = bcounter_b + 1
	print("-------------------------")
	basedroid_1.restore_durability()
	basedroid_2.restore_durability()

print("\n\n\n\n\n\n\n\n\n\n\n")
print("____Fighters Fights____")
fcounter_a = 0
fcounter_b = 0
for i in range(0, num_of_fights):
	fight(fighter_droid_1, fighter_droid_2)
	if fighter_droid_1.is_winner():
		fcounter_a = fcounter_a + 1
	else:
		fcounter_b = fcounter_b + 1
	print("-------------------------")
	fighter_droid_1.restore_durability()
	fighter_droid_2.restore_durability()

print("\n\n\n\n\n\n\n\n\n\n\n")
print("____Super Fights____")
scounter_a = 0
scounter_b = 0
for i in range(0, num_of_fights):
	fight(super_droid_1, super_droid_2)
	if super_droid_1.is_winner():
		scounter_a = scounter_a + 1
	else:
		scounter_b = scounter_b + 1
	print("-------------------------")
	super_droid_1.restore_durability()
	super_droid_2.restore_durability()



print("\n\n\n\n\n\n\n\n\n\n\n")
print("____Humandroid Fights____")
hcounter_a = 0
hcounter_b = 0
for i in range(0, num_of_fights):
	fight(humandroid_1, humandroid_2)
	if humandroid_1.is_winner():
		hcounter_a = hcounter_a + 1
	else:
		hcounter_b = hcounter_b + 1
	print("-------------------------")
	humandroid_1.restore_durability()
	humandroid_2.restore_durability()


print("#####################")
team_1[0].show_base_status()
basedroid_1.show_status()
basedroid_1.sum_of_status()
team_2[0].show_base_status()
basedroid_2.show_status()
basedroid_2.sum_of_status()
print(f"a= ",bcounter_a)
print(f"b= ",bcounter_b)
print("#####################")
fighter_droid_1.show_status()
fighter_droid_1.sum_of_status()
fighter_droid_2.show_status()
fighter_droid_2.sum_of_status()
print(f"a= ",fcounter_a)
print(f"b= ",fcounter_b)
print("#####################")
team_1[3].show_base_status()
super_droid_1.show_status()
super_droid_1.sum_of_status()
team_2[3].show_base_status()
super_droid_2.show_status()
super_droid_2.sum_of_status()
print(f"a= ",scounter_a)
print(f"b= ",scounter_b)
print("#####################")
team_1[5].show_base_status()
humandroid_1.show_status()
humandroid_1.sum_of_status()
team_2[5].show_base_status()
humandroid_2.show_status()
humandroid_2.sum_of_status()
print(f"a= ",hcounter_a)
print(f"b= ",hcounter_b)



