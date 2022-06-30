# Visualisation of gpx tracks with folium

Quick start guide for folium maps: [python-visualization.github.io](https://python-visualization.github.io/folium/quickstart.html)

## Plot tracks as polylines
Use polyline if:
- you have a low number of gnss points per distance
- you need a more responsive map since you have a large number of tracks

adapt color, weight (line thickness) and opacity to your liking (in functions.py)
suggestion: weight = 2.5, opacity = 0.2

![Example Lines](https://github.com/michel-chris/trackvis/blob/master/exampleLines.jpg)

## Plot tracks/points as a heatmap
Use heatmap if:
- you have many overlapping tracks, which cannot be displayed by polyline e.g. opacity = 0.2 --> max. number of lines is 5
- you have sufficiently high point density (every 3 meters??)
- you don't care about gaps in your lines
- you don't care about unresponsive maps or have a powerful pc (in the case of a large number of tracks)

adapt radius and blur to your liking (in functions.py)
suggestion: radius = 2, blur = 3

![Example Heat](https://github.com/michel-chris/trackvis/blob/master/exampleHeat.jpg)