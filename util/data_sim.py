import datetime
from datetime import date
from datetime import timedelta
import numpy as np
import random
from util import real_city_provider as real_city
from math import ceil, floor

def makeWeightsForChoice(inListLen, topPerc = .2, midPerc =.5, topBoost = .5, midBoost = .5):
    
    if inListLen < 1:
        raise Exception("List length must be int > 0. Length: " + str(inListLen))
    elif inListLen == 1:
        return [1]
    elif inListLen == 2:
        return [1, 2]
    elif inListLen >= 3 :
        countTopPerf = max(1, round(topPerc*inListLen))
        countMidPerf = min(1, floor(midPerc*inListLen))
        countBotPerf = max(1, inListLen-(countTopPerf + countMidPerf))

        weights = [1]*countBotPerf
        midWeight = ceil((1+midBoost)*countBotPerf)
        topWeight = ceil((1+topBoost+midBoost)*(countBotPerf+countMidPerf))

        for _ in range(countMidPerf):
            weights.append(midWeight)
        for _ in range(countTopPerf):
            weights.append(topWeight)
        random.shuffle(weights)
        return weights
    else:
        raise Exception("Unknown error in makeWeightsForChoice")

def getTotalWeight(inList):
    runningSum = 0
    for weight in inList:
        runningSum += weight
    return runningSum

def generate_customer():
    gender = random.choices(["Man", "Woman", "Non-binary", "Other/Prefer Not to Say"], weights = [.4818, .511 ,.0036, .0036], k = 1)[0]
    age = max(18, round(np.random.normal(28, 13)+18))
    town = real_city.get_real_city()
    return([gender, age, town])

def generate_sales_data(productDF, weightList,  maxPurchaseSize = 10, dataYears = 1):
    

    productList = productDF["Product Name"].tolist()
    priceList = productDF["Price"].tolist()

    uniqueCats = productDF["Product Program"].unique()
    categoryCount = len(uniqueCats)
    categoryWeights = makeWeightsForChoice(categoryCount)


    catWeightDict = {}
    i = 0
    for category in uniqueCats:
        catWeightDict[category] = categoryWeights[i]
        i += 1

    initialItemWeights = makeWeightsForChoice(len(productList))

    itemsWeightTotal = getTotalWeight(initialItemWeights)
    categoryWeightTotal = getTotalWeight(categoryWeights)
    
    productBias = []
    for i in range(len(productList)):

        itemWeight = initialItemWeights[i]/itemsWeightTotal
        catWeight = catWeightDict[productDF["Product Program"][i]]/categoryWeightTotal

        productBias.append(1 + itemWeight + catWeight)
        

    customerData = []
    orderData = []
    salesData = []
    
    customerID = 1000
    orderID = 1000
    
    today = date.today()
    daysDiff = 365*dataYears
    startDate = today - timedelta(days = daysDiff)

    purchaseWeight = []        
    for i in range(maxPurchaseSize):
        purchaseWeight.append(maxPurchaseSize - i)

    #Simulate each day
    curDate = startDate
    dailyTrend = .5
    dailyReturnTrend = .5
    for i in range(daysDiff):
        #Simulate number of customers for that day
        #numCustomers = round(max(0,np.random.normal(i*.25+20, 15)))
        numCustomers = round(max(0,np.random.normal((.019*(i**1.3))*dailyTrend, 10)+random.randint(-20,10)/2))

        if numCustomers > 0:
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
            
                #Loop through items and add them to the purchase table
                for item in basket:
                    salesData.append([orderID, item+1])

                orderData.append([orderID, customerID, curDate.strftime('%m/%d/%Y'), additionalItemsNum+1])
                customerID += 1
                orderID += 1
            

        #Generate some data from return customers
        numReturnCustomers = round(max(0,np.random.normal((i*.014-5)*dailyReturnTrend, 5)/2))
        if numReturnCustomers > 0 and len(customerData) > numReturnCustomers:
            for i in range(numReturnCustomers):

                #for each customer, generate demographic data and add it to the customerDate list
                returnCustomerID = random.choice(customerData)[0]
            

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
            
                #Loop through items and add them to the purchase table
                for item in basket:
                    salesData.append([orderID, item+1])
                    
                orderData.append([orderID, returnCustomerID, curDate.strftime('%m/%d/%Y'), additionalItemsNum+1])
                orderID += 1

        curDate = curDate + timedelta(days = 1)
        dailyTrend = min(1, max(0.05, dailyTrend + np.random.normal(0, .2)))
        dailyReturnTrend = min(2, max(0.05, dailyReturnTrend + np.random.normal(0, .2)))
        
    return([customerData, orderData, salesData])