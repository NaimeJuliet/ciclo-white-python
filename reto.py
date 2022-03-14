contador=1
sumatoria=0

#se pregunta en programacion con una condicion
while(contador<=5):
    numero=int(input('Ingrese un numero:'))
    if(numero < 0):
        sumatoria +=1
    contador +=1
print(f'La cantidad de numero negativos ingresados fue: {sumatoria}')

