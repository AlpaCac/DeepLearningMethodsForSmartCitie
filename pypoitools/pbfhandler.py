import warnings
import folium
import pyrosm
import pandas as pd
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

        self.poi_type_num = dict()
        self.poi_type_list = list()
        self.cal_poi_types()
        self.street_type_list = ['primary', 'secondary', 'residential', 'tertiary', 'service', 'motorway_link', 'motorway', 'trunk_link', 'unclassified', 'primary_link', 'trunk', 'pedestrian', 'tertiary_link', 'secondary_link', 'living_street', 'footway', 'disused', 'cycleway', 'track', 'path', 'busway', 'construction', 'crossing', 'steps']
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
            if row['amenity'] not in self.poi_type_list and row['amenity'] != None and row['amenity'] != 'yes' and row['amenity'] != 'nan':
                self.poi_type_list.append(row['amenity'])
            if row['shop'] not in self.poi_type_list and row['shop'] != None and row['shop'] != 'yes' and row['shop'] != 'nan':
                self.poi_type_list.append(row['shop'])
            if row['tourism'] not in self.poi_type_list and row['tourism'] != None and row['tourism'] != 'yes' and row['tourism'] != 'nan':
                self.poi_type_list.append(row['tourism'])

            if row['amenity'] != None and row['amenity'] != 'yes' and row['amenity'] != 'nan':
                if self.poi_type_num.get(row['amenity']) is None:
                    self.poi_type_num[row['amenity']] = 0
                self.poi_type_num[row['amenity']] += 1
            if row['shop'] != None and row['shop'] != 'yes' and row['shop'] != 'nan':
                if self.poi_type_num.get(row['shop']) is None:
                    self.poi_type_num[row['shop']] = 0
                self.poi_type_num[row['shop']] += 1
            if row['tourism'] != None and row['tourism'] != 'yes' and row['tourism'] != 'nan':
                if self.poi_type_num.get(row['tourism']) is None:
                    self.poi_type_num[row['tourism']] = 0
                self.poi_type_num[row['tourism']] += 1

    def get_poi_type_num(self, poi_type):
        return self.poi_type_num[poi_type]

    def get_num_of_bad_data(self):
        count = 0
        pois = self.get_pois()
        for index, row in pois.iterrows():
            badNum = 0
            if row['amenity'] == None or row['amenity'] == 'nan' or row['amenity'] == 'yes':
                badNum+=1
            if row['shop'] == None or row['shop'] == 'nan' or row['shop'] == 'yes':
                badNum+=1
            if row['tourism'] == None or row['tourism'] == 'nan' or row['tourism'] == 'yes':
                badNum+=1
            if badNum == 3:
                count+=1
        return count

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

    def get_streets(self, type=None):
        streets = self.osm.get_network(network_type="driving")
        if type == None:
            return streets
        return streets[streets['highway'] == type]

    def get_poi_type_list(self):
        return self.poi_type_list
