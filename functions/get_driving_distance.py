def get_driving_distance(dict):
    import json
    import requests
    import pandas as pd
    from datetime import timedelta
    import datetime
    global propertylat, propertylon

    distance_list = []

    for category, dictionary in dict['coordinates'].items():
        for item in dictionary:
            for place, coordinatepair in item.items():
                if place == 'property':
                    property = place
                propertylat = coordinatepair['lat']
                propertylon = coordinatepair['lon']

    for category, dictionary in dict['coordinates'].items():
        for item in dictionary:
            for place, coordinatepair in item.items():
                if place != 'property':
                    person = place
                lat = coordinatepair['lat']
                lon = coordinatepair['lon']

                r = requests.get(f"http://router.project-osrm.org/route/v1/car/{propertylon},{propertylat};{lon},{lat}?overview=false""")
                # then you load the response using the json libray
                # by default you get only one alternative so you access 0-th element of the `routes`
                routes = json.loads(r.content)
                route_1 = routes.get("routes")[0]

                distance = int(route_1["duration"]/60)

                distance_list.append(f"{person}: {distance} Mins")

    return distance_list
