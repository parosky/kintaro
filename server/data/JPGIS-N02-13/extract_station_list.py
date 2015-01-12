#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import shapefile

if __name__ == "__main__"
    stations = codecs.open('N02-13_Station.csv', 'r', 'shift-jis').readlines()
    shapes = shapefile.Reader('N02-13_Station.shp').shapes()
    with codecs.open('stations.csv', 'w', 'utf-8') as f:
        for station, shape in zip(stations, shapes):
            station = ','.join(station.split(',')[2:]).strip()
            shape = ','.join(map(str, shape.bbox))
            f.write('%s,%s\n' % (station, shape))
