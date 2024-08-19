import pandas as pd
import pyrosm
import matplotlib.pyplot as plt
from area import area
import geopandas as gpd
from pyproj import CRS
from shapely.ops import unary_union
from pyproj import Geod
from shapely.geometry import Point, LineString, Polygon, mapping

from pbfhandler import PbfHandler
from shapely.geometry.polygon import Polygon

pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行

pbf_dir = "F:\\items\\生产实习20240705\\data\\pbf\\Manhattan.osm.pbf"  #.osm.pbf数据位置
output_dir = "F:\\items\\生产实习20240705\\data"  #.geojson数据位置

polygon = Polygon([(116.36,39.92), (116.37,39.92), (116.37,39.93), (116.36,39.93), (116.36,39.92)])
pbfhandler = PbfHandler(pbf_dir, output_dir, polygon=None)


# print(pbfhandler.get_pois().columns)
# print(pbfhandler.get_pois().count())
# print(pbfhandler.get_poi_num())
# print(pbfhandler.get_num_of_bad_data())
# print(pbfhandler.get_poi_type_list())
# print(len(pbfhandler.get_poi_type_list()))
# print(pbfhandler.poi_type_num)
# for type in pbfhandler.get_poi_type_list():
#    print(type, pbfhandler.get_poi_type_num(type))

streets = pbfhandler.get_streets()
streets.plot()
# street_type_list = list()
# print(streets.columns)
# print(streets.head(10))
# print(streets['name'])
# print(len(streets))
# for index,row in streets.iterrows():
#     if row['highway'] not in street_type_list:
#         street_type_list.append(row['highway'])
# print(street_type_list)
# print(pbfhandler.get_streets(type='primary'))

# print(pbfhandler.get_street_length())
# print(pbfhandler.get_street_density())

# pois = pbfhandler.get_pois()
# for index, row in pois.iterrows():
#     if row['amenity'] == None and row['shop'] == None and row['tourism'] == None:
#         print(row)
#     if row['amenity'] == 'yes' or row['shop'] == 'yes' or row['tourism'] == 'yes':
#         print(row)
#     if row['amenity'] == 'nan' or row['shop'] == 'nan' or row['tourism'] == 'nan':
#         print(row)

pois = pbfhandler.osm.get_pois()
# print(pois.head(3))
# print(pois.columns)
pois.plot(markersize=3)
# ax = pois.plot(column='poi_type', markersize=3, figsize=(12,12), legend=True, legend_kwds=dict(loc='upper left', ncol=5, bbox_to_anchor=(1, 1)))

boundaries = pbfhandler.osm.get_boundaries()
# print(boundaries)
boundaries.plot(facecolor="none", edgecolor="blue")

print(pbfhandler.street_type_num)
# print(pbfhandler.get_street_density())
# pbfhandler.add_streets_to_map()
# pbfhandler.save_map()
plt.show()