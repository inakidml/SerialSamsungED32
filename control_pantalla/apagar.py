import serial
import time
powerOff = (0xAA, 0x11, 0xFE, 0x01, 0x00, 0x10)
ser = serial.Serial(
                    port='COM3',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS)  # open serial port

time.sleep(1)            #para que le de tiempo a abrir
for n in powerOff:
    ser.write(chr(n))


ser.close()              # close port
