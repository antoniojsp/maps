from  tcx_parser_js import *
import sys
import matplotlib
from matplotlib import cm

def map_js(map:str, color:str, attr:str, name:str):
    cmap = matplotlib.cm.get_cmap(color) # color system
    attributes = get_info_formatted(map, color) # choose between speed or altitude to clor the map

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

    '''
    Javascript function to create a route
    '''
    js_fn = 'function initialize() { \n \
            var map = new google.maps.Map(document.getElementById("map_canvas"), \n{ \
                zoom: 14, \
                center: new google.maps.LatLng('+str(middle_lat)+', '+ str(middle_lon) +')\
            });\n \
            \
            var  lat =' +  str(attributes["latitude"]) +'; \n\
            var  lon =' +  str(attributes["longitude"]) +'; \n\
            var  attr =' +  str(color) +'; \n\
            \
            for(var i = 0; i < lat.length; i++) {\
                new google.maps.Polyline({ \n\
                    clickable: true, \n\
                    geodesic: true,\n \
                    strokeColor: attr[i], \n\
                    strokeOpacity: 1.000000, \n\
                    strokeWeight: 5, \n\
                    map: map, \n\
                    path: [ \n\
                        new google.maps.LatLng(lat[i], lon[i]), \n\
                        new google.maps.LatLng(lat[i+1], lon[i+1]) \n\
                    ] \n\
            }) }; \n\
        }'

    '''
    WEBPAGE OF THE MAP
    '''
    result =  '<html> \n \
    <head> \n\
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" /> \n\
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> \n\
    <title>Google Maps - gmplot</title> \n\
    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?libraries=visualization&key=AIzaSyCW08x5zYibLbXKKoMvZE6TK8DFGjCrobw">\n \
    </script> \
    <script type="text/javascript">' + js_fn + '</script>\n \
    </head>\n \
    <body style="margin:0px; padding:0px;" onload="initialize()"> \n\
        <div id="map_canvas" style="width: 100%; height: 100%;" /> \n\
    </body> \n\
    </html>'

    with open(name, 'w') as f:
        f.write(result)

if __name__ == "__main__":
    map_js(sys.argv[1], "Blues", "altitude", "map.html")



