import os
import sys
import gpxpy
import folium
import folium.plugins
import webbrowser
import requests

def downloadExample(outputPath):
    '''
    Downloads multiple gpx files from Openstreetmap to create an example map.
    The download links are stored in 'datalinks.txt'.
    '''
    if outputPath[-1] != '/':
        outputPath = outputPath + '/'

    if not os.path.isdir(outputPath):
        os.mkdir(outputPath)

    print('Downloading...')

    with open('datalinks.txt') as file:
        for i, line in enumerate(file):
            url = line.rstrip()

            # download file if it does not exist
            if not os.path.isfile(outputPath + 'track' + str(i) + '.gpx'):
                req = requests.get(url)
                open(outputPath + 'track' + str(i) + '.gpx', 'w').write(req.text)

            sys.stdout.write("%d..." % i) # update progress bar
            sys.stdout.flush()

def readGPX(fileList):
    # read all gpx files on 'path' and append all points to 'tracks'
    tracks = []
    for filename in fileList:
        if filename.endswith('.gpx'):
            file = open(filename, 'r')
            gpx = gpxpy.parse(file)
            
            # append all points to one variable 'tracks'
            points = []
            for track in gpx.tracks:
                for segment in track.segments:
                    for point in segment.points:
                        points.append(tuple([point.latitude, point.longitude]))

            tracks.append(points)

            print(filename)

    return tracks


def plotMap(
    tracks,
    vectorType = 'polyline',
    tiles = 'Stamen Terrain',
    opacity = 0.6,
    outputFile = 'map.html',
    ):

    # create folium map object, where the map is centered to the first point
    map = folium.Map(location=[tracks[0][0][0], tracks[0][0][1]], tiles = None)

    # add background raster layer
    folium.TileLayer(tiles = tiles, opacity = opacity).add_to(map)

    # draw map depending on user input
    if vectorType == 'polyline':
        for track in tracks:
            folium.PolyLine(track, color = 'red', weight = 2.5, opacity = 0.2).add_to(map)

    elif vectorType == 'heatmap':
        cmap = getColormap()
        for track in tracks:
            folium.plugins.HeatMap(track, radius = 2, blur = 3, gradient = cmap).add_to(map)

    # save map as html file
    map.save(outputFile)

    # open in browser
    webbrowser.open('file://' + os.path.abspath(outputFile))


def getColormap():
    # TODO: add other colormaps
    cmap = \
        {0.0: '#000003',
        0.1: '#160b39',
        0.2: '#410967',
        0.3: '#6a176e',
        0.4: '#932567',
        0.5: '#bb3754',
        0.6: '#dc5039',
        0.7: '#f37719',
        0.8: '#fba40a',
        0.9: '#f5d745',
        1.0: '#fcfea4'}

    return cmap
