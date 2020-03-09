import requests as rq
import json
import csv
import numpy as np

def buildurl(Station):
    Url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+ Station + '+Subway+Station&key=AIzaSyDtVzseEoY34Fu6g-3AzhTyBQTd13CUfTM'
    return Url


def getlocationval(Station):
    response = rq.get(buildurl(Station))
    dictionary = json.loads(response.text)
    return dictionary['results'][0]['geometry']['location']


def buildlistofstations(referenceFile, stationlist):
    for line in referenceFile:
        stationlist.append(line[4])
    del stationlist[0]
    arry = np.array(stationlist)
    return np.unique(arry)


ReferenceFile = open("data/AllCleanDataFrame.csv", 'r')
reference = csv.reader(ReferenceFile)

#Write the Station Names and Station Locations to wfile
wfile = open('data/StationGEOLocations.csv', mode='w')
writer = csv.writer(wfile)
stationlist = []

UniqueStationsNames = buildlistofstations(reference, stationlist)

HeaderList = ['Latitude', 'Longitude', 'StationName']
writer.writerow(HeaderList)
i = 0
for Station in UniqueStationsNames:
    i += 1
    print(str((i/len(UniqueStationsNames))*100) + '% Done')
    locationDict = getlocationval(Station)
    locationDict.update({'station': Station})
    writer.writerow(locationDict.values())

#This code could be made better by checking subway station tags in the location file to make sure the
#The recorded location is actually coming from a station