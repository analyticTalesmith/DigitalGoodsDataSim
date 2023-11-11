import pandas as pd
import random
from util import data_sim as ds
from util import semantic_simularity

#CONSTANTS
NUM_PURCHASES           = 200
MAX_ITEMS               = 5
DATA_YEARS_DURATION     = 2

#Import CSV of product data and create list
productsDF = pd.read_csv('Products.csv')
productNames = productsDF["Product Name"].tolist()

#Calculate semantic simularity of items based on product name
#associationArray = semantic_simularity.semantic_array(productNames)

ds.generate_customer()

