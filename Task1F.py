# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 00:46:15 2017

@author: hz324
"""

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()

list_of_inconsistency = inconsistent_typical_range_stations(stations)

print(list_of_inconsistency)
