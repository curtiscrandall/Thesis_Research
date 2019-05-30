# -*- coding: utf-8 -*-
"""
Created on Feb 21 2019
@author: Curtis Crandall

This function takes two images of equal dimensions and creates georeferenced
linear interpolations between them.

INPUTS:
    img1= first image (i.e. "image1.tif")
    img2: second image (i.e. "image10.tif")
    img1Day = index value (if first day of series, then imgDay1=1)
    img2Day = index value (if tenth day of series, then imgDay2=10)
    outputFolder = new image output location
        
    EXAMPLE:
    image1Path = "D:\GIS_Data\Thesis\Scripts\Rasters\evi1014.tIF"
    image2Path = "D:\GIS_Data\Thesis\Scripts\Rasters\evi1024.tIF"
    img1Day = 1
    img2Day = 10
    outputFolder = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest"

"""

def eviImageFill(image1Path, image2Path, img1Day, img2Day, outputFolder):

    # Imports
    from osgeo import gdal
    from osgeo.gdalconst import GDT_Float32
    import numpy as np
    import sys
    
    # Register files for all of the GDAL drivers
    gdal.AllRegister()
    
    
    # -------------------------------------------------------------------------
    # EVI IMAGES TO INTERPOLATE BETWEEN
    # -------------------------------------------------------------------------
    # image directory pathways
    image1 = image1Path
    image2 = image2Path
    # how many days between the two images
    fillDays = img2Day - img1Day
    # what image day to start on
    startDay = img1Day+1
    
    
    # -------------------------------------------------------------------------
    # FIRST EVI IMAGE ARRAY----------------------------------------------------
    # -------------------------------------------------------------------------
    # open image
    inDs = gdal.Open(image1)
    if inDs is None:
      #print 'Could not open image file'
      sys.exit(1)
    # read in data for first band
    band1 = inDs.GetRasterBand(1)
    # calculate rows
    rows = inDs.RasterYSize
    # calculate columns
    cols = inDs.RasterXSize
    # create array
    img1 = band1.ReadAsArray(0, 0, cols, rows)
    
    
    # -------------------------------------------------------------------------
    # SECOND EVI IMAGE ARRAY---------------------------------------------------
    # -------------------------------------------------------------------------
    # open image
    inDs2 = gdal.Open(image2)
    if inDs2 is None:
      #print 'Could not open image file'
      sys.exit(1)
    # read in data for first band
    band2 = inDs2.GetRasterBand(1)
    # calculate rows
    rows2 = inDs2.RasterYSize
    # calculate columns
    cols2 = inDs2.RasterXSize
    # create array
    img2 = band2.ReadAsArray(0, 0, cols2, rows2)
    
    # -------------------------------------------------------------------------
    # CREATE NEW EMPTY EVI IMAGE-----------------------------------------------
    # -------------------------------------------------------------------------
    # empty array based on actual EVI image
    imgX = np.zeros_like(img1)
    
    # -------------------------------------------------------------------------
    # CALCULATE NEW IMAGES-----------------------------------------------------
    # -------------------------------------------------------------------------
    for i in range(1,fillDays):
        
        # img 1 gap value
        f1 = ((fillDays-i) / fillDays)
        # img 2 gap value
        f2 = (i / fillDays)
        # calculate image 1 with gap value
        newImg1 = f1*img1
        # calculate image 2 with gap value
        newImg2 = f2*img2
        # new array of new values
        imgX = newImg1 + newImg2
        # set no data value threshold
        outData = imgX
        outData[outData <= 0] = -1
        
        # CREATE NEW GEOREFERENCED IMAGE OUTPUT
        # new image name
        newFile = "{}\new{}.tif" .format(outputFolder,startDay)
        # initialize driver
        driver = inDs.GetDriver()
        # new image raster
        outDs = driver.Create(newFile, cols, rows, 1, GDT_Float32)
        # set writing band of raster
        outBand = outDs.GetRasterBand(1)
        
        # write new image file
        outBand.WriteArray(outData)
        # set no data values
        outBand.SetNoDataValue(-1)
        # georeference the image and set the projection to match first image
        outDs.SetGeoTransform(inDs.GetGeoTransform())
        outDs.SetProjection(inDs.GetProjection())
        outDs = None
        
        print("New Image {} Completed" .format(startDay))
        # change file name for next image
        startDay += 1


img1 = "D:\GIS_Data\Thesis\Scripts\Rasters\evi194.tif"
img2 = "D:\GIS_Data\Thesis\Scripts\Rasters\evi204.tif"
eviImageFill(img1, img2, 194, 204, "D:\GIS_Data\Thesis\Scripts\Rasters")




