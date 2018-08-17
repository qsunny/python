# -*- codiing:utf-8 -*-
"""
serial port test
通讯设置格式：
波特率：9600（72.b.L.4）
校验位：ＮＯＮＥ(73.PA.0)
数据位：8
停止位：2

4F 30 0D 0A 正常结束
4F 31 0D 0A 持续输出  工作位(71.o.c.1):1
4F 32 0D 0A 如果稳定持续输出 工作位(71.o.c.2):2
4F 39 0D 0A 稳定后输出指令 工作位(71.o.c.4):4
4F 38 0D 0A 立即后输出指令(不管是否稳定) 工作位(71.o.c.4):4

响应数据：A00 正常结束 41 30 30
	  E01 命令错误 45 30 31
"""
__author__="aaron.qiu"

import serial
import time
import string
import io

def hex2dec(string_num):
    """十六进制 to 十进制"""
    return str(int(string_num.upper(), 16))

if __name__ == "__main__":
    ser = serial.Serial()
    ser.port="COM2"
    ser.baudrate=9600
    ser.stopbits=serial.STOPBITS_TWO
    ser.timeout=0
    ser.parity=serial.PARITY_NONE
    #ser.rtscts=1
    print(ser)

    try:
        '''ser = serial.Serial('COM2', 9600, timeout=0, parity=serial.PARITY_NONE, rtscts=1)'''
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
            #ser.write(b"D")
            #ser.write(b"4F 39 0D 0A")
            str22 = "4F390D0A"
            b = bytearray(4)
            b[0]=0x4F
            b[1]=0x32
            b[2]=0x0D
            b[3]=0x0A
            ser.write(b)

            #a1 = bytearray(0x4F)
            #a2 = bytearray(0x39)
            #a3 = bytearray(0x0D)
            #a4 = bytearray(0x0A)


            ser.write(b)

            print("write data: "+b.decode("utf-8"))

            time.sleep(0.5)  # give the serial port sometime to receive the data

            numOfLines = 0

            while True:
                time.sleep(3)
                response = ser.readline()
                print(response.decode("utf-8"))

                #print("read data: " + str(response, encoding = "utf-8"))
                #print("read data: " + bytes)

                numOfLines = numOfLines + 1

                if (numOfLines >= 10):
                    break

            ser.close()
        except Exception as e1:
            print("error communicating...: " + str(e1))

    else:
        print("cannot open serial port ")






