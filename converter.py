import math
from_unit = int(input("What would you like to convert from?\n(1)Pounds\n(2)Something Else\n"))
if from_unit == 1:
    number1 = float(input("How many pounds?\n"))
    option1 = int(input("What Group of Stuff?\n(1)Convential Units\n"))
    if option1 == 1:
        to_unit = int(input("What would you like to convert to?\n(1)Grams\n(2)Milligrams\n(3)Kilograms\n(4)Metric Ton\n(5)Ounce\n(6)Pouns\n(7)Stone\n(8)Hundredweight\n(9)US Ton\n(10)Imperial Ton\n"))
        if to_unit == 1:
            
elif from_unit == 2:
    print("Under Construction")
else:
    print("Brother Just put in a real answer.")
#to_unit = input("What would you like to convert to?")
#value = float(input("What is the value you would like to convert?"))
