from pbfhandler import PbfHandler

pbf_dir = "F:\\items\\生产实习20240705\\data\\pbf\\Beijing.osm.pbf"  #.osm.pbf数据位置
output_dir = "F:\\items\\生产实习20240705\\data"  #.geojson数据位置

pbfhandler = PbfHandler(pbf_dir, output_dir)
pbfhandler.set_bounding()
pbfhandler.add_buildings_to_map()
pbfhandler.save_map()
