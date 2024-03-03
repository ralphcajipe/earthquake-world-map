# Update the 'data' dictionary with the marker settings
data['marker'] = {
    'size': scaled_mags,
    'color': scaled_mags,  # Use the magnitude values as the marker color
    'colorscale': 'viridis',  # Use the Viridis color scale
    'reversescale': True,  # Reverse the color scale
    'colorbar': {'title': 'Magnitude', 'len': 0.5, 'thickness': 20, 'lenmode': 'fraction', 'len': 0.5, 'thickness': 20, 'cmin': min(mags), 'cmax': max(mags)},  # Add a colorbar with title 'Magnitude'
}

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 
       'layout': my_layout}

# Render HTML file
offline.plot(fig, filename='global_earthquakes.html')