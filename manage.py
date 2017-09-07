from bike import Bike
from car import Car
from product import Product
from store import Store
import animal
from math_dojo import MathDojo
import call_center
import hospital
from underscore import Underscore

bmx = Bike(100, "30 mph")
print bmx.__repr__()
toyota = Car(20000, "120 mph", "Full", 50000)
print toyota.__repr__()
mouse = Product(10, "Computer Mouse", "5 ounces", "Logitech", 5)
print mouse.__repr__()
electronics = Store("San Jose, CA", "Me Me")
print electronics.__repr__()
hamster = animal.Animal("Hammy", 50)
print hamster.__repr__()
spot = animal.Dog()
print spot.__repr__()
maggie = animal.Dragon()
print maggie.__repr__()
al = MathDojo()
print al.__repr__()
call1 = call_center.Call("Aaron", "268-347-1484", 911, "Complaint")
print call1.__repr__()
center1 = call_center.CallCenter()
print center1.__repr__()
patient1 = hospital.Patient(135, "Deborah", "sulfonamides")
print patient1.__repr__()
general = hospital.Hospital("BB General", 100)
print general.__repr__()
_ = Underscore()
print _.__repr__()