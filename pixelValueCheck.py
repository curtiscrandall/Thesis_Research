# -*- coding: utf-8 -*-
"""
Created March 2018

@author: Curtis Crandall

This code will print all pixel values for all Sentinel image tiles; 
specifically images with tile information: N0205_R070_T11TNJ
And in the same location with a similar naming convention for iteration.

"""

# Imports
from osgeo import gdal
from progressbar import ProgressBar
pbar = ProgressBar()


# EVI CHECK
day = 2
for days in range(0,14):
    # image location
    image1 = "D:\GIS_Data\Thesis\Scripts\Rasters\img{}.tif" .format(day)
    inDs = gdal.Open(image1)
    # read in data for first band
    band1 = inDs.GetRasterBand(1)
    # calculate rows
    rows = inDs.RasterYSize
    # calculate columns
    cols = inDs.RasterXSize
    # create array
    img1 = band1.ReadAsArray(0, 0, cols, rows)
    boii = img1[7220,6645]
    print(boii)
    day += 1

# ET CHECK
day = 1
for days in pbar(range(1,29)):
    # image location
    image1 = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\et{}.tif" .format(day)
    inDs = gdal.Open(image1)
    # read in data for first band
    band1 = inDs.GetRasterBand(1)
    # calculate rows
    rows = inDs.RasterYSize
    # calculate columns
    cols = inDs.RasterXSize
    # create array
    img1 = band1.ReadAsArray(0, 0, cols, rows)
    boii = img1[7220,6645]
    print(boii)
    day += 1









