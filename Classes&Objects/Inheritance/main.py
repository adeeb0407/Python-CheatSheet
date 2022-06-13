from chefGenralDishes import GenralChef
from chinaChefDishes import ChinaChef

chef = GenralChef()
chef2 = ChinaChef()

chef.salad()
chef2.salad() # inherited the genral Chef functions

chef.chicken()
chef2.chicken()# over rides the inherited fuction to its own function
