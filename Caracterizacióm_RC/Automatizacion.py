from machine import Pin, ADC
import time

Des_cap = Pin(25, Pin.OUT, value=1) # activado para comenzar con  el capacitor descargado. Satura el transistor
adc = ADC(Pin(32))#pin de lectura adc
adc.atten(ADC.ATTN_11DB)#Atenuación de 11dB (150mV - 2450mV)

#Variables del sistema RC
Capacitor = 0.000100 #faradios
Resistor = 100000 #ohmios
t = 5*Capacitor*Resistor #Tiempo de carga para 99% aprox
muestreo = t/0.010 #en segundos

print("BD_int:")#Inicio de mediciones 
time.sleep_ms(1000) # 1seg de tiempo más que suficiente para que tenga aprox 0v
Des_cap.off()#Da comienzo a la carga del capacitor. Corta el transistor

#Comienza muestreo
num=0 #Contador
while num<=muestreo:#Cuantos muestreos?
    val = adc.read_u16()*(3.3/65535)#lectura analogica
    time.sleep_ms(10)#Periodo del muestreo en ms
    print("volts"+str(val*(5/3.3)))#imprimimos lectura
    num += 1
    print("BD_end")#Fin de mediciones

while True:
    Des_cap.on()#Descarga capacitor. Vuelve a saturar el transistor
    #Para detener el programa CTRL