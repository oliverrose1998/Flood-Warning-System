# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:36:35 2017

@author: Oliver Rose
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import river_with_stations 
from floodsystem.geo import stations_by_river

stations = build_station_list()

listofrivers = river_with_stations(stations)
print('Rivers with stations:')
print(listofrivers[:10])

stationsbyriver = stations_by_river(stations)
print('Stations by river:')
print(stationsbyriver['River Cam'])
