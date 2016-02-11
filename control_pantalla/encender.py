import serial
import time
powerOff = (0xAA, 0x11, 0xFE, 0x01, 0x01, 0x11)
ser = serial.Serial(
                    port='COM3',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS)  # abrir y configurar puerto serie

time.sleep(0.1)            #para que le de tiempo a abrir
for n in powerOff:
    ser.write(chr(n))   # lanxzamos el array de uno en uno



ser.close()              # cerramos puerto
