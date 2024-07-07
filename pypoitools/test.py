import warnings
import pyrosm
import folium
import geopandas as gpd
import pandas as pd

# settings
pd.set_option('display.max_columns', None)    # 显示所有列
pd.set_option('display.max_rows', None)      # 显示所有行
warnings.simplefilter(action='ignore', category=FutureWarning) #解决FutureWarning问题

# static
PBFDIR = "F:\\items\\生产实习20240705\\data\\pbf\\"   #.osm.pbf数据位置
GEODIR = "F:\\items\\生产实习20240705\\data\\geojson\\"   #.geojson数据位置
HTMLDIR = "F:\\items\\生产实习20240705\\data\\html\\"   #.html数据位置

# main
osm = pyrosm.OSM(PBFDIR+"Beijing.osm.pbf")   #创建osm对象
drive_net = osm.get_network(network_type="driving") #获取drive_net数据
gdf = gpd.GeoDataFrame(drive_net)   #转化为geo格式
gdf.to_file(GEODIR+"drive_net.geojson", driver='GeoJSON') #将gdb保存为文件

m = folium.Map(location=[39.9042, 116.4074], zoom_start=13) #创建map对象
folium.GeoJson(gdf).add_to(m) #将geo数据加入map
m.save(HTMLDIR+'beijing_drive_net.html') #将map保存为html