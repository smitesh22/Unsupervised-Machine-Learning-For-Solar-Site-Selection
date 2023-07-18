#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:58:02 2023

@author: smitesh22
"""


import numpy as np
import pandas as pd
import re
import time
import glob
import os
from osgeo import ogr

#check the dem data 

if __name__ == "__main__":
    
    print("----------------CHECK DEM DATA INTEGRITY--------------------")
    time.sleep(2)
    
    dem_data = pd.read_csv("/home/smitesh22/Data/extent.csv")
    
    filename_location = []
    for index, row in dem_data.iterrows():
        coords = re.findall('\d+', row.filename)
        coords = [int(coord) for coord in coords[:2]]
        updated_coords = []
        data = [int(np.round(item)) for item in row[1:]]
        
        for coord in coords:
            updated_coords.append(coord)
            updated_coords.append(coord+1)
        assert sorted(data) == sorted(updated_coords), f'Error with DEM file name and extend do not match {row.filename}'
        
        print(f"Checked file {row.filename}.tif")
    
    
    print("----------------CHECK SOLAR IRRADIANCE INTEGRITY--------------------")
    time.sleep(2)
    
    for i, file in enumerate(glob.glob("/home/smitesh22/Data/Solar Irradiance/*.csv")):    
        df = pd.read_csv(file, nrows=2, header=None)
        latitude = int(np.round(float(df[5][1])))
        longitude = int(np.round(float(df[6][1])))
        pattern = r'N(\d+)E(\d+)_wgs84.csv'
        
        match = re.search(pattern, file)
        if match:
            number1 = int(match.group(1))
            number2 = int(match.group(2))
        assert latitude == number1 and longitude == number2, f'Solar Irradiance data problem with file {file}'
        
        print(f"Checked file {file}")
        
    print("----------------CHECK GIS INTEGRITY--------------------")
    time.sleep(2)
    
    path = "/home/smitesh22/Data/GIS Extracted/"
    directories = [os.path.join(path, name) for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    
    driver = ogr.GetDriverByName('ESRI Shapefile')
    file_paths = []
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for dir_name in dirs:
                file_paths.append(os.path.join(root, dir_name))
                
    driver = ogr.GetDriverByName('ESRI Shapefile')
    
    for shape_file in file_paths[1::2]:
        match = re.findall(r'\d+', shape_file)
        match  = [int(num) for num in match[1:3]]
        dataset = driver.Open(shape_file, 0)
        layer = dataset.GetLayer()
        extent = layer.GetExtent()
        min_x, max_x, min_y, max_y = extent
        coords = [int(np.round(coord)) for coord in extent]
            
        assert abs(coords[2] - match[0]) in (0, 1) and abs(coords[0] - match[1]) in (0, 1), f'Error with shape file {shape_file}'
        print(f'Checked file {shape_file}')