# This script converts data into JSON-compatible strings
import json

def createStringJSON(data: list, data_type: str) -> str:
    if data_type == "climate":
        json_data = {
            "user_id": 1,
            "detector_id":1,
            "temperature": float(data[0]),
            "pressure": float(data[1]),
            "altitude": float(data[2])
        }
        
        json_string = json.dumps(json_data)
        
        return json_string
    else:
        json_data = {
            "user_id": 1,
            "detector_id":1,
            "longitude": float(data[0]),
            "latitude": float(data[1])
        }
        
        json_string = json.dumps(json_data)
        
        return json_string

