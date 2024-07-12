import warnings
import folium
import pyrosm
import geopandas as gpd
from shapely import Polygon

warnings.simplefilter(action='ignore', category=FutureWarning)  #解决FutureWarning问题


class PbfHandler:
    def __init__(self, pbf, output_dir):
        self.pbf = pbf
        self.output_dir = output_dir
        self.osm = pyrosm.OSM(pbf)  #创建osm对象
        self.map = folium.Map(location=self.getpos(), zoom_start=10)  # 创建map对象

    # TODO: 计算中心点
    def getpos(self):
        return [39.9042, 116.4074]

    def save_map(self):
        self.map.save(self.output_dir + '\\output.html')  # 将map保存为html

    def add_streets_to_map(self):
        streets = self.osm.get_network(network_type="driving")  # 获取drive_net数据
        gdf = gpd.GeoDataFrame(streets)  # 转化为geo格式
        folium.GeoJson(gdf).add_to(self.map)  # 将geo数据加入map

    def add_buildings_to_map(self):
        buildings = self.osm.get_buildings()
        gdf = gpd.GeoDataFrame(buildings)
        folium.GeoJson(gdf).add_to(self.map)  # 将geo数据加入map

    def add_pois_to_map(self):
        pois = self.osm.get_pois()
        gdf = gpd.GeoDataFrame(pois)
        folium.GeoJson(gdf).add_to(self.map)  # 将geo数据加入map

    def set_bounding(self):
        polygon = Polygon(((38, 115), (40, 117)))
        self.osm = self.osm = pyrosm.OSM(self.pbf, bounding_box=polygon)  #创建osm对象