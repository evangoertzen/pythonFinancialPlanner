import Equations
import Constants

class Stocks:

    principal = 0	#amount invested at time 0
    growthRate = 0	#rate of growth in percent (ex. 1.7 = 1.7% yearly growth)
    currentVal = 0	#current value of stock given yearly compound interest on principal
    yearsOwned = 0  #number of years passed since start of simulation
    yearPurchased = 0   #year stock was purchased in simulation

    #constructor
    def __init__(self, principal, growthRate, simYear, simMonth=0):
        self.principal = principal
        self.growthRate = growthRate
        self.currentVal = principal
        self.yearsOwned = 0
        self.yearPurchased = simYear + simMonth/12

    #get value of stock x years from start using compounding interest
    def simToTime(self, years, months=0):
        self.yearsOwned = years + months/12 - self.yearPurchased
        self.currentVal = Equations.timeVal(self.principal, self.growthRate, self.yearsOwned)

    #print member variables
    def display(self):
        print()
        print("Stock information:")
        if(self.yearsOwned == 0):
            print("Principal Amount: $" + str(round(self.principal, 2)))
            print("Growth Rate: " + str(round(self.growthRate,2)) + "%")
        else:
            print("Owned for " + str(round(self.yearsOwned,2)) + " years")
        print("Current value: $" + str(round(self.currentVal,2)))
