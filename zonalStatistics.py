# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:38:13 2019

@author: Curtis

This is to be run within the ArcPRO environment from Python console to
generate the associated boundary statistics

"""

from progressbar import ProgressBar
pbar = ProgressBar()


"""
# for python console in arcpro
import arcpy
i_Day = 1
boundaryName = "Irrigated"
saveName = "Ag"
for day in range(0,204):
    zone = "D:\GIS_Data\Thesis\Boundaries\{}.shp" .format(boundaryName)
    raster = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\et{}.tif" .format(i_Day)
    outTable = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables\etStats{}{}.dbf" .format(saveName ,i_Day)
    csvFolder = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables"
    arcpy.gp.ZonalStatisticsAsTable(zone,"FID",raster,outTable,"DATA","MEAN")
    arcpy.TableToTable_conversion(outTable, csvFolder, "etStats{}{}.csv" .format(saveName ,i_Day))
    i_Day += 1
    
i_Day = 1
boundaryName = "samplesAlfalfa"
saveName = "Alfalfa"
for day in range(0,204):
    zone = "D:\GIS_Data\Thesis\Boundaries\{}.shp" .format(boundaryName)
    raster = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\et{}.tif" .format(i_Day)
    outTable = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables\etStats{}{}.dbf" .format(saveName ,i_Day)
    csvFolder = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables"
    arcpy.gp.ZonalStatisticsAsTable(zone,"FID",raster,outTable,"DATA","MEAN")
    arcpy.TableToTable_conversion(outTable, csvFolder, "etStats{}{}.csv" .format(saveName ,i_Day))
    i_Day += 1

i_Day = 1
boundaryName = "samplesWheat"
saveName = "Wheat"
for day in range(0,204):
    zone = "D:\GIS_Data\Thesis\Boundaries\{}.shp" .format(boundaryName)
    raster = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\et{}.tif" .format(i_Day)
    outTable = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables\etStats{}{}.dbf" .format(saveName ,i_Day)
    csvFolder = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables"
    arcpy.gp.ZonalStatisticsAsTable(zone,"FID",raster,outTable,"DATA","MEAN")
    arcpy.TableToTable_conversion(outTable, csvFolder, "etStats{}{}.csv" .format(saveName ,i_Day))
    i_Day += 1

i_Day = 1
boundaryName = "samplesCorn"
saveName = "Corn"
for day in range(0,204):
    zone = "D:\GIS_Data\Thesis\Boundaries\{}.shp" .format(boundaryName)
    raster = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\et{}.tif" .format(i_Day)
    outTable = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables\etStats{}{}.dbf" .format(saveName ,i_Day)
    csvFolder = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables"
    arcpy.gp.ZonalStatisticsAsTable(zone,"FID",raster,outTable,"DATA","MEAN")
    arcpy.TableToTable_conversion(outTable, csvFolder, "etStats{}{}.csv" .format(saveName ,i_Day))
    i_Day += 1
 
i_Day = 1
boundaryName = "Semi_Irrigated"
saveName = "Urban"
for day in range(0,204):
    zone = "D:\GIS_Data\Thesis\Boundaries\{}.shp" .format(boundaryName)
    raster = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\et{}.tif" .format(i_Day)
    outTable = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables\etStats{}{}.dbf" .format(saveName ,i_Day)
    csvFolder = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables"
    arcpy.gp.ZonalStatisticsAsTable(zone,"FID",raster,outTable,"DATA","MEAN")
    arcpy.TableToTable_conversion(outTable, csvFolder, "etStats{}{}.csv" .format(saveName ,i_Day))
    i_Day += 1

i_Day = 1
boundaryName = "UrbanDensity_High"
saveName = "Urban_HD"
for day in range(0,204):
    zone = "D:\GIS_Data\Thesis\Boundaries\{}.shp" .format(boundaryName)
    raster = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\et{}.tif" .format(i_Day)
    outTable = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables\etStats{}{}.dbf" .format(saveName ,i_Day)
    csvFolder = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables"
    arcpy.gp.ZonalStatisticsAsTable(zone,"FID",raster,outTable,"DATA","MEAN")
    arcpy.TableToTable_conversion(outTable, csvFolder, "etStats{}{}.csv" .format(saveName ,i_Day))
    i_Day += 1

i_Day = 1
boundaryName = "UrbanDensity_Medium"
saveName = "Urban_MD"
for day in range(0,204):
    zone = "D:\GIS_Data\Thesis\Boundaries\{}.shp" .format(boundaryName)
    raster = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\et{}.tif" .format(i_Day)
    outTable = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables\etStats{}{}.dbf" .format(saveName ,i_Day)
    csvFolder = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables"
    arcpy.gp.ZonalStatisticsAsTable(zone,"FID",raster,outTable,"DATA","MEAN")
    arcpy.TableToTable_conversion(outTable, csvFolder, "etStats{}{}.csv" .format(saveName ,i_Day))
    i_Day += 1
    
i_Day = 1
boundaryName = "UrbanDensity_Low"
saveName = "Urban_LD"
for day in range(0,204):
    zone = "D:\GIS_Data\Thesis\Boundaries\{}.shp" .format(boundaryName)
    raster = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\et{}.tif" .format(i_Day)
    outTable = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables\etStats{}{}.dbf" .format(saveName ,i_Day)
    csvFolder = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables"
    arcpy.gp.ZonalStatisticsAsTable(zone,"FID",raster,outTable,"DATA","MEAN")
    arcpy.TableToTable_conversion(outTable, csvFolder, "etStats{}{}.csv" .format(saveName ,i_Day))
    i_Day += 1

"""


# extract spatial data from zonal stats tables
import numpy as np
import pandas as pd


Area = []
Mean = []
to_acres = 0.000247105
fileNames = "Corn"
saveArea = "All_{}_Area" .format(fileNames)
saveMean = "All_{}_et" .format(fileNames)
day = 1


for days in pbar(range(0,200)):
    inFile = pd.read_csv("D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables\etStats{}{}.csv" .format(fileNames,day))
    df = pd.DataFrame(inFile)
    # Area
    area = df['AREA'].values
    area = np.array(area)
    area[area <= 0] = 0.1
    acres = np.sum(area)*to_acres
    Area.append(acres)
    # Mean ET
    mean = df['MEAN'].values
    mean = np.array(mean)
    mean[mean <= 0] = 0.1
    mean = np.mean(mean)
    Mean.append(mean)
    
    day += 1



# dataframe for area
#dfa = pd.DataFrame(Area)
#dfa.to_csv("D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables\etStats{}.csv" .format(saveArea))
# dataframe for mean
dfm = pd.DataFrame(Mean)
dfm.to_csv("D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\etTables\etStats{}.csv" .format(saveMean))








