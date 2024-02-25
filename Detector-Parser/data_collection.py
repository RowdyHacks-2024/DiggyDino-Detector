# Collect data from the Arduino
import serial
import sys

# Setup process for the Arduino serial communication
def serialSetup() -> None:
    global ser
    ser = serial.Serial("COM18", 9600, timeout=1)
    
    print("--- Opening serial port... ---")
    print()
    
    if not ser.is_open:
        try:
            ser.open()
        except serial.SerialException:
            print("--- Serial port could not be opened ---")
            print()
            ser.close()
            sys.exit(0)
            
    
    print("--- Serial port opened successfully! ---")
    print()

# Checks if there is data in the serial port
def readyToReadFromSerial() -> bool:
    return ( ser.in_waiting > 0 )

# Returns a list from the serial data
def readFromSerial() -> list:
    serial_data = ser.readline().decode('utf-8').rstrip()
    serial_list = serial_data.split(",")
    return serial_list

def validSensorData(data: list) -> bool:
    if "True" in data:
        return True
    else:
        return False

def serialTerminate() -> None:
    if ser.is_open:
        print("Terminating serial port!")
        print()
        ser.close()
    
    sys.exit(0)