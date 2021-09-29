import json

infile = open('eq_data_1_day_m1.json','r')
outfile = open('readable_eq_data.json','w')

#this converts contents of the json file into a dictionary
eqdata = json.load(infile)      #eqdata is not a python dictionary

#dump contents into eqfile
json.dump(eqdata,outfile,indent=4)

#pull magnitude from readable_eq_data.json
print(len(eqdata["features"]))

list_of_eqs = eqdata["features"]    #this is a list of dictionaries (each dic is an earthquake)

mags = []
lats = []   #latitudes
lons = []   #longitudes


for eq in list_of_eqs:   #eq is a dictionary
    mag = eq["properties"]["mag"]
    lat = eq["geometry"]["coordinates"][0]
    lon = eq["geometry"]["coordinates"][1]
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)

print(mags)
print(lats)
print(lons)