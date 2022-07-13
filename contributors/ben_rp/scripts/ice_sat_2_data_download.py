import pandas as pd 
import geopandas as gpd 
import sys
import logging
import concurrent.futures
import time
from datetime import datetime
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pyproj import Transformer, CRS
from shapely.geometry import Polygon, Point
from sliderule import icesat2
from sliderule import sliderule


# Specify region of interest from geojson
poly_fn = 'grandmesa.geojson'
region = icesat2.toregion(poly_fn)["poly"]

# Read geojson with geopandas
pregion = gpd.read_file(poly_fn)

# Prepare coordinate lists for plotting the region of interest polygon
region_lon = [e["lon"] for e in region]
region_lat = [e["lat"] for e in region]