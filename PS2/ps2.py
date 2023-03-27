# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:38:53 2023

@author: felhasznalo
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
def remainingBalance(balance,annualInterestRate,monthlyPaymentRate):
    """
    calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
    

    Parameters
    ----------
    balance : float
        the outstanding balance on the credit card
    annualInterestRate : float
        annual interest rate as a decimal
    monthlyPaymentRate : float
        minimum monthly payment rate as a decimal

    Returns
    -------
    float
        At the end of 12 months, print out the remaining balance.

    """
    monthlyInterestRate=annualInterestRate/12
    for i in range(1,12+1):
        minMonthlyPayment=balance*monthlyPaymentRate
        unpaidBalance=balance-minMonthlyPayment
        interest=monthlyInterestRate*unpaidBalance
        balance=unpaidBalance+interest
    return round(balance,2)    
print('Remaining balance:',remainingBalance(balance,annualInterestRate,monthlyPaymentRate)) 


def remainingBalance(balance,annualInterestRate):
    """
    calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months

    Parameters
    ----------
    balance : float
        the outstanding balance on the credit card.
    annualInterestRate : float
        annual interest rate as a decimal

    Returns
    -------
    lowestPayment : integer
        the lowest monthly payment that will pay off all debt in under 1 year

    """
    monthlyPayment=10
    newBalance=balance
    #Monthly interest rate = (Annual interest rate) / 12.0
    monthlyInterestRate=annualInterestRate/12
    lowestPayment=0
    while newBalance>=0: 
        newBalance=balance
        for i in range(1,12+1):
            #Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
            unpaidBalance=newBalance-monthlyPayment
            interest=monthlyInterestRate*unpaidBalance
            #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
            newBalance=unpaidBalance+interest
        lowestPayment=monthlyPayment    
        monthlyPayment+=10
    return lowestPayment    
print('Lowest payment:',remainingBalance(balance,annualInterestRate))

def remainingBalance(balance,annualInterestRate):
    """
    

    Parameters
    ----------
    balance : float
        DESCRIPTION.
    annualInterestRate : float
        DESCRIPTION.

    Returns
    -------
    lowestPayment : float
        the lowest monthly payment that will pay off all debt in under 1 year

    """
    #Monthly interest rate = (Annual interest rate) / 12.0
    monthlyInterestRate=annualInterestRate/12
    newBalance=1
    epsilon=0.1
    #Monthly payment lower bound = Balance / 12
    low=balance/12
    #Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
    high=(balance*(1+monthlyInterestRate)**12)/12    
    guess=(high+low)/2
    while abs(newBalance)>=epsilon: 
        newBalance=balance
        for i in range(1,12+1):
            unpaidBalance=newBalance-guess
            interest=monthlyInterestRate*unpaidBalance
            newBalance=unpaidBalance+interest
        if newBalance < 0:
            high=guess
        else:
            low=guess            
        guess=(high+low)/2
    return round(guess,2)    
print('Lowest payment:',remainingBalance(balance,annualInterestRate)) 