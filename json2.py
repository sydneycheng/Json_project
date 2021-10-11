import json

infile = open('eq_data_30_day_m1.json','r')
outfile = open('readable_eq_data.json','w')

#this converts contents of the json file into a dictionary
eqdata = json.load(infile)      #eqdata is not a python dictionary

#dump contents into eqfile
json.dump(eqdata,outfile,indent=4)

#pull magnitude from readable_eq_data.json
print(len(eqdata["features"]))

list_of_eqs = eqdata["features"]    #this is a list of dictionaries (each dic is an earthquake)

mags, lats, lons, hover_texts = [],[],[],[]


for eq in list_of_eqs:   #eq is a dictionary
    mag = eq["properties"]["mag"]
    lat = eq["geometry"]["coordinates"][1]
    lon = eq["geometry"]["coordinates"][0]
    title = eq["properties"]["title"]
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)
    hover_texts.append(title)

print(mags[:5])
print(lats[:5])
print(lons[:5])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#data = [Scattergeo(lon=lons, lat=lats)] #the orange (lon,lat) are arguments; lons and lats are lists

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*m for m in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    }

}]


my_layout = Layout(title="Global Earthquakes 30 Day")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="globalearthquakes30day.html")
