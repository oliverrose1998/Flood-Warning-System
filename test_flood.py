# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:17:09 2017

@author: lenovo
"""


#import pytest
from floodsystem.station import MonitoringStation
from floodsystem.flood import  stations_level_over_threshold, stations_highest_rel_level, rel_moving_average, risk_index_calc, issuing_warning
from floodsystem.stationdata import build_station_list, update_water_levels

def test_stations_level_over_threshold_and_stations_highest_rel_level():
# two functions are very similar so tested together
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    list_s=[]
    list_s.append(s)
    list_s = list_s*3
    for station in list_s:
        station.latest_level = 3.4445
    #disable the update water level function when using this test function
    list_of_stations = stations_level_over_threshold(list_s, 1)
    assert len(list_of_stations) == 3
    for station in list_s:
        station.latest_level = -2.3
    list_of_stations = stations_level_over_threshold(list_s, 0)
    assert len(list_of_stations) == 3
    list_of_stations = stations_highest_rel_level(list_s, 2)
    assert len(list_of_stations) == 2
#This function tests all the functions related to assesing the risk of flood
def test_risk_assesment():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    # Find station 'Cam'
    for station in stations:
        if station.name == 'Cam':
            station_cam = station
            break
    
    assert type(rel_moving_average(station_cam,2)) == float
    assert risk_index_calc(station_cam,2) < 1
    assert risk_index_calc(station_cam,2) > -1
 # Find station 'Swindon'
    for station in stations:
        if station.name == 'Swindon':
            station_swindon = station
            break
    stations_for_test = [station_cam, station_swindon]
#    assert type(issuing_warning(stations_for_test)[1][1]) == str
    assert type(issuing_warning(stations_for_test)[0][1]) == str
    