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

#check the dem data 

if __name__ == "__main__":
    
    time.sleep(2)
    
    print("----------------CHECK DEM DATA INTEGRITY--------------------")
    
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
        
    time.sleep(2)
    
    