import datetime
from datetime import date
from datetime import timedelta
import numpy as np
import random
import real_city

def generate_customer():
    gender = random.choices(["Man", "Woman", "Non-binary", "Other/Prefer Not to Say"], weights = [.4818, .511 ,.0036, .0036], k = 1)[0]
    age = max(18, round(np.random.normal(46, 13)))
    town = real_city.get_real_city()
    return([gender, age, town])

def generate_sales_data(maxPurchaseSize = 10, dataYears = 1):
    
    customerData = []
    purchaseData = []

    customerID = 1000
    orderID = 1000

    today = date.today()
    daysDiff = 365*dataYears
    startDate = today - timedelta(days = daysDiff)

    purchaseWeight = []        
    for i in range(maxPurchaseSize):
        purchaseWeight.append(maxPurchaseSize - i)

    #Simulate each day
    for i in range(10):
        curDate = startDate + timedelta(days = i)
    
        #Simulate number of customers for that day
        numCustomers = round(max(0,np.random.normal(i*.25+20, 15)))
        for i in range(numCustomers):
            customerInfo = generate_customer()
            customerData.append([customerID, customerInfo[0], customerInfo[1], customerInfo[2]])

            basket = []

            #Randomly "buy" one item
            itemChoice = random.randint(0, len(productNames)-1)

            #Determine number of additional items to buy
            additionalItemsNum = random.choices(range(MAX_ITEMS), purchaseWeight)[0]

            #"Buy" them if applicable
            if additionalItemsNum > 0:
                basket = random.choices(range(len(productNames)), weights=weightList[1], k = additionalItemsNum)

            basket.append(itemChoice)


        '''


for i in range(NUM_PURCHASES):
    basket = []

    #Randomly "buy" one item
    itemChoice = random.randint(0, len(productNames)-1)

    #Determine number of additional items to buy
    additionalItemsNum = random.choices(range(MAX_ITEMS), purchaseWeight)[0]

    #"Buy" them if applicable
    if additionalItemsNum > 0:
        basket = random.choices(range(len(productNames)), weights=weightList[1], k = additionalItemsNum)

    basket.append(itemChoice)
    #for item in basket:
    #    print(productNames[item])

    '''