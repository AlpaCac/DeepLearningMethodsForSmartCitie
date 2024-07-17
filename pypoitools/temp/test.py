from pyrosm import OSM, get_data
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry.polygon import Polygon

pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行

fp = get_data("beijing", update=True)
osm = OSM(fp)
# polygon = Polygon([(-0.21, 51.55), (-0.20, 51.55), (-0.21, 51.56), (-0.20, 51.56), (-0.21, 51.55)]) # 伦敦
# polygon = Polygon([(41.39, -87.34), (41.39, -87.33), (41.40, -87.33), (41.40, -87.34), (41.39, -87.34)]) # 芝加哥
# polygon = Polygon([(41.43, -74.00), (41.43, -74.01), (41.44, -74.00), (41.44, -74.01), (41.43, -74.00)])# 纽约
# polygon = Polygon([(-74.00, 41.43) ,( -74.01, 41.43), (-74.00, 41.44), (-74.01, 41.44), (-74.00, 41.43)])
polygon = Polygon([(116.39,39.90), (116.40,39.90), (116.40,39.91), (116.39,39.91), (116.39,39.90)])  # 北京
print("bbox:")
print(polygon)
osm = OSM(fp, bounding_box=polygon)
camden = osm.get_buildings()
ax = camden.plot(column="building", figsize=(12,12), legend=True, legend_kwds=dict(loc='upper left', ncol=3, bbox_to_anchor=(1, 1)))
plt.show()
