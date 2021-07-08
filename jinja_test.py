from jinja2 import Template
from  tcx_parser_js import *
import sys
import matplotlib
from matplotlib import cm

cmap = matplotlib.cm.get_cmap("rainbow") # color system
attributes = get_info_formatted("paseo.tcx", "rainbow") # choose between speed or altitude to clor the map

'''
Generates map of color according to the values
'''
mini = min(attributes["speed"])
maxi = max(attributes["speed"])    
color = []
for i in attributes["speed"]:
    normalize = (i-mini)/(maxi-mini) #select color
    rgba = cmap(normalize) # pass to cmap 
    color.append(matplotlib.colors.rgb2hex(rgba))

'''
Gets the middle point to center the map
'''
middle_lat = (max(attributes["latitude"])+min(attributes["latitude"]))/2
middle_lon = (max(attributes["longitude"])+min(attributes["longitude"]))/2

with open('template.html.jinja') as f:
    tmpl = Template(f.read())

result = tmpl.render(
    latitude = attributes["latitude"],
    longitude = attributes["longitude"],
    color = color,
    lat_middle = middle_lat,
    long_middle = middle_lon
)

with open("map.html", 'w') as f:
    f.write(result)