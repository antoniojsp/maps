from jinja2 import Template
from  tcx_parser_js import get_info_formatted
import sys
import matplotlib
from matplotlib import cm


def jinja_map(map:str, color:str, attr:str, name:str):
    '''
    (str,str,str,str) -> html file
    '''
    cmap = matplotlib.cm.get_cmap(color) # color scheme
    attributes = get_info_formatted(map) # choose between speed or altitude to clor the map
    '''
    Generates map of color according to the values
    '''
    mini = min(attributes[attr])
    maxi = max(attributes[attr])
    color = []
    for i in attributes[attr]:
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

    with open(name, 'w') as f:
        f.write(result)

if __name__ == "__main__":
    jinja_map(sys.argv[1], "rainbow", "altitude", "map.html")
