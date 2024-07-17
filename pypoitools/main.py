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

pbf_dir = "F:\\items\\生产实习20240705\\data\\pbf\\Beijing.osm.pbf"  #.osm.pbf数据位置
output_dir = "F:\\items\\生产实习20240705\\data"  #.geojson数据位置

polygon = Polygon([(116.36,39.92), (116.37,39.92), (116.37,39.93), (116.36,39.93), (116.36,39.92)])
pbfhandler = PbfHandler(pbf_dir, output_dir, polygon=polygon)


# print(pbfhandler.get_pois())
# print(pbfhandler.get_pois().count())
# print(pbfhandler.get_poi_num())
# print(pbfhandler.get_poi_type_list())

# streets = pbfhandler.get_streets()
# print(streets.columns)
# print(pbfhandler.get_street_length())
# pbfhandler.get_street_density()

# boundaries = pbfhandler.get_boundaries()
# gdf = gpd.GeoDataFrame(index=[0], geometry=[boundaries])
# gdf.crs = {'init': 'epsg:4326'} # WGS84
# fig, ax = plt.subplots(figsize=(10, 10))
# gdf.plot(ax=ax, facecolor='red', edgecolor='black')
# polygon1 = Polygon([(115.2,39.28), (117.3,39.28), (117.3,41.05), (115.2,41.05), (115.2,39.28)])
# obj = mapping(boundaries)
# area = area(obj)/1e6
# print(area)

print(pbfhandler.get_street_density())
# pbfhandler.add_pois_to_map()
pbfhandler.add_streets_to_map()
pbfhandler.save_map()
plt.show()