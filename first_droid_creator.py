from new_droid_classes_aproach import *
from random import *


droid_core1 = Droid_Core("", 0, 0, 0)
base_droid1 = Base_droid("", 0, 0, 0, droid_core1)
fighter_droid1 = Fighter_droid("", 0, 0, 0, droid_core1, base_droid1)
support_droid1 = Support_droid("", 0, 0, 0)
super_droid1 = Super_droid("", 0, 0, 0, droid_core1, base_droid1, fighter_droid1, support_droid1)
extension_droid1 = Extension_droid("", 0, 0, 0)
humandroid1 = Humandroid("", 0, 0, 0, droid_core1, base_droid1, fighter_droid1, support_droid1, super_droid1, extension_droid1)

def create_team():
	punk_list = [[4, 1, 1], [3, 2, 1], [2, 2, 2]]

	punctuation = choice(punk_list)
	name_list = ["algo","otra cosa", "no", "nose", "quizás", "yes", "palapaokja"] 
	droidcoretest = Droid_Core(choice(name_list), punctuation[0], punctuation[1], punctuation[2])
	
	punctuation = choice(punk_list)
	shuffle(punctuation)
	basedroidtest = Base_droid(choice(name_list), punctuation[0], punctuation[1], punctuation[2], droidcoretest)



	basedroidtest.show_status()
	print(droidcoretest.strength, droidcoretest.defense, droidcoretest.AI)
	

create_team()

	


