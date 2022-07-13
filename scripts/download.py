from sliderule import icesat2
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import contextily as cx
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

"""
UAVSAR CODE TO GET COHERENCE AND BOUNDING BOX GEOJSON
"""

def download_uavsar(args):
    for poly in poly_list:
        """
        use code from Jack's group
        """
        return 
    
def download_icesat2(poly_list, directory='/tmp/is2', conf=2, length=100.0, res=50.0):
    os.makedirs(directory, exist_ok=True)
    icesat2.init("icesat2sliderule.org", verbose=False)
    for name,poly in poly_dict.items():
        res = gpd.GeoDataFrame()
        for conf in range(2,5):
            parms = {"poly": poly,
            "srt": icesat2.SRT_LAND,
            "atl08_class": "atl08_ground",
            "cnf": [conf],
            "len": length,
            "res": res,
            "maxi": 1,
            "t0":'2018-10-01T00:00:00Z',
            "t1":'2022-04-30T00:00:00Z'}
            rsps = icesat2.atl06p(parms)
            res = res.append(rsps)
    res.to_file(os.path.join(directory,f'{name}_atl06sr.geojson'))
                            

if __name__ == '__main__':
    poly_dict = download_uavsar(args)
    download_icesat2(poly_list)