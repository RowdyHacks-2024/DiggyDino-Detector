#include <Arduino.h>
#include <Adafruit_BMP280.h>
#include "globals.h"

// BMP variables
Adafruit_BMP280 bmp;
float temp;
int pressure;
float alt;

// holds sensor data
String data;

void setup() {

    Serial.begin(BAUDRATE);

    // wait for serial to initialize
    while ( !Serial );

    // Initializing BMP280 using I2C Address 0x76
    if ( !bmp.begin(BMP280_ADDRESS_ALT) ) {  
        Serial.println("Could not find a valid BMP280 sensor, check wiring!");
        delay(500);
    }

    Serial.println("BMP280 found!");

    Serial.println("Temperature(Celsius), Barometric Pressure(Pa), Altitude above sea level (hPa)");

}

// On every loop, read temperature, pressure, and altitude and send to SERVER as csv
void loop() {
    // Clear data "buffer"
    data = "";
    
    // Clear data variables
    temp = 0.0f;
    pressure = 0;
    alt = 0.0f;

    // Take the sum of data measurements
    for(int i = 0; i < NUM_READINGS; i++) {
        temp += bmp.readTemperature(); // Celsius, float
        pressure += bmp.readPressure(); // Pa, int
        alt += bmp.readAltitude(); // meters
    }

    // Calculate the average of data collected
    temp /= NUM_READINGS;
    pressure /= NUM_READINGS;
    alt /= NUM_READINGS;

    data = String(temp) + "," +  String(pressure) + "," + String(alt) + "," + "True"; // temperature,pressure,altitude

    Serial.print(data);
    Serial.println();

    delay(1000);
}