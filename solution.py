import requests


def getModelsFromYear(year):
    response = requests.get("https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/honda/modelyear/{}?format=json".format(year))
    return response.json()['Results']


def getDiscuntinuedVehicles():
    discontinued_vehicle_model_names = {}
    models_10_yr = set()
    models_2_yr = set()
    all_models = {}
    years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
    for i in range(len(years)):
        result = getModelsFromYear(years[i])
        for eachdict in result:
            models_10_yr.add(eachdict['Model_Name'])
            all_models[eachdict['Model_Name']] = eachdict
            if len(years) - i <=2:
                models_2_yr.add(eachdict['Model_Name'])
    
    discontinued_vehicle_model_names = models_10_yr.difference(models_2_yr)
    discontinued_model_data = []
    for model_name in discontinued_vehicle_model_names:
        discontinued_model_data.append(all_models[model_name])
    
    return discontinued_model_data



print(getModelsFromYear(2018))

print(getDiscuntinuedVehicles())