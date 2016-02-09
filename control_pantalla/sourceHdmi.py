import serial
import time
sourceHdmi = (0xAA, 0x14, 0xFE, 0x01, 0x21, 0x34)
ser = serial.Serial(
                    port='COM3',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS)  # open serial port

time.sleep(1)            #para que le de tiempo a abrir
for n in sourceHdmi:
    ser.write(chr(n))   # lanxzamos el array de uno en uno



ser.close()              # cerramos puerto
