import sys
import os
import numpy
import pandas as pd

folder = "/Users/annapavlova/Downloads/city/CityGeoTools-master"
sys.path.append(folder)

from metrics.data import CityInformationModel as BaseModel

city_model = BaseModel.CityInformationModel(city_name="Miass", city_crs=32641, cwd="../")
print(city_model)

print(city_model.Buildings)