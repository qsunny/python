# -*- codiing:utf-8 -*-
"""
serial port test
扫描枪测试:D 起动 E 结束
"""
__author__="aaron.qiu"

import serial
import time
import string
import io

if __name__ == "__main__":
    ser = serial.Serial()
    ser.port="COM2"
    ser.baudrate=115200
    ser.stopbits=serial.STOPBITS_ONE
    ser.timeout=0
    ser.parity=serial.PARITY_NONE
    #ser.rtscts=1
    print(ser)

    try:
        '''ser = serial.Serial('COM2', 115200, timeout=0, parity=serial.PARITY_NONE, rtscts=1)'''
        ser.open()
    except Exception as e:
        print("error open serial port: " + str(e))
        exit()

    if ser.isOpen():
        print("ready====")
        try:
            #ser.flushInput()  # flush input buffer, discarding all its contents
            #ser.flushOutput()  # flush output buffer, aborting current output
            # and discard all that is in buffer

            # write data
            ser.write(b"E")
            print("write data: E")

            time.sleep(0.5)  # give the serial port sometime to receive the data

            numOfLines = 0

            while True:
                time.sleep(2)
                response = ser.readline()
                print(bytes.decode(response)  )

                print("read data: " + str(response, encoding = "utf-8"))

                numOfLines = numOfLines + 1

                if (numOfLines >= 5):
                    break

            ser.close()
        except Exception as e1:
            print("error communicating...: " + str(e1))

    else:
        print("cannot open serial port ")






