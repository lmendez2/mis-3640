name = ["julian", "zach", "alex"]
scores = [95, 75, 85]


grades = {}  ##or can use dict() to create a dictionary
print(type(grades))

grades["zach"] = 75
print(grades)
print(grades["zach"]) ## the key is the name and the key now becomes the index

def histogram(s):
    d = dict()
    for c in s.lower(): ##converts letters to lower cases so that not case sensitive
        # if c not in d:
        #     d[c] = 1 ## if c is not in the dictionary we create one 
        # else:
        #     d[c] = d[c] + 1 ##if it does exist we add one to that key 
        d[c] = d.get(c,0) + 1  ## (c,0) assign zero if that key does not exist and add one if it does exist 
    return d

h = histogram('bookkeeper')
print(h)
print(sorted(h)) ##sorts and prints the word but doesnt return the count 
 

def print_hist():
    for c in h: 
        print(c, h[c]) ##h[c] dictionary name and the key 

print_hist()


# json_example = {
#    "results" : [
#       {
#          "address_components" : [
#             {
#                "long_name" : "231",
#                "short_name" : "231",
#                "types" : [ "street_number" ]
#             },
#             {
#                "long_name" : "Forest Street",
#                "short_name" : "Forest St",
#                "types" : [ "route" ]
#             },
#             {
#                "long_name" : "Babson Park",
#                "short_name" : "Babson Park",
#                "types" : [ "neighborhood", "political" ]
#             },
#             {
#                "long_name" : "Wellesley",
#                "short_name" : "Wellesley",
#                "types" : [ "locality", "political" ]
#             },
#             {
#                "long_name" : "Norfolk County",
#                "short_name" : "Norfolk County",
#                "types" : [ "administrative_area_level_2", "political" ]
#             },
#             {
#                "long_name" : "Massachusetts",
#                "short_name" : "MA",
#                "types" : [ "administrative_area_level_1", "political" ]
#             },
#             {
#                "long_name" : "United States",
#                "short_name" : "US",
#                "types" : [ "country", "political" ]
#             },
#             {
#                "long_name" : "02457",
#                "short_name" : "02457",
#                "types" : [ "postal_code" ]
#             },
#             {
#                "long_name" : "0310",
#                "short_name" : "0310",
#                "types" : [ "postal_code_suffix" ]
#             }
#          ],
#          "formatted_address" : "231 Forest St, Babson Park, MA 02457, USA",
#          "geometry" : {
#             "location" : {
#                "lat" : 42.2993708,
#                "lng" : -71.2659951
#             },
#             "location_type" : "ROOFTOP",
#             "viewport" : {
#                "northeast" : {
#                   "lat" : 42.3007197802915,
#                   "lng" : -71.26464611970849
#                },
#                "southwest" : {
#                   "lat" : 42.2980218197085,
#                   "lng" : -71.26734408029149
#                }
#             }
#          },
#          "place_id" : "ChIJ7xQZi0GB44kRiWrnmTgf904",
#          "types" : [ "establishment", "point_of_interest" ]
#       }
#    ],
#    "status" : "OK"
# }

# print(json_example["results"][0]['address_components'][5]['short_name'])
# print(len(json_example['results']))