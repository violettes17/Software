# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:49:48 2017

@author: Cyril
"""
import pygpx
from pygpx import GPX
gpx = GPX("blandine.gpx")
tracks = gpx.tracks
for track in tracks:
    print (track.name)
    for trkseg in track.trksegs:
        for trkpnt in trkseg.trkpts:
            #print (trkpnt.lat)
            #print (trkpnt.lon)
            #print (trkpnt.elevation)
            print (trkpnt.hr)
            print (trkpnt.time)

    print (track.full_duration())
    #print (rack.distance())