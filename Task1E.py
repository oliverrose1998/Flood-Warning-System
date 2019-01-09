# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 22:10:04 2017

@author: Oliver Rose
"""
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

stations = build_station_list()

rivers = rivers_by_station_number(stations,9)
print('Rivers ranked by number of stations ascending order:')
print(rivers)



