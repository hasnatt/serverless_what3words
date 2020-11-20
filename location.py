import requests
from geopy.geocoders import Nominatim, GoogleV3
import what3words
import json
import config

# get your key from https://developer.what3words.com/public-api
key = config.API_KEY

class Location:
    def __init__(self, w1, w2,w3):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3


    def get_words_list(self):
       l = [self.w1, self.w2, self.w3]
       return(l)


    def get_json(self):
        # get the words list
        words = self.get_words_list()
        #  print(words)
        x = (f'{words[0]}.{words[1]}.{words[2]}')
        url = 'https://api.what3words.com/v3/convert-to-coordinates?words='+ x +'&key=' + key
        try:
            response = requests.request("GET", url)
            body = json.loads(response.content)
        except Exception:
            print("Error:  request for words: " + x )
        return(body)

    def get_lat_long(self):
        body = self.get_json()
        lng = body['coordinates']['lng']
        lat = body['coordinates']['lat']
        return(lat,lng)


    def get_nearestplace(self):
        body = self.get_json()
        np = body['nearestPlace']
        return(np)

    def find_address(self):
        tup = self.get_lat_long()
        lat = tup[0]
        lng = tup[1]

        geolocator = Nominatim(user_agent="3words")
        location = geolocator.reverse(f'{lat},{lng}')
        return(location.address)

    def get_directions(self):
        tup = self.get_lat_long()
        lat = tup[0]
        lng = tup[1]

        goog_maps = (f'https://www.google.com/maps/dir/?api=1&destination={lat},{lng}')
        # https://www.google.com/maps/dir/?api=1&destination={lat},{lng}
        return(goog_maps)



# address = Location('prom','cape','pump')
# print(address.get_json())
