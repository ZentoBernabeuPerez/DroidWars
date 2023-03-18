from new_droid_classes_aproach import *

droid_Core1 = Droid_Core("Pure ", 4, 1, 1)
base_droid1 = Base_droid("Fucking ", 3, 2, 1, droid_Core1)
fighter_droid1 = Fighter_droid("Metal", 2, 2, 2, droid_Core1, base_droid1)
support_droid1 = Support_droid("PLOWINK", 2, 1, 1)
super_droid1 = Super_droid("The Killer!", 3, 3, 2, droid_Core1, base_droid1, fighter_droid1, support_droid1)
extension_droid1 = Extension_droid("the defender", 1, 1, 4)
humandroid1 = Humandroid("Stiff!", 3, 3, 2, droid_Core1, base_droid1, fighter_droid1, support_droid1, super_droid1, extension_droid1)


droid_Core2 = Droid_Core("Young ", 2, 2, 2)
base_droid2 = Base_droid("Naive ", 2, 2, 2, droid_Core2)
fighter_droid2 = Fighter_droid("Sucker ", 2, 2, 2, droid_Core2, base_droid2) 
support_droid2 = Support_droid("CHANTILLY", 1, 1, 2)
super_droid2 = Super_droid("True Motherfucker!", 2, 3, 3, droid_Core2, base_droid2, fighter_droid2, support_droid2)
extension_droid2 = Extension_droid("the attacker", 4, 1, 1)
humandroid2 = Humandroid("Plataplac!", 2, 3, 3, droid_Core2, base_droid2, fighter_droid2, support_droid2, super_droid2, extension_droid2)


droid_Core3 = Droid_Core("Chumbawamba ", 2, 3, 1)
base_droid3 = Base_droid("Shared ", 2, 1, 3, droid_Core3)
fighter_droid3 = Fighter_droid("Plots ", 3, 2, 1, droid_Core3, base_droid3) 
support_droid3 = Support_droid("SEHNSUCHT", 2, 1, 1)
super_droid3 = Super_droid("Fertile Death!", 4, 1, 3, droid_Core3, base_droid3, fighter_droid3, support_droid3)
extension_droid3 = Extension_droid("apachusque", 4, 1, 1)
humandroid3 = Humandroid("VayaJamba!", 3, 2, 3, droid_Core3, base_droid3, fighter_droid3, support_droid3, super_droid3, extension_droid3)



print("______FIGHTS__________")
num_of_fights = 10
print("___BASE FIGHTS_______")
bcounter_a = 0
bcounter_b = 0
for i in range(0, num_of_fights):
	fight(base_droid1, base_droid2)
	if base_droid1.is_winner():
		bcounter_a = bcounter_a + 1
	else:
		bcounter_b = bcounter_b + 1
	print("-------------------------")
	base_droid1.restore_durability()
	base_droid2.restore_durability()

print("\n\n\n\n\n\n\n\n\n\n\n")
print("____Fighters Fights____")
fcounter_a = 0
fcounter_b = 0
for i in range(0, num_of_fights):
	fight(fighter_droid1, fighter_droid2)
	if fighter_droid1.is_winner():
		fcounter_a = fcounter_a + 1
	else:
		fcounter_b = fcounter_b + 1
	print("-------------------------")
	fighter_droid1.restore_durability()
	fighter_droid2.restore_durability()

print("\n\n\n\n\n\n\n\n\n\n\n")
print("____Super Fights____")
scounter_a = 0
scounter_b = 0
for i in range(0, num_of_fights):
	fight(super_droid1, super_droid2)
	if super_droid1.is_winner():
		scounter_a = scounter_a + 1
	else:
		scounter_b = scounter_b + 1
	print("-------------------------")
	super_droid1.restore_durability()
	super_droid2.restore_durability()



print("\n\n\n\n\n\n\n\n\n\n\n")
print("____Humandroid Fights____")
hcounter_a = 0
hcounter_b = 0
for i in range(0, num_of_fights):
	fight(humandroid1, humandroid2)
	if humandroid1.is_winner():
		hcounter_a = hcounter_a + 1
	else:
		hcounter_b = hcounter_b + 1
	print("-------------------------")
	humandroid1.restore_durability()
	humandroid2.restore_durability()



print("#####################")
base_droid1.show_status()
base_droid2.show_status()
print(f"a= ",bcounter_a)
print(f"b= ",bcounter_b)
print("#####################")
fighter_droid1.show_status()
fighter_droid2.show_status()
print(f"a= ",fcounter_a)
print(f"b= ",fcounter_b)
print("#####################")
super_droid1.show_status()
super_droid2.show_status()
print(f"a= ",scounter_a)
print(f"b= ",scounter_b)
print("#####################")
humandroid1.show_status()
humandroid2.show_status()
print(f"a= ",hcounter_a)
print(f"b= ",hcounter_b)

print("______FIGHTS__________")
print("___BASE FIGHTS_______")
bcounter_a = 0
bcounter_b = 0
for i in range(0, num_of_fights):
	fight(base_droid3, base_droid2)
	if base_droid3.is_winner():
		bcounter_a = bcounter_a + 1
	else:
		bcounter_b = bcounter_b + 1
	print("-------------------------")
	base_droid3.restore_durability()
	base_droid2.restore_durability()

print("\n\n\n\n\n\n\n\n\n\n\n")
print("____Fighters Fights____")
fcounter_a = 0
fcounter_b = 0
for i in range(0, num_of_fights):
	fight(fighter_droid3, fighter_droid2)
	if fighter_droid3.is_winner():
		fcounter_a = fcounter_a + 1
	else:
		fcounter_b = fcounter_b + 1
	print("-------------------------")
	fighter_droid3.restore_durability()
	fighter_droid2.restore_durability()

print("\n\n\n\n\n\n\n\n\n\n\n")
print("____Super Fights____")
scounter_a = 0
scounter_b = 0
for i in range(0, num_of_fights):
	fight(super_droid3, super_droid2)
	if super_droid3.is_winner():
		scounter_a = scounter_a + 1
	else:
		scounter_b = scounter_b + 1
	print("-------------------------")
	super_droid3.restore_durability()
	super_droid2.restore_durability()



print("\n\n\n\n\n\n\n\n\n\n\n")
print("____Humandroid Fights____")
hcounter_a = 0
hcounter_b = 0
for i in range(0, num_of_fights):
	fight(humandroid3, humandroid2)
	if humandroid3.is_winner():
		hcounter_a = hcounter_a + 1
	else:
		hcounter_b = hcounter_b + 1
	print("-------------------------")
	humandroid3.restore_durability()
	humandroid2.restore_durability()



print("#####################")
base_droid3.show_status()
base_droid2.show_status()
print(f"a= ",bcounter_a)
print(f"b= ",bcounter_b)
print("#####################")
fighter_droid3.show_status()
fighter_droid2.show_status()
print(f"a= ",fcounter_a)
print(f"b= ",fcounter_b)
print("#####################")
super_droid3.show_status()
super_droid2.show_status()
print(f"a= ",scounter_a)
print(f"b= ",scounter_b)
print("#####################")
humandroid3.show_status()
humandroid2.show_status()
print(f"a= ",hcounter_a)
print(f"b= ",hcounter_b)