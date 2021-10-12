import json


infile = open("US_fires_9_14.json", "r")

fire_data = json.load(infile)

#create empty lists
lats,lons,bright = [],[],[]
 
for f in fire_data:
    if f['brightness'] > 450:
        lat = f['latitude']
        lon = f['longitude']
        brightness = f['brightness']
        lats.append(lat)
        lons.append(lon)
        bright.append(brightness)



print(lats[:5])
print(lons[:5])
print(bright[:5])

from plotly import offline
from plotly.graph_objs import Scattergeo, Layout

data = [{
    "type":"Scattergeo",
    "lon":lons,
    "lat":lats,
    "text":bright,
    "marker":{
        "size":[.05*br for br in bright],
        "color":bright,
        "colorscale":"Viridis",
        "reversescale":True,
        "colorbar":{"title":"brightness"}
    }
}]


my_layout = Layout(title = "US Fires - 9/14/2020 thorugh 9/20/2020")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="globalfiresgreaterthan450_9_14.html")
