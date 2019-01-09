# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:13:57 2017

@author: lenovo"""

from floodsystem.stationdata import build_station_list
from floodsystem.flood import issuing_warning
from floodsystem.stationdata import update_water_levels

def run():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    list_of_rel_moving_average =  issuing_warning(stations)
    print(list_of_rel_moving_average)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")

    run()

        