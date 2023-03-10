def generate_folium_map(coordinates_df, coordinates_dict):
    import folium
    
    map = folium.Map(location=[coordinates_df['lat'].mean(), coordinates_df['lon'].mean()], 
                 zoom_start=10, control_scale=True)

    for category, dict in coordinates_dict['coordinates'].items():
        for item in dict:
            for place, coordinate_pair in item.items():
                iframe = folium.IFrame(f"{place}")
                popup = folium.Popup(iframe, min_width=100, max_width=100)

                if category == 'home':
                    folium.Marker(location=[coordinate_pair['lat'],coordinate_pair['lon']], popup = popup, c=place, icon=folium.Icon(color='purple')).add_to(map)
                elif category == 'work':
                    folium.Marker(location=[coordinate_pair['lat'],coordinate_pair['lon']], popup = popup, c=place, icon=folium.Icon(color='blue')).add_to(map)
                elif category == 'property':
                    folium.Marker(location=[coordinate_pair['lat'],coordinate_pair['lon']], popup = popup, c=place, icon=folium.Icon(color='green')).add_to(map)
                    
    return map
