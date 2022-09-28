from xml.sax.handler import property_interning_dict
import math


def rev(numeroReferencia): 
    return int(numeroReferencia != 0) and ((numeroReferencia % 10) *
             (10**int(math.log(numeroReferencia, 10))) + 
                          rev(numeroReferencia // 10)) 
  


#definicion variables
suma=0
resta=0
multiplicacion=0
division=0

#verificar si es primo
def esPrimo(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


#menu principal
print(".:Menu:.")
print("1 para sumar")
print("2 para restar")
print("3 para multiplicar")
print("4 para dividir")
print("5 para verificar si un numero es primo")
print("6 para verificar si un numero es palindromo")

opcion = int(input("Digite una opcion de menu: "))

print()

numero1 = int(input("Digite el primer numero "))

#opciones
if opcion == 1:
    numero2 = int(input("Digite el segundo numero "))
    suma = numero1+numero2
    print(f"La suma de los dos numeros es: {suma}")

elif opcion == 2:
    numero2 = int(input("Digite el segundo numero "))
    resta = numero1-numero2
    print(f"La resta de los dos numeros es: {resta}")

elif opcion == 3:
    numero2 = int(input("Digite el segundo numero "))
    multiplicacion = numero1*numero2
    print(f"La multiplicacion de los dos numeros es: {multiplicacion}")

elif opcion == 4:
    numero1 = float(input("Digite el numero 1 "))
    numero2 = float(input("Digite el numero 2 "))
    division = numero1/numero2
    print(f"La division de los dos numeros es: {division}")

elif opcion == 5:
    if(esPrimo(numero1)):
        print("El numero es primo")
    else:
        print("El numero no es primo")

elif opcion == 6:
    print ("El numero original es : " + str(numero1)) 
    res = numero1 == rev(numero1) 
    print ("Es palindromo ? : " + str(res)) 
else:
    print("Digito incorrecto")
