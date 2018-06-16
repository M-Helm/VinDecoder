#!/usr/local/opt/python/bin/python2.7
"""Decode VINs from the NHTSA API as of 6/16/28."""
import urllib2
import json


class VinDecoder():
    """."""

    def __init__(self, vin_arr):
        """Initialize the decoder."""
        self.__decode(vin_arr)
        return None

    def __decode(self, arr):
        for v in arr:
            url = 'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/\
                %s?format=json' % v
            url = url.strip()
            url = url.replace(" ", "")
            res = urllib2.urlopen(url).read()
            obj = json.loads(res)
            if 'Results' in obj:
                o = obj['Results']
                for i in o:
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
                    % (v, year, make, model, disp, cyl)


if __name__ == "__main__":
    vins = ['5UXWX7C5*BA']
    decoder = VinDecoder(vins)
