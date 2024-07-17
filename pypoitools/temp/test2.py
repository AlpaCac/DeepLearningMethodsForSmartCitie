from pyrosm import OSM, get_data
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry.polygon import Polygon

pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行

fp = get_data("Beijing", update=True)
osm = OSM(fp)
polygon = Polygon([(39.90, 116.40), (39.91, 116.40), (39.90, 116.41), (39.91, 116.41), (39.90, 116.40)])
print("bbox:")
print(polygon)
osm = OSM(fp, bounding_box=polygon)
camden = osm.get_buildings()
ax = camden.plot(column="building", figsize=(12,12), legend=True, legend_kwds=dict(loc='upper left', ncol=3, bbox_to_anchor=(1, 1)))
plt.show()
