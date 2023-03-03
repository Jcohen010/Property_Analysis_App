def generate_folium_map(coordinates_df, coordinates_dict):
    import folium
    
    map = folium.Map(location=[coordinates_df['lat'].mean(), coordinates_df['lon'].mean()], 
                 zoom_start=10, control_scale=True)

    for item in coordinates_dict['coordinates']:
        for place, coordinate_pair in item.items():
            iframe = folium.IFrame(f"{place}")
            popup = folium.Popup(iframe, min_width=100, max_width=100)

            folium.Marker(location=[coordinate_pair['lat'],coordinate_pair['lon']], popup = popup, c=place).add_to(map)

    return map
