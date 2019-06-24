# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:31:33 2017
@author: crc

This code uses 10m resolution Sentinal Imagery to calculate evapotranspiration 
at each pixel, and output an ET.tif for each image. The Sentinel Imagery must 
be Bottom of Atmosphere values. Any image over 5% cover should not be used.
Images need to be converted to show the Enhanced Vegetation Indexing values.
The images are handled using the GDAL/osgeo python packages from Python 2.7.

This model is coded specific to the Treasure Valley and the correspnding
Agrimet stations. Make climate input edits as neccesary.
Agrimet Data:
Reference ET (ASCE)
Max Temp
Min Temp
Solar Radiation
Dew Point
Wind Speed
Elevation

"""


def etProcessing(eviImagePath, newETImagePath, station, year, month, day):
    
    # imports for function
    from osgeo import gdal
    from osgeo.gdalconst import GDT_Float32
    import numpy as np
    import sys
    import pandas as pd


    # -----------------------------------------------------------------------------------------------------
    # IMAGE FILE LOCATIONS
    # -----------------------------------------------------------------------------------------------------
    # ndviRaster   = "D:\GIS_Data\Thesis\Scripts\Rasters\ndvi0623.tif"
    # albedoRaster = "D:\GIS_Data\Thesis\Scripts\Rasters\albedo0623.tif"
    # "D:\GIS_Data\Thesis\Scripts\Rasters\evi{}{}.tIF"
    # "D:\GIS_Data\Thesis\Scripts\Rasters\et{}{}.tif"
    eviRaster  = eviImagePath
    newFile    = newETImagePath
    
    # Register files for all of the GDAL drivers
    gdal.AllRegister()
    
    # Print Date
    print('----Starting: {}{}{}{}----' .format(station, year, month, day))
    
    # -----------------------------------------------------------------------------------------------------
    # CLIMATE DATA FROM AGRIMET STATIONS
    # uSE ANY SINGLE STATION OR ANY COMBINATION
    # -----------------------------------------------------------------------------------------------------
    # Boise Agrimet station information

    # Use this for ETrs; reference ET for Alfalfa
    if station == "Boise":
        # print("--BOISE INFORMATION--")
        url = "https://www.usbr.gov/pn-bin/daily.pl?station=BOII&year=%s&month=%s&day=%s&year=%s&month=%s&day=%s&pcode=ETRS&pcode=MN&pcode=MX&pcode=MM&pcode=SR&pcode=TA&pcode=YM&pcode=UA" % (year, month, day, year, month, day)
        # table from website
        urlCSV         = pd.read_table(url)
        urlValues      = urlCSV[18:20].values
        AgMet_KM_input = float(urlValues[1,0][19:23])
        #Tmin_input     = float(urlValues[1,0][31:36])
        #Tmax_input     = float(urlValues[1,0][43:49])
        #Tmean_input    = float(urlValues[1,0][57:62])
        #Rnet_input     = float(urlValues[1,0][69:75])
        #RH_mean_input  = float(urlValues[1,0][83:88])
        #Tdew_input     = float(urlValues[1,0][96:101])
        #uz_input       = float(urlValues[1,0][110:114])
        #z              = 829
    
    # Parma Agrimet station information
    if station == "Parma":
        # print("--PARMA INFORMATION--")
        url = "https://www.usbr.gov/pn-bin/daily.pl?station=PMAI&year=%s&month=%s&day=%s&year=%s&month=%s&day=%s&pcode=ETRS&pcode=MN&pcode=MX&pcode=MM&pcode=SR&pcode=TA&pcode=YM&pcode=UA" % (year, month, day, year, month, day)
        # table from website
        urlCSV         = pd.read_table(url)
        urlValues      = urlCSV[18:20].values
        AgMet_KM_input = float(urlValues[1,0][19:23])
        #Tmin_input     = float(urlValues[1,0][31:36])
        #Tmax_input     = float(urlValues[1,0][43:49])
        #Tmean_input    = float(urlValues[1,0][57:62])
        #Rnet_input     = float(urlValues[1,0][69:75])
        #RH_mean_input  = float(urlValues[1,0][83:88])
        #Tdew_input     = float(urlValues[1,0][96:101])
        #uz_input       = float(urlValues[1,0][110:114])
        #z              = 703
    
    # Nampa Agrimet station information
    if station == "Nampa":
        # print("--NAMPA INFORMATION--")
        url = "https://www.usbr.gov/pn-bin/daily.pl?station=NMPI&year=%s&month=%s&day=%s&year=%s&month=%s&day=%s&pcode=ETRS&pcode=MN&pcode=MX&pcode=MM&pcode=SR&pcode=TA&pcode=YM&pcode=UA" % (year, month, day, year, month, day)
        # table from website
        urlCSV         = pd.read_table(url)
        urlValues      = urlCSV[18:20].values
        AgMet_KM_input = float(urlValues[1,0][19:23])
        #Tmin_input     = float(urlValues[1,0][31:36])
        #Tmax_input     = float(urlValues[1,0][43:49])
        #Tmean_input    = float(urlValues[1,0][57:62])
        #Rnet_input     = float(urlValues[1,0][69:75])
        #RH_mean_input  = float(urlValues[1,0][83:88])
        #Tdew_input     = float(urlValues[1,0][96:101])
        #uz_input       = float(urlValues[1,0][110:114])
        #z              = 824
    
    
    # Climate Station Averages
    if station == "Mean":
        # print("--BOISE INFORMATION--")
        url1 = "https://www.usbr.gov/pn-bin/daily.pl?station=BOII&year=%s&month=%s&day=%s&year=%s&month=%s&day=%s&pcode=ETRS&pcode=MN&pcode=MX&pcode=MM&pcode=SR&pcode=TA&pcode=YM&pcode=UA" % (year, month, day, year, month, day)
        # table from website
        urlCSV1         = pd.read_table(url1)
        urlValues1      = urlCSV1[18:20].values
        AgMet_KM_input1 = float(urlValues1[1,0][19:23])
        # Tmin_input1     = float(urlValues1[1,0][31:36])
        # Tmax_input1     = float(urlValues1[1,0][43:49])
        # Tmean_input1    = float(urlValues1[1,0][57:62])
        # Rnet_input1     = float(urlValues1[1,0][69:75])
        # RH_mean_input1  = float(urlValues1[1,0][83:88])
        # Tdew_input1     = float(urlValues1[1,0][96:101])
        # uz_input1       = float(urlValues1[1,0][110:114])
        # z1              = 829
        # print("--PARMA INFORMATION--")
        url2 = "https://www.usbr.gov/pn-bin/daily.pl?station=PMAI&year=%s&month=%s&day=%s&year=%s&month=%s&day=%s&pcode=ETRS&pcode=MN&pcode=MX&pcode=MM&pcode=SR&pcode=TA&pcode=YM&pcode=UA" % (year, month, day, year, month, day)
        # table from website
        urlCSV2         = pd.read_table(url2)
        urlValues2      = urlCSV2[18:20].values
        # climate variables from table
        AgMet_KM_input2 = float(urlValues2[1,0][19:23])
        # Tmin_input2     = float(urlValues2[1,0][31:36])
        # Tmax_input2     = float(urlValues2[1,0][43:49])
        # Tmean_input2    = float(urlValues2[1,0][57:62])
        # Rnet_input2     = float(urlValues2[1,0][69:75])
        # RH_mean_input2  = float(urlValues2[1,0][83:88])
        # Tdew_input2     = float(urlValues2[1,0][96:101])
        # uz_input2       = float(urlValues2[1,0][110:114])
        # z2              = 703
        # print("--NAMPA INFORMATION--")
        url3 = "https://www.usbr.gov/pn-bin/daily.pl?station=NMPI&year=%s&month=%s&day=%s&year=%s&month=%s&day=%s&pcode=ETRS&pcode=MN&pcode=MX&pcode=MM&pcode=SR&pcode=TA&pcode=YM&pcode=UA" % (year, month, day, year, month, day)
        # table from website
        urlCSV3         = pd.read_table(url3)
        urlValues3      = urlCSV3[18:20].values
        # climate variables from table
        AgMet_KM_input3 = float(urlValues3[1,0][19:23])
        # Tmin_input3     = float(urlValues3[1,0][31:36])
        # Tmax_input3     = float(urlValues3[1,0][43:49])
        # Tmean_input3    = float(urlValues3[1,0][57:62])
        # Rnet_input3     = float(urlValues3[1,0][69:75])
        # RH_mean_input3  = float(urlValues3[1,0][83:88])
        # Tdew_input3     = float(urlValues3[1,0][96:101])
        # uz_input3       = float(urlValues3[1,0][110:114])
        # z3              = 824
        
        # Station Averages
        AgMet_KM_input  = (AgMet_KM_input1 + AgMet_KM_input2 + AgMet_KM_input3)/3
        
        # Tmin_input      = (Tmin_input1 + Tmin_input2 + Tmin_input3)/3
        # Tmax_input      = (Tmax_input1 + Tmax_input2 + Tmax_input3)/3
        # Tmean_input     = (Tmean_input1 + Tmean_input2 + Tmean_input3)/3
        # Rnet_input      = (Rnet_input1 + Rnet_input2 + Rnet_input3)/3
        # RH_mean_input   = (RH_mean_input1 + RH_mean_input2 + RH_mean_input3)/3
        # Tdew_input      = (Tdew_input1 + Tdew_input2 + Tdew_input3)/3
        # uz_input        = (uz_input1 + uz_input2 + uz_input3)/3
        # z               = (z1 + z2 + z3)/3
    
    
    # -----------------------------------------------------------------------------------------------------
    # EVI RASTER ARRAY
    # -----------------------------------------------------------------------------------------------------
    # open the image
    
    inDs = gdal.Open(eviRaster)
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
    eviData = band1.ReadAsArray(0, 0, cols, rows)
    
    # Use identified pixel points from Arcmap of sites
    # Array coordinates of weather stations within EVI raster
    # eviParma = eviData[5034,537]
    # print('PMAI station: %s' %eviParma)
    #eviBoise = eviData[7220,6645]
    # print('BOII station: %s' %eviBoise)
    
    
    # -----------------------------------------------------------------------------------------------------
    # ET CALCULATIONS
    # -----------------------------------------------------------------------------------------------------
    # Input Conversions
    AgMet_ETRS = AgMet_KM_input*25.4  # ASCE alfalfa reference et in mm/day from Agrimet station
    
    # -----------------------------------------------------------------------------------------------------
    # USE BELOW IF REFERENCE ET VALUES ARE NOT AVAILABLE
    # -----------------------------------------------------------------------------------------------------
    # uz = uz_input*0.44704  # daily average wind speed m/s
    # Tmax = (Tmax_input-32)*.5556  # max daily air temperature, °C
    # Tmin = (Tmin_input-32)*.5556  # min daily air temperature, °C
    # Tmean = (Tmean_input-32)*.5556  # mean daily air temperature, °C
    # Tmean = (Tmin + Tmax)/2  # mean daily air temperature, °C
    # Tdew = (Tdew_input-32)*.5556  # dew point temperature, °C
    
    # Other Calculated Climate Variables
    # k       = 273.15
    # G       = .1  # soil heat flux; check metric for local derivation
    # a       = .25  # albedo
    # es      = 0.6108*np.exp((17.27*Tmean)/(Tmean + 237.3))  # saturation vapor pressure, kPa
    # es      = (0.6108*np.exp((17.27*Tmin)/(Tmin + 237.3)) + 0.6108*np.exp((17.27*Tmax)/(Tmax + 237.3)))/2  # saturation vapor pressure, kPa
    # ea      = 0.6108*np.exp((17.27*Tdew)/(Tdew + 237.3))  # preferred actual vapor pressure calculation, kPa
    # svp_def = es-ea  # saturation vapor pressure deficit, kPa
    # bc      = (5.67*(10**(-8)))/((k)**4)  # stephan boltzman constant
    # P       = 101.3*((293 - (.0065*z))/293)**5.26  # atmospheric pressure at elevation z
    # gamma   = .000665*P  # psychrometric constant, kPa °C-1
    # h       = 2  # height of the measurement above the ground surface, m.
    # u2      = uz*(4.87/(np.log(67.8*h - 5.42)))  # wind speed at 2 m height, m s-1
    # delta   = (2503*np.exp((17.27*Tmean)/(Tmean + 237.3)))/((Tmean + 237.3)**2)  # slope of vapor pressure curve, kPa/ºC-1
    # DT      = delta/(delta+gamma*(1+.34*u2))  # Delta Term used to calculate Radiation Term
    # PT      = gamma/(delta+gamma*(1+.34*u2))  # Psi Term used to calculate Wind Term
    # TT      = (900/(Tmean+273))*u2  # Temperature Term used to calculate Wind Term
    # Rns      = Rnet_input*0.04184*(1. - a)
    # Rnl     = bc*0.2*(0.34-0.14*np.sqrt(ea))*(((Tmax + k)**4+(Tmin + k)**4)/2)
    # Lin     = (2.7*ea + .245*(Tmean+k)-45.14)
    # Lout    = 0.98*bc*((Tmean+k)**4)+(1-0.98)*Lin
    # Rnl     = 0.98*bc*(Tmean+k)**4
    # Rnet    = Rns + Rnl
    # rnS2    = .7  # coefficient to convert global rad to net rad (Alados et al. 2003)
    # rn      = rnS2 * Rnet_input * 0.04184 * (1. - a)
    # Rnet    = rnS2 * (Rnet_input - 48.5) * 0.04184 * (1. - a)
    
    # month = int(month)
    # Crop Coefficients for cool season grass/turf (kentucky blue grass)
    #if month <= 5:
    #    ccGrass = .5
    #if month == 6:
    #    ccGrass = .8
    #if month == 7:
    #    ccGrass = 1
    #if month == 8:
    #    ccGrass = .9
    #if month == 9:
    #    ccGrass = .75
    #if month == 10:
    #    ccGrass = .5
    # Dual Crop Coefficients for cool season grass/turf (kentucky blue grass)
    # grassHeight = 0.12  # meters
    # rh = (ea/es)  # relative humidity
    # dcGrass = ccGrass + (0.04*(uz-2)-0.004*(rh-45))*((grassHeight/3)**0.3)
    
    # ET Alfalfa Standardized Reference
    # ETrs = (0.408*delta*(Rnet - G) + gamma*(1600./(Tmean+273.))*u2*svp_def)/(delta + gamma*(1.+.38*u2))
    # Difference between calculated and reported reference ET
    # dif = abs(1- ETrs / AgMet_KM)*100
    # dif2 = abs(ETrs - AgMet_KM)
    # ET Actual using crop coefficient
    # ETcc = .85*AgMet_ETRS
    # ETdc = ccGrass*AgMet_ETRS
    # print('Agmet Ref: %.2f' % AgMet_KM)
    # print('Model Ref: %.2f' % ETrs)
    # print('Ref ET Difference: %.2f percent' % dif)
    
    
    # ET ACTUAL FROM EVI
    c = 0.49  # fitting coefficient
    b = 1.48  # fitting coefficient
    ETboii = AgMet_ETRS * b * (1. - np.exp((-2.25) * pixel)) - c

   
    # -------------------------------------------------------------------------
    # CREATE NEW ET IMAGE
    # -------------------------------------------------------------------------
    # create the output image
    driver = inDs.GetDriver()
    # print driver
    outDs = driver.Create(newFile, cols, rows, 1, GDT_Float32)
    # Process whole raster
    outNewData = AgMet_ETRS * b * (1. - np.exp((-2.95) * eviData)) - c
    outNewData[outNewData < 0.0] = -1.0  # originiall = -1
    
    # write the data; assign nodata values
    outBand = outDs.GetRasterBand(1)
    outBand.WriteArray(outNewData)
    outBand.SetNoDataValue(-1)
    # georeference the image and set the projection
    outDs.SetGeoTransform(inDs.GetGeoTransform())
    outDs.SetProjection(inDs.GetProjection())
    outDs = None    
    # delete current stored mem data
    del eviData, outDs, outBand, outNewData
    
    print('Finished: {}{}{}' .format(year, month, day))
    # return dif, dif2, c, ETboii, AgMet_KM, station
   


"""
# EXAMPLE USAGE
# April 4th through 9th
indexStart = 1
indexEnd = 7
currentIndex = 1
dateDay = 4
for i in range(indexStart,indexEnd):
    eviImagePath = "D:\GIS_Data\Thesis\Scripts\Rasters\evi{}.tif" .format(currentIndex)
    newETImagePath = "D:\GIS_Data\Thesis\Scripts\Rasters\outputTest\et{}.tif" .format(currentIndex)
    etProcessing(eviImagePath, newETImagePath, "Mean", "2017", "04", "0{}" .format(dateDay))
    currentIndex += 1
    dateDay += 1
""" 
    
    
    
    
    
    
