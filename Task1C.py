# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:56:20 2017

@author: Oliver Rose
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
    
stations = build_station_list()

listwithinradius=stations_within_radius(stations,(52.2053, 0.1218),10)
print('Stations within radius:')
print(listwithinradius)
