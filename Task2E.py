# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:34:12 2017

@author: Oliver Rose
"""

import datetime

from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    
    dates = (datetime.datetime(2017, 2, 24), datetime.datetime(2017, 3, 3))
    
    # Build list of stations
    stations = build_station_list()
    
    # Compiles list of 5 most at risk stations
    list_of_stations = [0] * 5

    for i in range (5):
        list_of_stations[i] = stations_highest_rel_level(stations, 5)[i][0]

    return plot_water_levels(list_of_stations, dates)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    
run()

