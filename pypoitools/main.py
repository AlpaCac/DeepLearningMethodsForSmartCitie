import pandas as pd
from pbfhandler import PbfHandler
from shapely.geometry.polygon import Polygon

pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行

pbf_dir = "F:\\items\\生产实习20240705\\data\\pbf\\Beijing.osm.pbf"  #.osm.pbf数据位置
output_dir = "F:\\items\\生产实习20240705\\data"  #.geojson数据位置

polygon = Polygon([(116.36,39.92), (116.37,39.92), (116.37,39.93), (116.36,39.93), (116.36,39.92)])
pbfhandler = PbfHandler(pbf_dir, output_dir, polygon=None)
# print(pbfhandler.get_pois())
# print(pbfhandler.get_pois().count())
print(pbfhandler.get_poi_type_list())
# pbfhandler.add_pois_to_map()
# pbfhandler.save_map()