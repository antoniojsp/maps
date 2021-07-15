import matplotlib.pyplot as plt
from tcx_parser_js import *

attributes = get_info_formatted("paseo.tcx")

y1 = [i[1] for i in enumerate(attributes["speed"]) if i[0]%2 == 0 ]
x1 = [i for i in range(len(y1))]
minimum  = min(y1)


# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")



# naming the x axis
plt.xlabel('Route')
# naming the y axis
plt.ylabel('Speed')
# giving a title to my graph
plt.title('Speed from the route')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
