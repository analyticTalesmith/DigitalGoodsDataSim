import datetime
from datetime import date
from datetime import timedelta
import numpy as np
import random
from util import real_city_provider as real_city

def generate_customer():
    gender = random.choices(["Man", "Woman", "Non-binary", "Other/Prefer Not to Say"], weights = [.4818, .511 ,.0036, .0036], k = 1)[0]
    age = max(18, round(np.random.normal(46, 13)))
    town = real_city.get_real_city()
    return([gender, age, town])

def generate_sales_data(productList, priceList, weightList,  maxPurchaseSize = 10, dataYears = 1):
    customerData = []
    orderData = []
    salesData = []
    
    customerID = 1000
    orderID = 1000

    productBias = [] #Biases the first product that is purchased
    biasChoices = []

    for i in range(1, 51):
        for _ in range(round((51-i)/2)):
            biasChoices.append(i)

    for i in range(len(productList)):
        productBias.append(random.choice(biasChoices))

    today = date.today()
    daysDiff = 365*dataYears
    startDate = today - timedelta(days = daysDiff)

    purchaseWeight = []        
    for i in range(maxPurchaseSize):
        purchaseWeight.append(maxPurchaseSize - i)

    #Simulate each day - ###This will eventually be for the full range of daysDiff
    curDate = startDate
    for i in range(1):
        #Simulate number of customers for that day
        numCustomers = round(max(0,np.random.normal(i*.25+20, 15)))

        #Then loop through each customer
        for i in range(numCustomers):

            #for each customer, generate demographic data and add it to the customerDate list
            customerInfo = generate_customer()
            customerData.append([customerID, customerInfo[0], customerInfo[1], customerInfo[2]])
            

            #clear helper list for new items
            basket = []

            #Randomly "buy" one item
            itemChoice = random.choices(range(len(productList)), weights = productBias, k = 1)[0]

            #Determine number of additional items to buy
            additionalItemsNum = random.choices(range(maxPurchaseSize), purchaseWeight)[0]

            #"Buy" them if applicable
            if additionalItemsNum > 0:
                basket = random.choices(range(len(productList)), weights=weightList[1], k = additionalItemsNum)
            basket.append(itemChoice)
            
            print(f"Customer {customerID}")
            #Loop through items and add them to the purchase table
            totalRevenue = 0
            for item in basket:
                print(f"\t{item} ({priceList[item]})")
                salesData.append([orderID, item])
                totalRevenue += float(priceList[item])

            orderData.append([orderID, customerID, additionalItemsNum, totalRevenue])
            customerID += 1
            orderID += 1
        curDate + timedelta(days = i)
        
    print(salesData)
    print(orderData)
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