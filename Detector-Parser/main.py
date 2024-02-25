import data_collection as dc
import json_requests as jr
import json_parsing as jp
# dumps -> serialize
# loads -> deserialize

dc.serialSetup()

while(1):
    
    try:
        # check if there is data waiting in the serial buffer
        if dc.readyToReadFromSerial:
            data_list = dc.readFromSerial()
            
            if dc.validSensorData(data_list):
                # Create JSON string
                bmp_json = jp.createStringJSON(data_list)
                
                # Send JSON string
                # jr.sendDataJSON(bmp_json)
                
    except KeyboardInterrupt:
        dc.serialTerminate()