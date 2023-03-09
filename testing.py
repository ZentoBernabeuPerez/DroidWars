from droid_wars_main import *




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
base_droid_2 = Base_droid("Data Droid", 8, 4, 4)
base_droid_3 = Base_droid("Droid.Exe", 5, 3, 4)

support_droid_a = Support_droid("support test", 1, 1, 1)
extension_droid_a = Extension_droid("Chumbawamba", 1, 1, 1)
droid_a = Base_droid("Test A", 1, 1, 1)
droid_b = Base_droid("Test B", 1, 1, 1)
fight_droid_a = Fight_droid("test fight", 1, 1, 1, 1)
super_droid_a = Super_droid("test super", 1, 1, 1, 1, support_droid_a) 
humandroid_a = Humandroid("test human", 1, 1, 1, 1, support_droid_a, extension_droid_a) 



counter_a = 0
counter_b = 0
for i in range(0, 100):
	fight(super_droid_a, fight_droid_a)
	if droid_a.is_winner():
		counter_a = counter_a + 1
	else:
		counter_b = counter_b + 1
	print("-------------------------")
	super_droid_a.restore_durability()
	fight_droid_a.restore_durability()

print(f"A win times", counter_a)
print(f"B win times", counter_b)