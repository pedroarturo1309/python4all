#-  Su sobrino necesita saber si el numero 5 es par o impar.
# Haga un script en python que guarde el numero en una variable,
# lo evalúe y muestre un mensaje en la consola diciendo "True"
# si el numero es par o "False" si es impar.
# (Solo debe usar expresiones, no puede usar la condicional IF)
print("****** ejercicio 1 *******")
evaluar_numero = 5
if(evaluar_numero%2==0):
    print("True")
else:
    print("False")
print("****** FIN ejercicio 1 *******")

print("")
print("****** ejercicio 2 *******")
#- Una cajera del banco popular necesita un programa que le permita
# convertir DOP $129,867.83 a Dólares.
# Debe tomar en cuenta que la tasa de cambio es 58.30
tasa_cambio = 58.30
monto_dop = 129867.83
cantidadUSD = monto_dop / tasa_cambio
print("La cantidad obtenida en USD es de:", cantidadUSD)

print("****** FIN ejercicio 2 *******")
print("")

print("****** ejercicio 3 *******")
#Un maestro constructor necesita un programa que le permita convertir
# la medida de 80 metros a pies.
VALOR_MUL = 3.281
pies = 80 * VALOR_MUL
print("80 metros en pies es: ", pies)
print("****** FIN ejercicio 3 *******")
print("")

print("****** ejercicio 4 *******")
#-  Su sobrino necesita saber si un numero es par o impar.
# Haga un script en python que reciba un numero por teclado y muestre un mensaje
# en la consola diciendo si el numero es par o impar.
numero = int(input("Digite un numero: "))
if(numero%2==0):
    print("El numero es par")
else:
    print("El numero es impar")
print("****** FIN ejercicio 4 *******")
print("")

print("****** ejercicio 5 *******")
#- Juan hizo una compra en el supermercado, el valor de la compra sin
# impuestos fue de RD$16,760.74.
# Haga un script en python que calcule el ITBIS,
# un descuento de 5% y el total a pagar.

valor_compra = 16760.74
DESCUENTO = valor_compra * 0.05
ITBIS = (valor_compra - DESCUENTO) * 0.18
total = valor_compra - DESCUENTO - ITBIS
print("El descuento es de: ", DESCUENTO)
print("El ITBIS es de: ", ITBIS)
print("El valor a pagar es de: ", total)
print("****** FIN ejercicio 5 *******")
print("")

print("****** ejercicio 6 *******")
#- Tu sobrino necesita calcular el area de un circulo para su clase de matemáticas.
# Haz un script que le permita hacer este cálculo solicitando el ingreso del
# diámetro del radio del circulo a medir (la formula es la constante PI
# multiplicada por el diámetro del radio al cuadrado)
PI = 3.14
diametro = int(input("Digite el diametro del circulo: "))
area = PI * diametro
print("El area es de: ", area)
print("****** FIN ejercicio 6 *******")