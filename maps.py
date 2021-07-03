# api_key = "AIzaSyAPxKpFtItuUxkuyelfFyFTJbR2bBb-JsY"
from tcx_parser import *
import gmplot
import matplotlib
from matplotlib import cm

def plot_route(file:str, color:str, attribute:str, output_name:str):
    cmap = matplotlib.cm.get_cmap('Reds')

    # Create the map plotter:
    apikey = "AIzaSyAPxKpFtItuUxkuyelfFyFTJbR2bBb-JsY" # (your API key here)
    gmap = gmplot.GoogleMapPlotter(44.0521, -123.0868, 14, apikey=apikey)

    data = get_info_formatted(file)

    sortie = sorted(data, key=lambda x: x[attribute], reverse=True)

    max = sortie[1][attribute]
    min = sortie[-1][attribute]

    for i in range(len(data)-1):
        path1 = zip(*[ (data[i]["latitude"],data[i]["longitude"]),
                       (data[i+1]["latitude"],data[i+1]["longitude"])
                     ])

        normalize = (data[i][attribute]-min)/(max-min) #select color
        rgba = cmap(normalize)
        gmap.plot(*path1, edge_width=7, color=matplotlib.colors.rgb2hex(rgba))
        i+=1

    # Draw the map:
    gmap.draw(output_name)

plot_route("paseo.tcx", "Reds", "speed", "map.html")
