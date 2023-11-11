import pandas as pd
import random
from util import data_sim as ds
from util import semantic_simularity

#CONSTANTS
MAX_ITEMS               = 7
DATA_YEARS_DURATION     = 2

#Import CSV of product data and create list
productsDF = pd.read_csv('Products.csv')
productNames = productsDF["Product Name"].tolist()
productCosts = productsDF["Price"].tolist()

#Calculate semantic simularity of items based on product name
weightList = semantic_simularity.semantic_array(productNames)

#Simulate the data
results = ds.generate_sales_data(productNames, productCosts, weightList, MAX_ITEMS, DATA_YEARS_DURATION)


#Convert the results into data frames to save as CSVs
customerDF = pd.DataFrame(results[0], columns = ['CustomerID',
                                                 'Gender',
                                                 'Age',
                                                 'Location'])
customerDF.sort_values(['CustomerID'], inplace=True)


orderDF = pd.DataFrame(results[1], columns = ['OrderID',
                                              'CustomerID',
                                              'OrderDate',
                                              'TotalItems'])
orderDF.sort_values(['OrderID'], inplace=True)

salesDF = pd.DataFrame(results[2], columns = ['OrderID',
                                              'ItemID'])
salesDF.sort_values(['OrderID', 'ItemID'], inplace=True)

itemIDs = []
for i in range(1,len(productNames)+1):
    itemIDs.append(i)
productsDF["ItemID"] = itemIDs
productsDF["Category"] = productsDF["Product Program"]
productsDF = productsDF[["ItemID", "SKU", "Product Name", "Price", "Category"]]
productsDF.sort_values(['ItemID'], inplace=True)

customerDF.to_csv('generatedCSVs\\customers.csv', index=False)
orderDF.to_csv('generatedCSVs\\orders.csv', index=False)
salesDF.to_csv('generatedCSVs\\sales.csv', index=False)
productsDF.to_csv('generatedCSVs\\products.csv', index=False)