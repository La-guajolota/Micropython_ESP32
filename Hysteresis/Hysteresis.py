#Centro de temperatura por esmiferio. Controlar la temperatura
#entre un valor donde tenga dos dispositivos, un sispositivo por a
#arriva del valor de 5c y otro por debajo de 5c

from machine import Pin, ADC
import time

adc = ADC(Pin(32))#pin de lectura adc del sensor
adc.atten(ADC.ATTN_11DB)#Atenuación de 11dB (150mV - 2450mV)
Foco = Pin(2, Pin.OUT, value=0) # Accionador el foco
Led = Pin(14, Pin.OUT) #Led integrado


#Parámetro de la HISTERISÍS
Nb = 35 #Nivel bajo
Na = 45 #Nivel alto
P = 100 #Periodo de muestreo en ms

def ACCION(Bandera_acción):
    if Bandera_acción:
        Foco.on()
    else:
        Foco.off()
                
def MEDICION():
    Tem = adc.read_u16()*(3.3/65535)*(1/0.010)#lectura en celcius
    time.sleep_ms(P)#Periodo del muestreo en ms
    return Tem

while 1:#LOOP DEL PROGRAMA
    Tem = MEDICION()
    print("Temp: " + str(int(Tem)) +" *Celcius")
    
         
    if  Tem >= Na: #Por arriba de Na
        Foco.off() #Empieza a enfriar
        Bandera_acción = False #Bandera indicadora de estado actual
        
    if Tem <= Nb: #Por debajo de Nb
        Foco.on() #Empieza a calentar
        Bandera_acción = True #Bandera indicadora de estado actual
        
    Bandera_anchura = True #Para entrar a evaluar si se encuentra en la anchuara
    
    while Bandera_anchura:
        Tem = MEDICION()
        
        if Nb <= Tem and Tem <= Na:#Dentro de la anchura
            ACCION(Bandera_acción)#Se mantiene la acción anterior
            print("Dentro de la anchura con una temperatura de: " + str(int(Tem)) + " *Celcius")
            Led.on() #Indicador
        else:
            Bandera_anchura = False #Salío de la anchura
        
        