import matplotlib.pyplot as plt

#Adquisición de datos por parte del txt
f = open("", "r")#Buscamos archivo txt existente o creamos uno nuevo
Lines = f.readlines() #Leemos las lineas del documento
data = [] #Hacemos una lista en donde asignar cada medición a un  espacio

#Filtramos la información relevante
for l in Lines:
    if "volts" in l:
        data.append(float(l[5:].strip()))
        f.close()

#Proceso de creación de gráficas requeridas
ypointsvc = data #Lecturas medidas del voltaje en el capacitor

#Varieables del circuit0
fuentedc = 5 #En volts
Resistor = 100000 #En ohms
Capacitor = 0.0001 #En faradios

#Conseguimos el voltaje que cae en el resistor 
ypointsvr = []

for d in data:
    ypointsvr.append(fuentedc - d)
    #Conseguimos la corriente de la malla en el tiempo 
    ypointsI = []

for d in ypointsvr:
    ypointsI.append(d/Resistor)
    #Convertimos la cantidad de muestras en tiempo
    xpoints = []
    t = 0

for d in ypointsI:
    xpoints.append(t)
    t = t+0.010

#proceso para mostrar las graficas necesarias
plt.subplot(3, 1, 1)
plt.plot(xpoints, ypointsvc)
plt.ylabel('Vcapacitor')
plt.title('Voltages en R Y C')
plt.subplot(3, 1, 2)
plt.plot(xpoints, ypointsvr)
plt.ylabel('Vresistor')
plt.subplot(3, 1, 3)
plt.plot(xpoints, ypointsI)
plt.ylabel('Icorriente')
plt.xlabel('Tiempo en segundos')
plt.show()
