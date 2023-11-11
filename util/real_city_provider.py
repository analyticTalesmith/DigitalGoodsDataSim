from faker import Faker
from faker.providers import DynamicProvider
from random import choices
import pandas as pd

cityData = pd.read_csv("USCityData.csv", encoding='latin-1')
cityData["Location"] = cityData["Name"] + ", " + cityData["Admin1 Code"]

pool = cityData["Location"].tolist()
wts = cityData["Population"].tolist()

real_city = DynamicProvider(
    provider_name="real_city",
    elements=choices(pool,weights=wts,k=len(pool)))

fake = Faker()
fake.add_provider(real_city)

def get_real_city(k=1):
    if k == 1:
        return fake.real_city()
    elif k > 0:
        results = []
        for _ in range(k):
            results.append(fake.real_city())
        return results
    else:
        raise Exception("Invalid k for real_city()")


