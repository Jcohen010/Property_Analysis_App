def generate_raw_coordinates_dict(dict):
    maps_container = []

    for item in dict['coordinates']:
        for place in item.values():
            maps_container.append(place)

    return maps_container