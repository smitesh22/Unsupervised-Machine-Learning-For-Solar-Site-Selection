# -*- coding: utf-8 -*-
import glob
import pandas as pd
from osgeo import osr
from osgeo import gdal 
import re

def create_csv():
    pass


if __name__ == "__main__":
    files = glob.glob("/home/smitesh22/Data/DEM/*.tif")
    
    for i, filename in enumerate(files):
        im = gdal.Open(filename)
        geotransform = im.GetGeoTransform()
        projection = im.GetProjection()
        
        # Extract corner coordinates
        ulx, xres, xskew, uly, yskew, yres = geotransform
        lrx = ulx + (im.RasterXSize * xres)
        lry = uly + (im.RasterYSize * yres)
        
        # Create coordinate transformation
        source_projection = osr.SpatialReference()
        source_projection.ImportFromWkt(projection)
        target_projection = osr.SpatialReference()
        target_projection.ImportFromEPSG(4326)  # Assuming you want WGS84 coordinates
        
        transform = osr.CoordinateTransformation(source_projection, target_projection)
        
        # Transform corner coordinates to target CRS
        ul_lon, ul_lat, _ = transform.TransformPoint(ulx, uly)
        lr_lon, lr_lat, _ = transform.TransformPoint(lrx, lry)
        
        data = pd.read_csv("/home/smitesh22/Data/extent.csv")
        
        
        pattern = r"\/([^\/]+)\.tif$"
        
        match = re.search(pattern, filename)
        
        filename = match.group(1)
        
        new_data = {
        "filename": filename,
        "upper_lat": ul_lat,
        "upper_long": lr_lon,
        "lower_lat": lr_lat,
        "lower_long": ul_lon}
        
        new_row_df = pd.DataFrame([new_data])

        # Concatenate the existing data with the new row DataFrame
        data = pd.concat([data, new_row_df], ignore_index=True)

        # Write the updated DataFrame back to CSV
        data.to_csv("/home/smitesh22/Data/extent.csv", index=False)
                    