import serial
import time
sourcePc = (0xAA, 0x14, 0xFE, 0x01, 0x14, 0x27)
ser = serial.Serial(
                    port='COM3',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS)  # abrir y configurar puerto serie

time.sleep(0.1)            #para que le de tiempo a abrir
for n in sourcePc:  # lanxzamos el array de uno en uno
    ser.write(chr(n))


ser.close()              # cerramos puerto

