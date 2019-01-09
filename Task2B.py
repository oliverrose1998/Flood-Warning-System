# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 01:06:57 2017

@author: lenovo
"""

from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    output_list = stations_level_over_threshold(stations, 0.8)
    
    print(output_list)
    
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    run()
    