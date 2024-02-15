import json

filename = "data/eq_data_1_day_m4_5.json"

# Open the JSON file with utf-8 encoding
with open(filename, "r", encoding="utf-8") as f:
    all_eq_data = json.load(f)

# Create a new JSON file with formatted data
readable_filename = "data/readable_eq_data.json"
with open(readable_filename, "w", encoding="utf-8") as f:
    # Dump the Python object into the new JSON file, with ASCII characters ensured and indented by 4 spaces
    json.dump(all_eq_data, f, ensure_ascii=False, indent=4)

# Open the new JSON file and display the data
with open(readable_filename, "r", encoding="utf-8") as f:
    readable_eq_data = json.load(f)
    print(readable_eq_data)

# Extract the earthquake magnitude data
all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))

mags, lons, lats = [], [], []

# Extract the magnitude, location data (longitude and latitude) of each earthquake
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Display the first 10 magnitudes, first 5 longitudes, and first 5 latitudes
print(f"Magnitudes: {mags[:10]}")
print(f"Longitudes (x): {lons[:5]}")
print(f"Latitudes (y): {lats[:5]}")

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Map the earthquakes
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 
       'layout': my_layout}

# Render HTML fule
offline.plot(fig, filename='global_earthquakes.html')

