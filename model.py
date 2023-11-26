import sys
sys.path.append(r"C:\Users\Budha\Documents\GeoAnn\CityGeoTools-master\metrics")
import os
import numpy as np
from data import CityInformationModel as BaseModel
#folder ="/CityGeoTools-master"

city_model = BaseModel.CityInformationModel(city_name="Miass", city_crs=32641, cwd="../")
print(city_model)

print(city_model.Buildings)
print(city_model.Services)