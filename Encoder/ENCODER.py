import _thread
from machine import Pin
import utime

#Declaracion de entradas de loque de sensores A
inA = [Pin(34,Pin.IN),Pin(35,Pin.IN),Pin(32,Pin.IN),Pin(33,Pin.IN)]
LecA = [0,0,0,0]

#Declamos salidas
Leds = [Pin(2,Pin.OUT,value=0),Pin(25,Pin.OUT,value=0),Pin(27,Pin.OUT,value=0),Pin(12,Pin.OUT,value=1)]


lock = _thread.allocate_lock()
def LecturaA(): #Muestreo de bloque de sensores A
    global LecA
    while 1:
        lock.acquire()
        LecA = [puerto.value() for puerto in inA]
        utime.sleep_ms(50)
        lock.release()

def impresion(): #otro ilo se va a encargar de unicamete imprimir lo sensado
    while 1:
        lock.acquire()
        print(LecA)
        utime.sleep_ms(10)
        lock.release()
        
_thread.start_new_thread(LecturaA,())#Hilo_1<
_thread.start_new_thread(impresion,())#Hilo_2

#Hilo_0 hILO principal
while 1:#El hilo principal se dedida a manejar las asalidas segun lo sensado
    lock.acquire()
    
    if LecA[3]==1: #Se preciona el boton
        Leds[0].value(1)
    else:
        Leds[0].value(0)
        
    if LecA[1]==1 and LecA[2]==0: #Gira a un sentido A
        Leds[1].value(1)
    else:
        Leds[1].value(0)
    
    if LecA[1]==0 and LecA[2]==1:#Gira a un sentido B
        Leds[2].value(1)
    else:
        Leds[2].value(0)
    
    if LecA[1]==0 and LecA[2]==0: #De tecta si hay movimiento de sentidos A o B
        Leds[3].value(1)
    else:
        Leds[3].value(0)    
    lock.release()
