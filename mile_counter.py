from math import cos, asin, sqrt
import csv


def distance(lat1, lon1, lat2, lon2):
    """Returns distance in miles"""
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))/1.609


def get_distance(file):
    lat_list = []
    long_list = []
    with open(file) as trailer_file:
        file_reader = csv.DictReader(trailer_file, delimiter=",")
        for rows in file_reader:
            if rows['latitude'] and rows['longitude']:
                lat_list.append(rows['latitude'])
                long_list.append(rows['longitude'])
    x = 0
    distances_total = 0
    while x < len(lat_list)-1:
        y = distance(float(lat_list[x]), float(long_list[x]), float(lat_list[x+1]), float(long_list[x+1]))
        distances_total += y
        x += 1
    return distances_total

