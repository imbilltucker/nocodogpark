# Mark local NOCO dog parks

import folium

parks = [
  {"name": "Spring Canyon Dog Park", "loc": [40.548, -105.118]},
  {"name": "Soft Gold Dog Park", "loc": [40.601, -105.074]},
  {"name": "Fossil Creek Dog Park", "loc": [40.518, -105.072]}
]


def main() -> None:

    m = folium.Map(location=[40.56, -105.09], zoom_start=12)
    for p in parks:
      folium.Marker(p["loc"], popup=p["name"], icon=folium.Icon(color="green", icon="paw", prefix="fa")).add_to(m)

    m.save("noco_dog_parks.html")
    print("Map written to: noco_dog_parks.html")

