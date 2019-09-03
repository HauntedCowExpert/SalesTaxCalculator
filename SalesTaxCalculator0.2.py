import time
import sys
i = 0

salesTaxDict = {
    "alabama" : "0.04",
    "alaska" : "0",
    "arizona" : "0.056",
    "arkansas" : "0.065",
    "california" : "0.0725",
    "colorado" : "0.029",
    "connecticut" : "0.0635",
    "delaware" : "0",
    "florida" : "0.06",
    "georgia" : "0.04",
    "idaho" : "0.06",
    "illinois" : "0.0625",
    "indiana" : "0.07",
    "iowa" : "0.06",
    "kansas" : "0.065",
    "kentucky" : "0.06",
    "louisiana" : "0.0445",
    "maine" : "0.055",
    "maryland" : "0.06",
    "massachusetts" : "0.0625",
    "michigan" : "0.06",
    "minnesota" : "0.06875",
    "mississippi" : "0.07",
    "missouri" : "0.04225",
    "montana" : "0",
    "nebraska" : "0.055",
    "nevada" : "0.046",
    "new hampshire" : "0",
    "new jersey" : "0.06625",
    "new mexico" : "0.05125",
    "new york" : "0.04",
    "north carolina" : "0.0475",
    "north dakota" : "0.05",
    "ohio" : "0.0575",
    "oklahoma" : "0.045",
    "oregon" : "0",
    "pennsylvania" : "0.06",
    "rhode island" : "0.07",
    "south carolina" : "0.06",
    "south dakota" : "0.045",
    "tennessee" : "0.07",
    "texas" : "0.0625",
    "utah" : "0.0485",
    "vermont" : "0.06",
    "virginia" : "0.043",
    "washington" : "0.065",
    "west virginia" : "0.06",
    "wisconsin" : "0.05",
    "wyoming" : "0.04"
    }

# Opening Text
print("~~~~Sales Tax Calculator~~~~")
print("~~Created by Gavin Nielsen~~")
print()
print("**DISCLAIMER**")
print("This program was last updated in August of 2019, know when the sales tax in your state has last changed. " +
      "If you are unshure, do not take this program as gospel. I am not required to update it to reflect all changes in sales tax.")

# Initial Loop            
while i == 0:
    try:
        # Loops Entry Until Exited or Errored
        while i == 0:
            print("Enter \"exit\" In The Sale Price To Exit")
            print()
            salePrice = input("Enter The Sale Price: ")
            # Exit Program If "exit" Is Entered
            if salePrice == "exit":
                print("Exiting Program")
                time.sleep(3)
                i = 3
                break
            # Program runs if "exit" is not entered
            else:
                state = input("Enter The State Of The Sale: ")

                salePrice  = float(salePrice)
                salesTax   = float(salesTaxDict[state.lower()])
                taxPrice   = salePrice * salesTax
                totalPrice = salePrice + taxPrice
                print()
                print("Sub Total: " + str(salePrice))
                print("Tax      : " + str(taxPrice))
                print("                                 " + state + " Sales Tax Is: " + str(salesTax) + "%")
                print("-------------------------------")
                print("Total Price: " + str(totalPrice))
                print()
                print()
                print()
                print()
                print()
                time.sleep(5)
    except ValueError:
        print()
        print()
        print()
        print("That Is Not A Valid Sale Price")
        print()
        print()
        print()
        print()
        print()
        print()
    except KeyError:
        print()
        print()
        print()
        print("That Is Not A Valid State")
        print()
        print()
        print()
        print()
        print()
        print()
else:
    sys.exit
    

























