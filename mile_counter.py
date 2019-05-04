import csv

from haversine import haversine


def get_distance(file):
    """
        Returns distance in miles between 2 GPS coordinates from a CSV file
        Latitude must be labeled "Latitude" and Longitude must be labeled "Longitude"
    """
    lat_list = []
    long_list = []
    with open(file) as trailer_file:
        file_reader = csv.DictReader(trailer_file, delimiter=",")
        for rows in file_reader:
            if rows['Latitude'] and rows['Longitude']:
                lat_list.append(rows['Latitude'])
                long_list.append(rows['Longitude'])
    x = 0
    distances_total = 0
    while x < len(lat_list)-1:
        start = (float(lat_list[x]), float(long_list[x]))
        stop = (float(lat_list[x+1]), float(long_list[x+1]))
        y = haversine(start, stop, unit='mi')
        distances_total += y
        x += 1
    return round(distances_total, 0)

