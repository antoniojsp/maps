import re

def extract_data(file:str):
    '''
    (str)->(list)

    Gets a string with the location of the tcx file and returns list of the content
    '''
    with open(file, 'r', encoding='utf-8') as infile:
        raw_data = list(infile)
        result = raw_data[0].split("<Trackpoint>") #first split

    return result[1:]

def append_to_end(list_dictionary:list, key:str, item):
    '''
    (dict, str, val)->(dict)

    adds an extra key to the last dictionary present in a list
    '''
    temp = list_dictionary[-1]
    temp[str(key)] = item
    list_dictionary[-1] = dict(temp)
    return list_dictionary

def add_average(lista, rango):
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

    for i in result:
        dis = re.search(distance, str(i))
        if dis != None: #if distance present, add to the last dict
            variation = abs(float(dis.group(1)) - distancia_for_now)
            distancia_for_now = float(dis.group(1))
            speed = (variation*18)/float(5)
            temp_speed.append(speed)

    velo = add_average(temp_speed, 10)
    k = 0

    for i in result:
        lat = re.search(latitude, str(i))
        lon = re.search(longitude, str(i))
        alt = re.search(altitude, str(i))
        if lat and lon and alt != None: #if it doesn't has a latitude or longitude, skips the line
            location_data.append({"latitude":float(lat.group(1)), 
            "longitude":float(lon.group(1)), 
            "altitude": float(alt.group(1)), 
            "speed": float(velo[k])
            })
            k+=1

    return location_data


