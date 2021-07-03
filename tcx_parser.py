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
    result = extract_data(tcx_file)
    location_data = []
    distancia_for_now = 0
    for i in result:
        lat = re.search(latitude, str(i))
        lon = re.search(longitude, str(i))
        alt = re.search(altitude, str(i))
        dis = re.search(distance, str(i))
        if alt != None: #if it doesn't has a latitude or longitude, skips the line
            # print("latitude",float(lat.group(1)), "longitude",float(lon.group(1)), "altitude", float(alt.group(1)))

            location_data.append({"latitude":float(lat.group(1)), "longitude":float(lon.group(1)) , "altitude": float(alt.group(1))})

        if dis != None: #if distance present, add to the last dict
            variation = abs(float(dis.group(1)) - distancia_for_now)
            append_to_end(location_data, "distance", variation)
            distancia_for_now = float(dis.group(1))
            speed = (variation*18)/float(5)
            append_to_end(location_data, "speed", speed)

    return location_data

# get_info_formatted("paseo3.tcx")
# print(*get_info_formatted("paseo3.tcx"), sep="\n")
