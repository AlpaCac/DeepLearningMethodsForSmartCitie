import warnings
import folium
import pyrosm
from area import area
import geopandas as gpd
from shapely import Polygon
from shapely.geometry import mapping
from shapely.ops import unary_union

warnings.simplefilter(action='ignore', category=FutureWarning)  #解决FutureWarning问题


class PbfHandler:
    def __init__(self, pbf, output_dir, polygon):
        self.pbf = pbf
        self.output_dir = output_dir
        self.osm = pyrosm.OSM(pbf, bounding_box=polygon)  #创建osm对象
        self.map = folium.Map(location=self.getpos(), zoom_start=10)  # 创建map对象

        self.poi_type_list = list()
        self.cal_poi_types()
    '''
    'amenity', 'building',
    'drinking_water', 'fast_food', 'internet_access', 'landuse', 'office',
    'parking', 'post_office', 'social_facility', 'source', 'start_date',
    'wikipedia', 'bicycle', 'books', 'clothes', 'organic', 'religion',
    'second_hand', 'shop', 'trade', 'water', 'attraction', 'information',
    'museum', 'tourism', 'geometry', 'osm_type', 'building:levels',
    'fountain', 'school', 'theatre', 'wholesale', 'zoo'
    '''
    def cal_poi_types(self):
        pois = self.get_pois()
        for index, row in pois.iterrows():
            if row['amenity'] not in self.poi_type_list and row['amenity'] != None:
                self.poi_type_list.append(row['amenity'])
            if row['shop'] not in self.poi_type_list and row['shop'] != None:
                self.poi_type_list.append(row['shop'])
            if row['tourism'] not in self.poi_type_list and row['tourism'] != None:
                self.poi_type_list.append(row['tourism'])

    def get_poi_num(self):
        pois = self.get_pois()
        return len(pois)

    def get_street_length(self):
        streets = self.get_streets()
        res = 0
        for index, row in streets.iterrows():
            res+=row['length']
        return res

    def get_street_density(self):
        length = self.get_street_length() # 米
        obj = mapping(self.get_boundaries())
        s = area(obj)/1e6 # 平方公里
        return length/s

    def get_boundaries(self):
        if self.osm.bounding_box != None:
            return self.osm.bounding_box
        boundaries = self.osm.get_boundaries(boundary_type="all")
        all_polygons = [geom for geom in boundaries['geometry']]
        merged_polygons = unary_union(all_polygons)
        return merged_polygons

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

    def set_bounding(self, polygon):
        self.osm = pyrosm.OSM(self.pbf, bounding_box=polygon)  #创建osm对象
        self.poi_type_list = list()
        self.cal_poi_types()

    def get_pois(self):
        return self.osm.get_pois()

    def get_streets(self):
        return self.osm.get_network(network_type="driving")

    def get_poi_type_list(self):
        return self.poi_type_list
