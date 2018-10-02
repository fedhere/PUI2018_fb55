from __future__ import print_function
__author__ = 'fb55'

import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

DEBUG = True  # Change to True to print debug statements


def get_jsonparsed_data(url):
    """
    from http://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urllib.urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


if __name__ == '__main__':
    """Outputs the distance to the next stop for all MTA busses currently 
running for a given bus line.

    Arguments: 
        MTA key
        Bus line
        output file

    Output:
        CSV file
    """

    if not len(sys.argv) == 4:
        print('''USAGE:
        $python get_bus_line.py <MTA_KEY> <BUS_LINE> <outfile.csv>''')
        sys.exit()

    key, bus_line, outfile = sys.argv[1:]
    of = open(outfile, 'w')

    if DEBUG:
        print('#BUS LINE:', bus_line)

    print('Latitude,Longitude,Stop Name,Stop Status', file=of)

    bus_url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + key + \
               '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
    if DEBUG:
        print("URL of the bus", bus_url)

    # queries the url for json format bus data
    busdata = get_jsonparsed_data(bus_url)

    # counting the number of active busses
    nbusses = len(busdata['Siri']['ServiceDelivery']\
                  ['VehicleMonitoringDelivery'][0]['VehicleActivity'])

    if DEBUG:
        print('Number of Active Buses : %d' % nbusses)

    # extracting and printing info for each bus
    for i in range(nbusses):
        busloc = busdata['Siri']['ServiceDelivery']\
                 ['VehicleMonitoringDelivery'][0]\
                 ['VehicleActivity'][i]['MonitoredVehicleJourney']\
                 ['VehicleLocation']
        try:
            next_stop = busdata['Siri']['ServiceDelivery']\
                        ['VehicleMonitoringDelivery'][0]\
                        ['VehicleActivity'][i]['MonitoredVehicleJourney']\
                        ['OnwardCalls']['OnwardCall']
        except KeyError:
            next_stop = []

        if DEBUG:
            print(next_stop)
            print('Bus %d is at latitude %f and longitude %f' % \
                  (i, busloc['Latitude'], busloc['Longitude']))

        print("%f,%f," % (busloc['Latitude'], busloc['Longitude']),
              end='', file=of)

        # dealing with missing values
        if len(next_stop) < 1:
            print('N/A', 'N/A', file=of)
        else:
            print("%s,%s" % (next_stop[0]['StopPointName'],
                              next_stop[0]['Extensions']['Distances']\
                             ['PresentableDistance']),
                   file=of)
