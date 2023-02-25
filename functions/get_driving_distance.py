def get_driving_distance(dict):
    import json
    import requests
    import pandas as pd
    from datetime import timedelta
    import datetime

    distance_list = []

    for coord in dict['coordinates']:
        for place in coord:
            if place == 'property':
                property = place
                for place in coord.values():
                    propertylat = place['lat']
                    propertylon = place['lon']

    for coord in dict['coordinates']:
        for place in coord:
            if place != 'property':
                person = place
                for place in coord.values():
                    lat = place['lat']
                    lon = place['lon']

                    r = requests.get(f"http://router.project-osrm.org/route/v1/car/{propertylon},{propertylat};{lon},{lat}?overview=false""")
                    # then you load the response using the json libray
                    # by default you get only one alternative so you access 0-th element of the `routes`
                    routes = json.loads(r.content)
                    route_1 = routes.get("routes")[0]

                    distance = int(route_1["duration"]/60)

                    distance_list.append(f"{person}: {distance} Minutes")

    return distance_list