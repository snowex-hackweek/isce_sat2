from sliderule import icesat2
from uavsar_pytools import UavsarCollection
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import contextily as cx
import os
from os.path import join, exists, basename
import warnings
import pickle 
from glob import glob

warnings.simplefilter(action='ignore', category=FutureWarning)

def download_uavsar():
    col = UavsarCollection(collection = 'Grand Mesa, CO', work_dir = '~/Downloads/', dates = ('2019-12-01', 'today'))
    col.collection_to_tiffs()
    
def download_icesat2(poly_dict, directory='/tmp/is2', length=100.0, res=50.0, verbose=False, confidence = False):
    os.makedirs(directory, exist_ok=True)
    icesat2.init("icesat2sliderule.org", verbose=verbose)
    print(poly_dict)
    for name, poly in poly_dict.items():
        out_fp = os.path.join(directory,f'{name}_atl06sr.pkl')
        if not os.path.exists(out_fp):
            print(f'Starting on {name}'.center(50, '-'))
            # note that there is an issue here between os'. When running on a jupyter hub we indexed by                 
            # ['poly'] whereas on a mac local machine we indexed by [0]
            poly = icesat2.toregion(poly)['poly']
            result = gpd.GeoDataFrame()
            conf_range = range(2,5)
            if not confidence:
                conf_range = [4]
            for conf in conf_range:
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
                rsps['confidence'] = conf
                result = result.append(rsps)
            name = name.replace(' ','')
            name = name.replace(',','')

            with open(out_fp, 'wb') as f:
                pickle.dump(result, f)
        else:
            print(f'{name} already exists. Skipping...')
                            

if __name__ == '__main__':
    print('starting')
    # download_uavsar()
    polys = {}
    for fp in glob(join('/Users/zachkeskinen/Documents/isce_sat2/data/uavsar_shape_files', '*.shp')):
        name = basename(fp).split('_')[0]
        polys[name] = fp
    types = {'confidence':{'res': 50, 'len':100, 'conf':True}, 'sd':{'res': 20, 'len':40, 'conf':False}}
    # polys = pickle.load(open('data/bounds.pkl', 'rb'))
    
    for k, v in types.items():
        download_icesat2(polys, directory = os.path.join('/tmp/is2', k), res = v['res'], length = v['len'], confidence = v['conf'])