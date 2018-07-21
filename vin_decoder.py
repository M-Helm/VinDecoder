#!/usr/local/opt/python/bin/python2.7
"""Decode VINs from the NHTSA API as of 6/16/28."""
import urllib2
import json


class VinDecoder():
    """Super simple module to decode VINs using the NHTSA API."""

    def __init__(self):
        """Initialize the decoder."""
        return None

    def decode(self, vin):
        """Decode the given VIN."""
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/\
            %s?format=json' % vin
        url = url.strip()
        url = url.replace(" ", "")
        res = urllib2.urlopen(url).read()
        obj = json.loads(res)
        if 'Results' in obj:
            o = obj['Results']
            for i in o:
                if 'Variable' not in i:
                    return None
                if i['Variable'] == 'Model Year':
                    year = i['Value']
                if i['Variable'] == 'Make':
                    make = i['Value']
                if i['Variable'] == 'Model':
                    model = i['Value']
                if i['Variable'] == 'Displacement (L)':
                    disp = i['Value']
                if i['Variable'] == 'Engine Number of Cylinders':
                    cyl = i['Value']
            print "vin: %s %s %s %s, Disp: %s Cyl: %s" \
                % (vin, year, make, model, disp, cyl)
            return {'vin': vin, 'year': year, 'make': make,
                    'model': model, 'disp': disp, 'cyl': cyl}


if __name__ == "__main__":
    vd = VinDecoder()
    vin = '1GNGK56K19R227051'
    d = vd.decode(vin)
    print d
