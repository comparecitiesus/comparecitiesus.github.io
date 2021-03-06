import cities
import fbireport
import sbareport
import airports
import json
import climatereport

REPORT_PATH = "../cities/%s.json"

def generateAll():
    for currentCity in cities.MAJOR_CITIES:
        city = currentCity["name"]
        state = currentCity["state"]

        report = {}

        try:
            air  = airports.loadCity(city, state) 
            report.update((k, v) for k, v in air.iteritems() if v is not None)
        except LookupError:
            print "air", city, state

        try:
            fbi = fbireport.loadCity(city, state) 
            report.update((k, v) for k, v in fbi.iteritems() if v is not None)
        except LookupError:
            print "fbi", city, state

        try:
            sba = sbareport.loadCity(city, state)
            report.update((k, v) for k, v in sba.iteritems() if v is not None)
        except LookupError:
            print "sba", city, state

        try:
            climate = climatereport.loadCity(report)
            report.update((k, v) for k, v in climate.iteritems() if v is not None)
        except LookupError:
            print "climate", city, state

        if report:
            report["id"] = currentCity["id"]
            report["name"] = city
            report["state"] = state
            report["full_name"] = "%s, %s" % (city, state) 
            filename = REPORT_PATH % report["id"]
            cityFile = open(filename, "w")
            json.dump(report, cityFile)

if __name__ == "__main__":
    generateAll()
