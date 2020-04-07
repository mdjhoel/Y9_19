# cvt_ont.py - file io application to read in latest covid19 data and Leaflet.js circles using string concatenation
# April 6, 2020: mhoel - original coding 

# Access data from: https://data.ontario.ca/dataset/confirmed-positive-cases-of-covid-19-in-ontario/resource/455fd63b-603d-4608-8216-7d8647f43350

# Read file in
fi = open("april6.csv","r")
fi.readline() # skip over first title line
datarows = fi.readlines()
fi.close()

# Write file out that will contain javascript and data
fo = open("leafont.txt","w")

# loop through all rows in the csv file and create a collated data object
data = {};
for line in datarows:
    templist = line.split(",")
    hunit = templist[5]
    lat = templist[8].strip()
    lon = templist[9].strip()
    curnum = 0
    if (data.get(hunit)):
        curnum = int(data[hunit].get('num'))
        curnum = curnum + 1
    data[hunit] = {"lat":lat,"lon":lon,"num": curnum}

count = 0 # count number of circles/health units
# go through data object
for hunit in data:
    lat = data[hunit]["lat"]
    lon = data[hunit]["lon"]
    num = data[hunit]["num"]
    count = count + 1
    
    # make radius of circle bigger for cartographic appeal
    numradius = int(num) * 50
    # string concatenate Leaflet code and data
    marker = "L.circle([" + lat + "," + lon + "],{color:'red',fillColor:'#f03',fillOpacity:0.5,radius:" + str(numradius) + "}).addTo(map).bindPopup('" + hunit +  " : " + str(num) + "')"
    # write to file
    fo.write(marker + "\n")

print(str(count) + " markers written out")
fo.close()
