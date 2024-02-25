import data_collection as dc
import json_requests as jr
import json_parsing as jp
import random
# dumps -> serialize
# loads -> deserialize

dc.serialSetup()

while(1):
    
    try:
        # check if there is data waiting in the serial buffer
        if dc.readyToReadFromSerial:
            data_list = dc.readFromSerial()
            
            if dc.validSensorData(data_list):
                # Create JSON string from bmp data
                bmp_json = jp.createStringJSON(data_list, "climate")
                
                # Send JSON string containing bmp data
                # jr.sendDataJSON(bmp_json)
                print(bmp_json)
                
                # Create random coordinate data
                latitude = random.uniform(-70.0, 70.0)
                longitude = random.uniform(-180.0, 190.0)
                
                latitude = "{:.2f}".format(latitude)
                longitude = "{:.2f}".format(longitude)
                
                coord_list = [longitude, latitude]
                
                # Create JSON string from coordinate "data"
                coord_json = jp.createStringJSON(coord_list, "coordinate")
                
                # Send JSON string containing coordinate data
                # jr.sendDataJSON(coord_json)
                print(coord_json)
                
                
                
                
    except KeyboardInterrupt:
        dc.serialTerminate()