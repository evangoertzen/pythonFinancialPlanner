from Stocks import Stocks
from Property import Property
import Equations
import Constants

class Portfolio:

    principal = 0   #amount invested at time 0
    simYears = 0
    stockList = []
    propertyList = []
    totalContribution = 0

    #constructor
    def __init__(self, principal):
        print()
        print("Creating new portfolio...")
        self.principal = principal
        self.simYears = 0
        self.stockList = []
        self.propertyList = []
        self.totalContribution = principal

    def getStockVal(self, years, months=0):
        stockTotal = 0
        for stock in self.stockList:
            stock.simToTime(years, months)
            stockTotal+=stock.currentVal
        return stockTotal

    #base strategy (50% stocks, 50% property)
    def base(self, years, months=0):
        self.simYears = years + months/12
        print("Base strategy (50% stock, 50% property)")
        #invest half in stocks at 5% growth
        stockPrincip = self.principal/2
        self.stockList.append(Stocks(stockPrincip, Constants.STOCKGROWTH, 0))
        #invest half in property 500 rent, 3% appreciation rate, 5% rent increase
        propertyPrincip = self.principal/2
        self.propertyList.append(Property(propertyPrincip, Constants.PROPERTYGROWTH, Constants.RENTINCREASE, 0))

        for stock in self.stockList:
            stock.simToTime(years, months)
            #stock.display()

        for property in self.propertyList:
            property.simToTime(years, months)
            #property.display()

    #only buy stock with principal and monthly addition
    def onlyStock(self,  years, months=0):
        self.simYears = years + months/12
        print("Only stock strategy")

        self.stockList.append(Stocks(self.principal, Constants.STOCKGROWTH, 0))
        totalMonths = years*12+months
        for i in range (1, totalMonths+1):
            self.stockList.append(Stocks(Constants.MONTHLYCONTRIBUTION, Constants.RENTINCREASE, 0, i))
            self.totalContribution+=Constants.MONTHLYCONTRIBUTION
            stockVal = Portfolio.getStockVal(self, i/12)


    #only buy property
    def onlyProperty(self, years, months=0):
        self.simYears = years + months/12
        print("Only property strategy")

        self.propertyList.append(Property(self.principal, Constants.PROPERTYGROWTH, Constants.RENTINCREASE, 0))
        self.propertyList[0].simToTime(years, months)

    #save stock until you can buy property
    #monthly contributions
    def spendStock(self, years, mothns=0):
        print("Spend stock on property strategy")
        self.stockList.append

    def showPortfolio(self):
        print()
        print("Stock Investments:")
        for stock in self.stockList:
            print("Bought $" + str(round(stock.principal,2)) + " of stock in year " + str(round(stock.yearPurchased,1)) + " with " + str(stock.growthRate) + "% yearly growth. Now worth " + str(round(stock.currentVal)))
        print()

        print("Property Investments:")
        for property in self.propertyList:
            print("Bought $" + str(round(property.principal,2)) + " of property in year " + str(round(property.yearPurchased,1)) + " with $" + str(property.origRent) + " monthly rent, " + str(property.rentIncrease) + "% yearly rent increase, and " + str(property.appreciationRate) + "% yearly growth")

    def showNetWorth(self):
        stockTotal = 0
        for stock in self.stockList:
            stockTotal+=stock.currentVal

        propertyTotal=0
        totalRents = 0
        totalMortgagesPayed = 0
        for property in self.propertyList:
            propertyTotal += property.currentVal
            totalRents += property.totalRent
            totalMortgagesPayed += property.totalMortgagePayed

        netWorth = stockTotal + propertyTotal + totalRents - totalMortgagesPayed

        print()
        print("Net Worth Calculation after " + str(self.simYears) +" years:")
        print("Total stock value: $" + str(round(stockTotal,2)))
        print("Total property value: $" + str(round(propertyTotal,2)))
        print("Total rent collected: $" + str(round(totalRents,2)))
        print("Total mortgages paid: $" + str(round(totalMortgagesPayed,2)))
        print("Total contribution: $" + str(round(self.totalContribution,2)))
        print("Net worth: $" + str(round(netWorth,2)))
        print()
