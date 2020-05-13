# convert.py - file io application to read in latest covid19 data and spit out Leaflet.js circles using string concatenation
# March 24, 2020: mhoel - original coding 
# added geojson - https://github.com/datasets/geo-countries/tree/master/data

# Access data from: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
# Korea, South - Bahamas, The - Gambia, The : Must be manually fixed in the data (South Korea, Bahamas, Gambia) 

# Read file in
fi = open("03-22-2020.csv","r")
fi.readline() # skip over first title line
datarows = fi.readlines()
fi.close()

# loop through all rows in the csv file
provs = []
numdeaths = []
for line in datarows:
    templist = line.split(",")
    prov = templist[0].lower()
    country = templist[1].lower()
    confirmed = templist[3]
    deaths = templist[4]
    recover = templist[5]
    lat = templist[6]
    lon = templist[7]

    if (country == "canada"):
        provs.append(prov)
        numdeaths.append(deaths)

print(provs)
print(deaths)

import json

with open('canada_provinces.geojson') as f:
  data = json.load(f)

f.close()

for prov in data["features"]:
    name = prov["properties"]["name"].lower()
    try:
        i = provs.index(name)
        prov["properties"]["deaths"] = numdeaths[i]
        print(prov["properties"])
    except:
        print(name + " not found")
        prov["properties"]["deaths"] =0

with open('cloropleth.geojson', 'w') as json_file:
  json.dump(data, json_file)

json_file.close()

