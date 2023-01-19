from Stocks import Stocks
from Property import Property
from Portfolio import Portfolio
import Constants
import Equations


# base strategy with 100k initial investment (50% stock, 50% property)
def base():
    portfolio1 = Portfolio(100000)
    portfolio1.base(10)
    portfolio1.showPortfolio()
    portfolio1.showNetWorth()


# only stock portfolio
def stockOnly():
    portfolio2 = Portfolio(100000)
    portfolio2.onlyStock(50)
    portfolio2.showPortfolio()
    portfolio2.showNetWorth()

# only property portfolio
def propertyOnly():
     portfolio3 = Portfolio(100000)
     portfolio3.onlyProperty(50)
     portfolio3.showPortfolio()
     portfolio3.showNetWorth()

base()
