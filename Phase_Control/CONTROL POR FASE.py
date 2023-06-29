#Control PID por fase
from machine import Pin, Timer, ADC
from time import sleep_us, sleep_ms
from array import array as arr

#Variables
us = 0 #Contador
cero = 0 #Bandera para cruce por cero
Anglon = 730 #Inicia apagado


#PINES CONFIG
Triger = Pin(13, Pin.OUT, drive=Pin.DRIVE_3, value=0) #Pin donde dispara el triac
cruce_cero = Pin(12, Pin.IN, Pin.PULL_DOWN)

#Para lecturas analógicas
POT = ADC(Pin(34))
i = 0
dato_Tr = arr('f',[0]*10) #array apara mediam movil

#Rutina de interrupción1
def Angulo_disparo(tim):
    
    global us, cero, Anglon
    if cero:
        us = us + 10
        if us>=Anglon:
            Triger.on()
            sleep_us(20)#Timepo para enclavar
            Triger.off()
            cero = 0

#Interrupcion por cada 100us
tim = Timer(0) # Escogemos timer0 
tim.init(mode=Timer.PERIODIC, freq=10000, callback=Angulo_disparo)

#Rutina de interrupción2
def cero_f(cruce_cero):
    
    global cero,us
    
    cero = 1 #Bandera onde haber pasado un cruce por cero
    us = 0 #Seteamos contador a 0us
 
#Interrupción por cruce por cero
cruce_cero.irq(cero_f, Pin.IRQ_FALLING )


while 1:

    #Lectura adc y filtro media movil
    Tr = POT.read_u16()   
    sleep_ms(10)
    
    dato_Tr[i] = Tr #Agregamos a la lista  
    Tr = sum(dato_Tr)/10 
    if i>=9:
        i = 0
    else:
        i=i+1
        
    #Control al actuador
    Anglon = int((Tr)*(730/65535))
