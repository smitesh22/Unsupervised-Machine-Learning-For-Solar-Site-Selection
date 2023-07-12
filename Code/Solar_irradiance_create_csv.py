import pandas as pd
import numpy as np
import re
import glob 



def create_csv():
    files = glob.glob("/home/smitesh22/Data/Solar Irradiance/*.csv")
    
    out = pd.read_csv('/home/smitesh22/Data/solar_irradiance.csv')
    
    for location in files:
        df = pd.read_csv(location, nrows=2, header=None)
        
        # Display the resulting DataFrame
        latitude = int(np.round(float(df[5][1])))
        longitude = int(np.round(float(df[6][1])))
        
        
        pattern = r'N(\d+)E(\d+)_wgs84.csv'

        match = re.search(pattern, location)
        if match:
            number1 = int(match.group(1))
            number2 = int(match.group(2))
            
            
        assert latitude == number1
        assert longitude == number2
        
        file = pd.read_csv(location,  skiprows=2)
        
        #subset important attr
        df = file[['GHI',   
                  'DHI',
                  'DNI',
                  'Clearsky DHI',
                  'Clearsky DNI',
                  'Clearsky GHI',
                  'Temperature',
                  'Relative Humidity']]
        
        entry = df.describe().iloc[1].to_dict()
        
        filename = re.search(r'/([^/]+)\.csv$', location).group(1)
        
        entry['filename'] = filename
        
        row = pd.DataFrame([entry])

        out = pd.concat([out, row], ignore_index=True)
        
        out.to_csv("/home/smitesh22/Data/solar_irradiance.csv", index=False)
        
        
if __name__ == "__main__":
    
    create_csv()
    
    