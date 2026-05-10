import math

async def main():
    print("\nI won't lie I am like very bad at organizing and for some stuff I don't wanna so I will make a list that you can search on to find all of them. Any suggestions can go in the issues area.\n")
    while True:
        from_unit = int(await input("What would you like to convert from?\n(1)Pounds\n(2)Something Else BTW if it is something else you can only go to pounds.\n"))
        if from_unit == 1:
            number1 = float(await input("How many pounds?\n"))
            option1 = int(await input("What Group of Stuff?\n(1)Convential Units\n(2)Unconventional Units (still real just not very usable)\n(3)Just stupid stuff\n"))
            
            
#pounds to convential units
            if option1 == 1:
                to_unit = int(await input("What would you like to convert to?\n(1)Grams\n(2)Milligrams\n(3)Kilograms\n(4)Metric Ton\n(5)Ounce\n(6)Pound\n(7)Stone\n(8)Hundredweight\n(9)US Ton\n"))
                if to_unit == 1:
                    print(number1 * 453.592)
                elif to_unit == 2:
                    print(number1 * 453592)
                elif to_unit == 3:
                    print(number1 * 0.453592)
                elif to_unit == 4:
                    print(number1 * 0.000453592)
                elif to_unit == 5:
                    print(number1 * 16)
                elif to_unit == 6:
                    print(number1)
                elif to_unit == 7:
                    print(number1 * 0.0714286)
                elif to_unit == 8:
                    print(number1 * 0.02)
                elif to_unit == 9:
                    print(number1 * 0.0005)
            
            
# pounds to Unconventional Units
            if option1 == 2:
                option2 = int(await input("What group of stuff?\n(1)Troy and Apothecary units\n(2)Tower Weights\n(3)Roman Units\n(4)Babylonian Units\n(5)Ancient Egyptian Units\n(6)Misc stuff that I might organize later\n"))
                
                
#pounds to troy and apothecary units. 
                if option2 == 1:
                    to_unit = int(await input("What would you like to convert to?\n(1)Grains\n(2)Pennyweights\n(3)Troy Ounces\n(4)Troy Pounds\n(5)Apothecary Ounces\n(6)Apothecary Pounds\n(7)Dram\n(8)Scruple\n"))
                    if to_unit == 1:
                        print(number1 * 7000)
                    elif to_unit == 2:
                        print(number1 * 700)
                    elif to_unit == 3:
                        print(number1 * 14.5833)
                    elif to_unit == 4:
                        print(number1 * 0.583333)
                    elif to_unit == 5:
                        print(number1 * 12)
                    elif to_unit == 6:
                        print(number1 * 0.75)
                    elif to_unit == 7:
                        print(number1 * 256)
                    elif to_unit == 8:
                        print(number1 * 480)
                
                
#pounds to tower weights.
                if option2 == 2:
                    to_unit = int(await input("What would you like to convert to?\n(1)Tower Ounces\n(2)Tower Pounds\n"))
                    if to_unit == 1:
                        print(number1 * 7000 / 450)
                    if to_unit == 2:
                        print(number1 * 7000 / 450 / 12)
                
                
#pounds to roman units.
                if option2 == 3:
                    to_unit = int(await input("What would you like to convert to?\n(1)Uncia\n(2)Libra\n(3)Siliqua\n(4)Deunx\n(5)Dextans\n(6)Dodrans\n(7)Bes\n(8)Septunx\n(9)Semis\n(10)Quincunx\n(11)Triens\n(12)Quadrans\n(13)Sextans\n(14)Scrupulum\n(15)Obulos\n(16)Sicilicus\n"))
                    if to_unit == 1:
                        print(number1 * 1.404 * 12)
                    if to_unit == 2:
                        print(number1 * 1.404)
                    if to_unit == 3:
                        print(number1 * 1.404 * 12 * 144)
                    if to_unit == 4:
                        print(number1 * 1.404 * 12 * 11)
                    if to_unit == 5:
                        print(number1 * 1.404 * 12 * 10)
                    if to_unit == 6:
                        print(number1 * 1.404 * 12 * 9)
                    if to_unit == 7:
                        print(number1 * 1.404 * 12 * 8)
                    if to_unit == 8:
                        print(number1 * 1.404 * 12 * 7)
                    if to_unit == 9:
                        print(number1 * 1.404 * 12 * 6)
                    if to_unit == 10:
                        print(number1 * 1.404 * 12 * 5)
                    if to_unit == 11:
                        print(number1 * 1.404 * 12 * 4)
                    if to_unit == 12:
                        print(number1 * 1.404 * 12 * 3)
                    if to_unit == 13:
                        print(number1 * 1.404 * 12 * 2)
                    if to_unit == 14:
                        print(number1 * 1.404 * 12 * 24)
                    if to_unit == 15:
                        print(number1 * 1.404 * 12 * 48)
                    if to_unit == 16:
                        print(number1 * 1.404 * 12 * 24)
                
                
#pounds to babylonian units.
                if option2 == 4:
                    to_unit = int(await input("What would you like to convert to?\n(1)Shekel\n(2)Mina\n(3)Talent\n"))
                    if to_unit == 1:
                        print(number1 * 453.592 * 11.25)
                    if to_unit == 2:
                        print(number1 * 453.592 * 11.25 * 60)
                    if to_unit == 3:
                        print(number1 * 453.592 * 11.25 * 3600)
                
                
#pounds to ancient egyptian units.
                if option2 == 5:
                    to_unit = int(await input("What would you like to convert to?\n(1)Deben\n(2)Kite\n(3)Shematy\n"))
                    if to_unit == 1:
                        print(number1 / 0.198)
                    if to_unit == 2:
                        print(number1 / 0.198 / 10)
                    if to_unit == 3:
                        print(number1 / 0.198 / 12)
            
            
#pounds to stupid stuff
            if option1 == 3:
                option2 = int(await input("What group of stuff?\n(1)Cosmic Stuff\n(2)Currencies\n(3)Family And Friends\n(4)Misc\n"))

                if option2 == 1:
                    option3 = int(await input("What group of stuff?\n(1)Milky Way\n"))
                    if option3 == 1:
                        
#pounds to milky way planets and the moon
                        to_unit = int(await input("What would you like to convert it to?\n(1)Earth\n(2)Moon\n(3)Mercury\n(4)Mars\n(5)Jupiter\n(6)Saturn\n(7)Uranus\n(8)Neptune\n(9)Pluto\n"))
                        if to_unit == 1:
                            print(number1 / 1.37e25)
                        if to_unit == 2:
                            print(number1 / 1.62e23)
                        if to_unit == 3:
                            print(number1 / 7.28e23)
                        if to_unit == 4:
                            print(number1 / 1.41e24)
                        if to_unit == 5:
                            print(number1 / 4.184e27)
                        if to_unit == 6:
                            print(number1 / 1.25e27)
                        if to_unit == 7:
                            print(number1 / 1.91e26)
                        if to_unit == 8:
                            print(number1 / 2.25e26)
                        if to_unit == 9:
                            print(number1 / 2.87e22)
                
                
#pounds to currencies.
                if option2 == 2:
                    option3 = int(await input("Which Currencies?\n(1)USD\n"))
                    
#pounds to USD
                    if option3 == 1:
                        to_unit = int(await input("What would you like to convert it to?\n(1)Bills (they are all the same weight, $1 - $100 bills)\n(2)Pennies before 1983\n(3)Pennies after 1983\n(4)Nickels\n(5)Dimes\n(6)Quarters\n(7)Half Dollars\n(8)Dollar Coins\n"))
                        if to_unit == 1:
                            print(number1 * 453.592)
                        if to_unit == 2:
                            print(number1 * 453.592 / 3.11)
                        if to_unit == 3:
                            print(number1 * 453.592 / 2.5)
                        if to_unit == 4:
                            print(number1 * 453.592 / 5)
                        if to_unit == 5:
                            print(number1 * 453.592 / 2.268)
                        if to_unit == 6:
                            print(number1 * 453.592 / 5.67)
                        if to_unit == 7:
                            print(number1 * 453.592 / 11.34)
                        if to_unit == 8:
                            print(number1 * 453.592 / 8.1)


#pounds to family and friends
                if option2 == 3:
                    to_unit = int(await input("What would you like to convert it to?\n(1)Buttercup the Dog\n"))
                    if to_unit == 1:
                        print(number1 / 18.8)


#pounds to misc
                if option2 == 4:
                    to_unit = int(await input("What would you like to convert it to?\n(1)Party sized bag of hot cheetos\n(2)Large Blahaj\n(3)Small Blahaj\n)"))
                    if to_unit == 1:
                        print(number1 / 1.12)
                    if to_unit == 2:
                        print(number1 * 16 / 24)
                    if to_unit == 3:
                        print(number1 * 16 / 7)


# Convert something else to pounds.
        if from_unit == 2:
            number1 = float(await input("How many of that unit?\n"))
            option1 = int(await input("What Group of Stuff?\n(1)Conventional Units\n(2)Unconventional Units (still real just not very usable)\n"))
            
            
#conventional units to pounds
            if option1 == 1:
                to_unit = int(await input("What would you like to convert to?\n(1)Grams\n(2)Milligrams\n(3)Kilograms\n(4)Metric Ton\n(5)Ounce\n(6)Pound\n(7)Stone\n(8)Hundredweight\n(9)US Ton\n"))
                if to_unit == 1:
                    print(number1 / 453.592)
                elif to_unit == 2:
                    print(number1 / 453592)
                elif to_unit == 3:
                    print(number1 / 0.453592)
                elif to_unit == 4:
                    print(number1 / 0.000453592)
                elif to_unit == 5:
                    print(number1 / 16)
                elif to_unit == 6:
                    print(number1)
                elif to_unit == 7:
                    print(number1 / 0.0714286)
                elif to_unit == 8:
                    print(number1 / 0.02)
                elif to_unit == 9:
                    print(number1 / 0.0005)

        if from_unit < 1 or from_unit > 2:
            print("Brother put in a real input")
        if await input("Do you want to convert something else? (y/n)\n") == "n":
            break