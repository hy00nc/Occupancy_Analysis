from file_read import *

features_train, _ = makeData("training")

def getAllTemperature():
    temperature = list()
    for line in features_train:
        temperature.append(line[0])
    return temperature

def getAllHumidity():
    humidity = list()
    for line in features_train:
        humidity.append(line[1])
    return humidity

def getAllLight():
    light = list()
    for line in features_train:
        light.append(line[2])
    return light

def getAllCO2():
    co2 = list()
    for line in features_train:
        co2.append(line[3])
    return co2

def getAllHumidityRatio():
    humidityRatio = list()
    for line in humidityRatio:
        humidityRatio.append(line[4])
    return humidityRatio

def getMaxTemperature():
    return max(getAllTemperature())

def getMinTemperature():
    return min(getAllTemperature())

def getMaxHumidity():
    return max(getAllHumidity())

def getMinHumidity():
    return min(getAllHumidity())

def getMaxLight():
    return max(getAllLight())

def getMinLight():
    return min(getAllLight())

def getMaxCO2():
    return max(getAllCO2())

def getMinCO2():
    return min(getAllCO2())

def getMaxHumidityRatio():
    return max(getAllHumidityRatio())

def getMinHumidityRatio():
    return min(getAllHumidityRatio())
