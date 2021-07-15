import re
import matplotlib
from matplotlib import cm

def extract_data(file:str):
    '''
    (str)->(list)

    Gets a string with the location of the tcx file and returns list of the content
    '''
    with open("maps/"+file, 'r', encoding='utf-8') as infile:
        raw_data = list(infile)
        result = raw_data[0].split("<Trackpoint>") #first split

    return result

def add_average(lista, rango):
    '''
    (list, number) -> (list)

    gets a list of values and gets their average in blocks of "rango" i.e: rango = 10, it will get the average
    from 10 to 10 and creates a list of the same size with repeated values
    '''
    promedio = []
    suma = 0
    avg = len(lista)%rango
    result = []

    for i, j in enumerate(lista):
        suma+=j
        if (i+1)%rango == 0 and i !=0:
            promedio.append(suma/rango)
            suma=0
        elif i == len(lista)-1:
            promedio.append(suma/avg)

    elements_num = int(len(lista)/rango)

    for i in promedio[:elements_num]:
        for j in range(rango):
            result.append(i)

    for i in promedio[elements_num:]:
        for j in range(avg):
            result.append(i)

    return result


def get_info_formatted(tcx_file:str):
    '''
    ()-> (float, float)

    Extract the data from the tcx file
    '''

    #regex to get data
    latitude = "<LatitudeDegrees>(.*?)</LatitudeDegrees>"
    longitude = "<LongitudeDegrees>(.*?)</LongitudeDegrees>"
    altitude = "<AltitudeMeters>(.*?)</AltitudeMeters>"
    distance = "<DistanceMeters>(.*?)</DistanceMeters>"

    #extract raw data from tcx_file
    result = extract_data(tcx_file)

    location_data = []
    distancia_for_now = 0
    temp_speed = []

    for i in range(1,len(result),5):
        dis = re.search(distance, str(result[i]))
        if dis != None: #if distance present, add to the last dict
            variation = abs(float(dis.group(1)) - distancia_for_now)
            distancia_for_now = float(dis.group(1))
            speed = (variation*18)/float(5) #conver from m/s to km/s
            temp_speed.append(speed)

    '''
    Calculate the color of each segment
    '''
    velocidad = add_average(temp_speed, 20) # gets the sppeds and average in block

    lati = []
    long = []
    alti = []
    for i in result:
        lat = re.search(latitude, str(i))
        lon = re.search(longitude, str(i))
        alt = re.search(altitude, str(i))
        if lat and lon and alt != None: #if it doesn't has a latitude or longitude, skips the line
            lati.append(float(lat.group(1)))
            long.append(float(lon.group(1)))
            alti.append(float(alt.group(1)))

    return {"latitude":lati, "longitude":long, "speed":velocidad, "altitude":alti}
