# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 12:23:53 2017

@author: lenovo
"""

from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    output_list = stations_highest_rel_level(stations, 10)
    
    print(output_list)
    
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    run()