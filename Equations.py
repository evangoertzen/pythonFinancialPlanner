import Constants

def timeVal(currentVal, growthRate, timePassed):
    return currentVal*(1+growthRate/100)**timePassed


def calcMortPayment(principal, years, monthlyInterest = .005625):
    totalMonths = years*12
    p = principal
    i = monthlyInterest
    n = totalMonths
    payment = p*(i*(1+i)**n)/((1+i)**n-1)
    return payment

def calcRentPayment(principal):
    return principal*Constants.RENTPROPORTION
