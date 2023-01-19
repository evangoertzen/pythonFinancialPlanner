import Equations
import Constants

class Property:

    principal = 0           #amount invested at time 0
    appreciationRate = 0    #yearly appreciation rate of property value ((ex. 1.7 = 1.7% yearly growth)
    curretnVal = 0          #current value of property given yearly compound interest on principal
    yearsOwned = 0          #number of years property has been owned
    origRent = 0            #monthly rent at start of simulation
    currentRent = 0         #current rent given yearly rent increase
    rentIncrease = 0        #yearly increase of rent by percentage
    totalRent = 0           #total rent collected from property
    yearPurchased = 0       #year purchased in simulation
    mortgagePayment = 0     #monthly mortgage payment
    totalMortgagePayed = 0  #
    mortgageTerm = 0        #mortgage term in years

    #constructor
    def __init__(self, principal, appreciationRate, rentIncrease, simYear, mortgageTerm=30):
        self.principal = principal
        self.appreciationRate = appreciationRate
        self.currentVal = principal
        self.yearsOwned= 0
        self.origRent = Equations.calcRentPayment(principal)
        self.currentRent = self.origRent
        self.rentIncrease = rentIncrease
        self.totalRent = 0
        self.yearPurchased = simYear
        self.mortgagePayment = Equations.calcMortPayment(principal, mortgageTerm)
        self.totalMortgagePayed = 0
        self.mortgageTerm = mortgageTerm




    #set property value and rent from simulation progression
    def simToTime(self, years, months=0):
        self.yearsOwned += years + months/12 - self.yearPurchased
        #get value of property over simulated time
        self.currentVal = Equations.timeVal(self.principal, self.appreciationRate, self.yearsOwned)

        #sum rent from simulation progression
        simMonths = years*12 + months
        for monthCount in range(0,simMonths+1):
            self.totalRent+=self.currentRent
            #increase rent at the end of every year
            if monthCount > 0 and monthCount%12 == 0:
                self.currentRent = Equations.timeVal(self.currentRent, self.rentIncrease, 1)
            if monthCount < 12*self.mortgageTerm:
                self.totalMortgagePayed += self.mortgagePayment


    def display(self):
        print()
        print("Property information:")
        if(self.yearsOwned == 0):
            print("Principal Amount: $" + str(round(self.principal, 2)))
            print("Appreciation Rate: " + str(round(self.appreciationRate,2)) + "%")
        else:
            print("Owned for " + str(round(self.yearsOwned,2)) + " years")
        print("Current value: $" + str(round(self.currentVal,2)))
        print("Current monthly rent: $" + str(round(self.currentRent, 2)))
        print("Total rent collected: $" + str(round(self.totalRent,2)))
        print("Total mortgage payed: $" + str(round(self.totalMortgagePayed,2)))
        print(str(self.mortgageTerm) + " year fixed rate mortgage with $" + str(round(self.mortgagePayment,2)) + " monthly payment.")
