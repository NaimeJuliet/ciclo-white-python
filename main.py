import math
#menu de opciones
opcion=1

print("Empanadas el Machetico")
print("**************************")
print("0. Salir")
print("1. Encontrar multiplo de 2")
print("2. Encontrar raiz cuadrada")
print("3. Sumar 100")
print("4.Elevar al cuadrado")

#los elif siempre llevan condicion() pero los else no:
while(opcion !=0):
    opcion=int(input("Bienvenido, digita una opcion: "))
    if(opcion==1):
        numero=int(input("Digite un numero entero: "))
        if(numero % 2 == 0):
            print(f'El numero {numero} es multiplo de 2')
        else:
            print(f'El numero {numero} no es multiplo de 2')
    elif(opcion==2):
        numero=int(input("Digite un numero entero: "))
        print(f'La raiz cuadrada de {numero} es: {math.sqrt(numero)}')
    elif(opcion==3):
        numero=int(input("Digite un numero entero: "))
        print(f'La suma de {numero} + 100 es: {numero+100}')
    elif(opcion==4):
        numero=int(input("Digite un numero entero: "))
        print(f'El cuadrado de {numero} es : {numero*numero}')
    elif(opcion==0):
        break
    else:
        print(f'Digita una opcion valida')
else:
    print("PARA AHI")





'''
while(opcion !=0):
   # print(input("digita una opcion: "))
   #int operacion de casteo de datos
   opcion=int(input("digita una opcion: "))
else:
    print("para ahi")
'''