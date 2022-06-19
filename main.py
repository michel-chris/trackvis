#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chris Michel
"""

from functions import *

import os

# quick start guide for folium maps:
# https://python-visualization.github.io/folium/quickstart.html


dataPath = os.path.abspath('example')

downloadExample(dataPath)


# Use polyline if:
# - you have a low number of gnss points per distance
# - you need a more responsive map since you have a large number of tracks
# adapt color, weight (line thickness) and opacity to your liking
# (I suggest weight=2.5, opacity=0.2)

# folder path with all gpx tracks
fileList = [os.path.join(dataPath, f) for f in os.listdir(dataPath)]

# read all tracks and append to one variable
# tracks[i][j][0] == i-th track, j-th point, latitude
# tracks[i][j][1] == i-th track, j-th point, longitude
tracks = readGPX(fileList)

plotMap(tracks, vectorType = 'polyline', tiles = 'Stamen Terrain', outputFile = dataPath + '/city.html')


# Use heatmap if:
# - polyline looks ugly
# - you have normal point density (every 3 meters?)
# - you don't care about gaps in your lines
# - you have a powerful pc in case of a large number of tracks
# adapt radius and blur to your liking (I suggest radius=2, blur=3)


