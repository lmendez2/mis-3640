import urllib.request   # urlencode function
import json

from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"

url = "https://maps.googleapis.com/maps/api/geocode/json?address=231+Forest+Street,+Wellesley,+MA+02457,+USA&key=AIzaSyDA1865acKD_jP_65hIQ24lo1LmUjHiRHY"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """

    if ' ' in place_name:
        while ' ' in place_name:
            x = []
            for i in place_name:
                x.append(i)
            while ' ' in x:
                x[x.index(' ')] = '%20'
            place_name = ''.join(x)

    url = GMAPS_BASE_URL + '?address=' + place_name
    place_json = get_json(url)
    lat = place_json['results'][0]['geometry']['location']['lat']
    lon = place_json['results'][0]['geometry']['location']['lng']
    return (lat, lon)
        

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API in 'MBTA-realtime API v2 Documentation'.
    """
    MBTA_url = MBTA_BASE_URL + '?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat='+str(latitude)+'&lon='+str(longitude)+'&format=json'
    response_data_mbta = get_json(MBTA_url)

    if response_data_mbta['stop'] != []:
        x = 0
        station_name = response_data_mbta['stop'][x]['parent_station_name']
        distance = response_data_mbta['stop'][x]['distance']
        while station_name == '':
            x += 1
            station_name = response_data_mbta['stop'][x]['parent_station_name']
            distance = response_data_mbta['stop'][x]['distance']
        return station_name, distance

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat, lon = get_lat_long(place_name)
    return get_nearest_station(lat, lon)



def main():
    place = input()

    print(find_stop_near(place))


if __name__ == '__main__':
    main()