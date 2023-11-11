import datetime
from datetime import date
from datetime import timedelta
import numpy as np




def generate_sales_data(maxPurchaseSize = 10, dataYears = 1):
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

        #for i in range(numCustomers):
        #    basket = []

        #    #Randomly "buy" one item
        #    itemChoice = random.randint(0, len(productNames)-1)

        #    #Determine number of additional items to buy
        #    additionalItemsNum = random.choices(range(MAX_ITEMS), purchaseWeight)[0]

        #    #"Buy" them if applicable
        #    if additionalItemsNum > 0:
        #        basket = random.choices(range(len(productNames)), weights=weightList[1], k = additionalItemsNum)

        #    basket.append(itemChoice)


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