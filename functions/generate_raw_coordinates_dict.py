def generate_raw_coordinates_dict(dict):
    maps_container = []

    for category, dictionary in dict['coordinates'].items():
        for item in dictionary:
            for place, coordinatespair in item.items():
                maps_container.append(coordinatespair)

    return maps_container