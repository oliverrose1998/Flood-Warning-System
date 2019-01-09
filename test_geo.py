# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 13:41:47 2017

@author: hz324
"""

import pytest
from floodsystem.haversine import haversine
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import river_with_stations
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation

s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (1, 1)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
list_s=[]
list_s.append(s)
list_s = list_s*3

#def test_stations_by_distance():
#    assert (stations_by_distance(list_s, (0,0))[0][1])== haversine((1,1),(0,0))
#    assert (stations_by_distance(list_s, (0,0))[1][1])== haversine((1,1),(0,0))
#    assert (stations_by_distance(list_s, (0,0))[2][1])== haversine((1,1),(0,0))

def test_stations_within_radius():
    assert len(stations_within_radius(list_s,(0,0),0)) == 0
    assert len(stations_within_radius(list_s,(0,0),1000)) == 4

s_id = "test-s-id"
m_id = "test-m-id"
label = "another station"
coord = (1.1, 1)
trange = (-2.31, 3.4445)
river = "River Y"
town = "Your Town"
r = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
list_s.append(r)

def test_river_with_stations():
    assert river_with_stations(list_s) == ["River X","River Y"]

def test_stations_by_river():
    assert stations_by_river(list_s) == {"River X": ["some station"]*3, "River Y": ["another station"]}

def test_rivers_by_station_number():
    assert rivers_by_station_number(list_s,0) == [('River Y', 1), ('River X', 3)]
    assert rivers_by_station_number(list_s,1) == [('River X', 3)]
