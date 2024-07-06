import matplotlib
from pyrosm import OSM
from pyrosm import get_data
import warnings

DATADIR = "F:\\items\\生产实习20240705\\data"
warnings.simplefilter(action='ignore', category=FutureWarning)
fp = get_data("beijing", directory=DATADIR)

osm = OSM(fp)
buildings = osm.get_buildings()
buildings.plot()

matplotlib.pyplot.show()