from tcx_parser import *
import gmplot
import matplotlib
from matplotlib import cm
# main.py
import sys
import configparser#import the key from secret file
config = configparser.ConfigParser()
config.read("credentials.ini")
API_KEY = config["DEFAULT"]["KEY_FLASH"]

def max_min(data:list, attr:str):
    '''
    (list, str) -> (number, number)

    Gets a dictionary and a key. Then use that key to loop up values and return the minumum and maximum values.
    '''
    sortie = sorted(data, key=lambda x: x[attr], reverse=True)
    max = sortie[0][attr]
    min = sortie[-1][attr]

    return min, max

def plot_route(file:str, color:str, attribute:str, output_name:str):
    cmap = matplotlib.cm.get_cmap(color)

    # Create the map plotter:
    apikey = API_KEY # (your API key here)
    data = get_info_formatted(file)

    #middle point to center the map
    lat_min, lat_max = max_min(data, "latitude")
    lon_min, lon_max = max_min(data, "longitude")
    middle_point_lat = (lat_min+lat_max)/2
    middle_point_lon= (lon_min+lon_max)/2

    gmap = gmplot.GoogleMapPlotter(middle_point_lat, middle_point_lon, 14, apikey=apikey)

    min, max = max_min(data, attribute)
    # print(min, max)
    for i in range(len(data)-1):
        path1 = zip(*[ (data[i]["latitude"],data[i]["longitude"]),
                       (data[i+1]["latitude"],data[i+1]["longitude"])
                     ])

        normalize = (data[i][attribute]-min)/(max-min) #select color
        rgba = cmap(normalize) # pass to cmap 
        gmap.plot(*path1, edge_width=5, color=matplotlib.colors.rgb2hex(rgba)) # plot 

    # Draw the map:
    gmap.draw(output_name)


if __name__ == "__main__":
    plot_route(sys.argv[1], "rainbow", "altitude", "map.html")
