from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

stations = build_station_list()
listofdist=stations_by_distance(stations,(52.2053, 0.1218))
print(listofdist[:10])
print(listofdist[-10:])