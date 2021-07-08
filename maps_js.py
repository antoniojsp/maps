from  tcx_parser_js import *

lat, lon, color = get_info_formatted("paseo1.tcx", "rainbow")

middle_lat = (max(lat)+min(lat))/2
middle_lon = (max(lon)+min(lon))/2

js_fn = 'function initialize() { \n \
        var map = new google.maps.Map(document.getElementById("map_canvas"), \n{ \
            zoom: 14, \
            center: new google.maps.LatLng('+str(middle_lat)+', '+ str(middle_lon) +')\
        });\n \
        \
        var  lat =' +  str(lat) +'; \n\
        var  lon =' +  str(lon) +'; \n\
        var  color =' +  str(color) +'; \n\
        \
        for(var i = 0; i < lat.length; i++) {\
            new google.maps.Polyline({ \n\
                clickable: true, \n\
                geodesic: true,\n \
                strokeColor: color[i], \n\
                strokeOpacity: 1.000000, \n\
                strokeWeight: 5, \n\
                map: map, \n\
                path: [ \n\
                    new google.maps.LatLng(lat[i], lon[i]), \n\
                    new google.maps.LatLng(lat[i+1], lon[i+1]) \n\
                ] \n\
        }) }; \n\
    }'

first =  '<html> \
<head> \
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" /> \
<meta http-equiv="content-type" content="text/html; charset=UTF-8" /> \
<title>Google Maps - gmplot</title> \
<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?libraries=visualization&key=AIzaSyCW08x5zYibLbXKKoMvZE6TK8DFGjCrobw"></script> \
<script type="text/javascript">' + js_fn + '</script> \
</head> \
<body style="margin:0px; padding:0px;" onload="initialize()"> \
    <div id="map_canvas" style="width: 100%; height: 100%;" /> \
</body> \
</html>'

f = open("demo.html", "w")
f.write("")
f.write(first)
f.close()

