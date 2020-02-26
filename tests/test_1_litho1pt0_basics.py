import pytest

## ==========================


import litho1pt0 as litho
from pprint import pprint
import numpy as np

#%%



def test_model_sanity():

    print("\n")
    print("Number of points in triangulation: {}".format(litho._interpolator.npoints))
    print("Layer keys \n")
    for layer in litho.l1_layer_decode.items():
        pprint( layer )
    print("\nValue keys \n")
    for value in litho.l1_data_decode.items():
        pprint( value )


    return

#%%

def test_raster():

    lats = np.array([0,10,20])
    lons = np.array([0,0,0])

    litho.layer_depth(lats,lons, layerID='ASTHENO-TOP')

    #%%

    ## make a global raster of some quantity

    lonv, latv = np.meshgrid(np.linspace(-180,180,180), np.linspace(-89,89,89), sparse=False, indexing='xy')

    l1 = litho.layer_depth(latv, lonv, "LID-BOTTOM")
    l2 = litho.layer_depth(latv, lonv, "LID-TOP")

    lthickness = (l1 - l2)*0.001
    lab_depth = l1*0.001


    l1 = litho.layer_depth(latv, lonv, "CRUST3-BOTTOM")
    l2 = litho.layer_depth(latv, lonv, "CRUST1-TOP")

    cthickness = (l1 - l2)*0.001


    l1 = litho.layer_depth(latv, lonv, "LID-BOTTOM")
    l2 = litho.layer_depth(latv, lonv, "CRUST1-TOP")

    llthickness = (l1 - l2)*0.001

    topo = litho.layer_depth(latv, lonv, "WATER-BOTTOM")

    return

#%%



#%%


