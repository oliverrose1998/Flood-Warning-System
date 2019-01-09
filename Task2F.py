# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 19:19:08 2017

@author: Oliver Rose
"""

import datetime

from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    
    dates_input = (datetime.datetime(2017, 2, 24), datetime.datetime(2017, 3, 3))
    
    # Build list of stations
    stations = build_station_list()
    
    # Compiles list of 5 most at risk stations
    list_of_stations = [0] * 5

    for i in range (5):
        list_of_stations[i] = stations_highest_rel_level(stations, 5)[i][0]

    p = 4
    
    return plot_water_level_with_fit(list_of_stations, dates_input, p)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    
run()


