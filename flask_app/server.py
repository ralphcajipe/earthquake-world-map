from flask import Flask, send_from_directory
import json
from plotly.graph_objs import Layout
from plotly import offline

app = Flask(__name__, static_url_path="")


@app.route("/")
def home():
    filename = "data/eq_data_1_day_m4_5.json"
    with open(filename, "r", encoding="utf-8") as f:
        all_eq_data = json.load(f)

    all_eq_dicts = all_eq_data["features"]

    mags, lons, lats, hover_texts = [], [], [], []
    for eq_dict in all_eq_dicts:
        mag = eq_dict["properties"]["mag"]
        lon = eq_dict["geometry"]["coordinates"][0]
        lat = eq_dict["geometry"]["coordinates"][1]
        title = eq_dict["properties"]["title"]
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(title)

    data = {"type": "scattergeo", "lon": lons, "lat": lats, "text": hover_texts}
    scale_factor = 5
    scaled_mags = [mag * scale_factor for mag in mags]

    data["marker"] = {
        "size": scaled_mags,
        "color": mags,
        "colorscale": "viridis",
        "reversescale": True,
        "colorbar": {"title": "Magnitude", "len": 0.5, "thickness": 20},
    }

    my_layout = Layout(
        title={"text": "Global Earthquakes", "x": 0.5},
        annotations=[
            {
                "text": "The visualization includes data for all earthquakes with a magnitude M4.5 or greater that took place in the last 24 hours (as of Feb 5, 2024).",
                "showarrow": False,
                "xref": "paper",
                "yref": "paper",
                "x": 0.5,
                "y": 1.05,
                "xanchor": "center",
                "yanchor": "top",
                "font": {"size": 12},
            },
            {
                "text": "Created by Stephen Camilon and Ralph Cajipe",
                "showarrow": False,
                "xref": "paper",
                "yref": "paper",
                "x": 0.5,
                "y": -0.1,
                "xanchor": "center",
                "yanchor": "top",
                "font": {"size": 12},
            },
        ],
    )
    fig = {"data": data, "layout": my_layout}
    offline.plot(fig, filename="static/global_earthquakes.html")

    return send_from_directory("static", "global_earthquakes.html")


if __name__ == "__main__":
    app.run(debug=True)
