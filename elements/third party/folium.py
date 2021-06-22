
import streamlit as st

def title():
    return 'Folium'

def run():

    st.write('Here is an example of a map with geojson data. In order to use it, you need to identify a geojson data source ([here is one for France](https://github.com/gregoiredavid/france-geojson)). In order to use this code, first download the [departements.json](https://raw.githubusercontent.com/gmanchon/streamlit/master/data/departements.json) and [lewagon_cities.csv](https://raw.githubusercontent.com/gmanchon/streamlit/master/data/lewagon_cities.csv) files and store them in a `data` directory')

    with st.echo():

        from streamlit_folium import folium_static

        import folium

        import os

        import pandas as pd

        m = folium.Map(location=[47, 1], zoom_start=6)

        geojson_path = os.path.join("data", "departements.json")
        cities_path = os.path.join("data", "lewagon_cities.csv")

        for _, city in pd.read_csv(cities_path).iterrows():

            folium.Marker(
                location=[city.lat, city.lon],
                popup=city.city,
                icon=folium.Icon(color="red", icon="info-sign"),
            ).add_to(m)

        def color_function(feat):
            return "red" if int(feat["properties"]["code"][:1]) < 5 else "blue"

        folium.GeoJson(
            geojson_path,
            name="geojson",
            style_function=lambda feat: {
                "weight": 1,
                "color": "black",
                "opacity": 0.25,
                "fillColor": color_function(feat),
                "fillOpacity": 0.25,
            },
            highlight_function=lambda feat: {
                "fillColor": color_function(feat),
                "fillOpacity": .5,
            },
            tooltip=folium.GeoJsonTooltip(
                fields=['code', 'nom'],
                aliases=['Code', 'Name'],
                localize=True
            ),
        ).add_to(m)

        folium_static(m)
