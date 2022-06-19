#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chris Michel
"""

from functions import *

import os


'''
TODO:
- write readme
- only download example files on first run
- add other colormaps
- add configuration file (yaml??)
- add zoom_start option (any way to programmetically calculate an appropriate value?)
'''


# quick start guide for folium maps:
# https://python-visualization.github.io/folium/quickstart.html

# set data path with gpx files
dataPath = os.path.abspath('gpx')

# download example gpx files from Openstreetmap
downloadExample(dataPath)

# folder path with all gpx tracks
fileList = [os.path.join(dataPath, f) for f in os.listdir(dataPath)]

# read all tracks and append to one variable
# tracks[i][j][0] == i-th track, j-th point, latitude
# tracks[i][j][1] == i-th track, j-th point, longitude
tracks = readGPX(fileList)


# Use polyline if:
# - you have a low number of gnss points per distance
# - you need a more responsive map since you have a large number of tracks
#
# adapt color, weight (line thickness) and opacity to your liking
# (I suggest weight = 2.5, opacity = 0.2)

plotMap(tracks, vectorType = 'polyline', tiles = 'Stamen Terrain', outputFile = dataPath + '/exampleLines.html')


# Use heatmap if:
# - you have many overlapping tracks, which cannot be displayed by polyline
#   e.g. opacity = 0.2 --> max. number of lines is 5
# - you have sufficiently high point density (every 3 meters??)
# - you don't care about gaps in your lines
# - you don't care about unresponsive maps or have a powerful pc
#   (in the case of a large number of tracks)
#
# adapt radius and blur to your liking (I suggest radius = 2, blur = 3)

plotMap(tracks, vectorType = 'heatmap', tiles = 'Stamen Terrain', outputFile = dataPath + '/exampleHeat.html')

