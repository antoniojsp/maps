# api_key = "AIzaSyAPxKpFtItuUxkuyelfFyFTJbR2bBb-JsY"
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

def plot_route(file:str, color:str, attribute:str, output_name:str):
    cmap = matplotlib.cm.get_cmap(color)

    # Create the map plotter:
    apikey = API_KEY # (your API key here)
    gmap = gmplot.GoogleMapPlotter(44.0521, -123.0868, 14, apikey=apikey)

    data = get_info_formatted(file)


    distance = [i[attribute] for i in data]




    sortie = sorted(data, key=lambda x: x[attribute], reverse=True)

    max = sortie[1][attribute]
    min = sortie[-1][attribute]

    for i in range(len(data)-1):
        path1 = zip(*[ (data[i]["latitude"],data[i]["longitude"]),
                       (data[i+1]["latitude"],data[i+1]["longitude"])
                     ])

        normalize = (data[i][attribute]-min)/(max-min) #select color
        rgba = cmap(normalize)
        gmap.plot(*path1, edge_width=5, color=matplotlib.colors.rgb2hex(rgba))
        i+=1

    # Draw the map:
    gmap.draw(output_name)


if __name__ == "__main__":
    plot_route(sys.argv[1], "rainbow", "altitude", "map.html")
