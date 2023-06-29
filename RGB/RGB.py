from machine import Pin, Timer

R = Pin(12, Pin.OUT, drive=Pin.DRIVE_0)
V = Pin(13, Pin.OUT, drive=Pin.DRIVE_0)
A = Pin(14, Pin.OUT, drive=Pin.DRIVE_0)

#Variables modificables
led = 1 #Primer led en ecender
periodo=220

#Funcion selector de led
def SelecLed():
    global led
    
    if led==1:
        R.on()
        print("ROJO")
        V.off()
        A.off()
    
    if led==2:
        R.off()
        V.on()
        print("VERDE")
        A.off()
    
    if led ==3:
        R.off()
        V.off()
        A.on()
        print("AZUL")
    
    led+=1
    if led>3:
        led=1
        
tim1 = Timer(1)
tim1.init(period=periodo, mode=Timer.PERIODIC, callback=lambda t:SelecLed())