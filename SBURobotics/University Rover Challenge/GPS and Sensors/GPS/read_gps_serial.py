import serial
from serial import Serial
##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
#import serial

serial_port = 'COM8';
baud_rate = 115200; #In arduino, Serial.begin(baud_rate)
write_to_file_path = "newGPSOutput1.txt"
write_to_co2_file_path = "CO2Output.txt"
write_to_TVOC_file_path = "TVOCOutput.txt"
write_to_CO_file_path = "COOutput.txt"
output_file_gps = open(write_to_file_path, 'a')
output_file_co2 = open(write_to_co2_file_path, 'a')
output_file_TVOC = open(write_to_TVOC_file_path, 'a')
output_file_CO = open(write_to_CO_file_path, 'a')
ser = serial.Serial('COM8', 115200)

import time
time.sleep(3)
while True:
    line = ser.readline();
    line = line.decode("ANSI") #ser.readline returns a binary, convert to string
    line = line.replace('N', ' ')
    line = line.replace("W", ' ')
    print(line)
    if len(line) >= 25:
        output_file_gps.write(line)
    else:
        if line.startswith("Co2 ppm"):
            co2_string = line[10:]
            output_file_co2.write("42069  " + co2_string)
        if line.startswith("TVOC"):
            TVOC_string= line[6:]
            output_file_TVOC.write(TVOC_string)
        if line.startswith("MQ-7 PPM:"):
            CO_string = line[9:]
            output_file_CO.write(CO_string)
            

    output_file_gps.close()
    output_file_co2.close()
    output_file_TVOC.close()
    output_file_CO.close()
    time.sleep(1)

   
    output_file_gps = open(write_to_file_path, 'a')
    output_file_gps.truncate(0)

    output_file_co2 = open(write_to_co2_file_path, 'a')
    output_file_co2.truncate(0)

    output_file_TVOC = open(write_to_TVOC_file_path, 'a')
    output_file_TVOC.truncate(0)

    output_file_CO = open(write_to_CO_file_path, 'a')
    output_file_CO.truncate(1)
    
