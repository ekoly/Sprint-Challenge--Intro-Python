# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and lonitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

import csv

class City:

    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        """
            @returns: str
        """
        return f"<City name=\"{self.name}\" lat={self.lat} lon={self.lon}>"

def cityreader():
    """
        Expects a csv file with the following rows:
        city,state_name,county_name,lat,lng,population,density,timezone,zips
    """
    cities = []
    with open("cities.csv", "r") as f:
        csv_reader = csv.reader(f)
        # skip first row
        next(csv_reader)
        for row in csv_reader:
            cities.append(City(row[0], float(row[3]), float(row[4])))

    return cities

cities = cityreader()

# Print the list of cities (name, lat, lon), 1 record per line.
if __name__ == "__main__":
    for c in cities:
        print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and lonitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# lonitude values as parameters to the `cityreader_stretch` function, alon
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and lonitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    """
        Returns a list of cities boxed in by (lat1, lon1), (lat2, lon2).

        @type lat1: float
        @type lon1: float
        @type lat2: float
        @type lon2: float
        @type cties: List[City]

        @rtype: List[City]
    """
    right_lon = max([lon1, lon2])
    left_lon = min([lon1, lon2])
    upper_lat = max([lat1, lat2])
    lower_lat = min([lat1, lat2])

    contained_cities = [c for c in cities if left_lon <= c.lon and c.lon <= right_lon and lower_lat <= c.lat and c.lat <= upper_lat]
    return contained_cities

if __name__ == "__main__":
    while True:

        # break when the user enters invalid input

        user_input1 = input("Enter lat1,lon1: ")
        user_input1_split = user_input1.split(",")
        if len(user_input1_split) != 2:
            break
        user_input2 = input("Enter lat2,lon2: ")
        user_input2_split = user_input2.split(",")
        if len(user_input2_split) != 2:
            break

        try:
            lat1 = float(user_input1_split[0])
            lat2 = float(user_input2_split[0])
            lon1 = float(user_input1_split[1])
            lon2 = float(user_input2_split[1])
        except:
            break

        contained_cities = cityreader_stretch(lat1, lon1, lat2, lon2, cities=cities)
        for city in contained_cities:
            print(f"{city.name}: ({city.lat},{city.lon})")
