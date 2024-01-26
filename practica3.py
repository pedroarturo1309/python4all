#1 – Realizar un programa que solicite al usuario un número indeterminado de
# números (mientras se tecleen números que no sean cero). Al salir el programa
# debe dar en pantalla el total de números dados y la suma de ellos.
print("****** ejercicio 1 *******")
suma_numeros = 0.00
cantidad_numeros = 0.00
while True:
    numero = float(input("Digite un numero, (o precione 0 para salir): "))
    if numero == 0:
        break
    suma_numeros += numero
    cantidad_numeros += 1

print("La cantidad de numeros digitados fue: ", cantidad_numeros)
print("La suma de numeros digitados fue: ", suma_numeros)
print("****** FIN ejercicio 1 *******")
print("")

print("****** ejercicio 2 *******")
# 2- Realizar un programa que presente un menú con las siguientes opciones
# 1- Convertir grados a Celsius a Fahrenheit
# 2- Convertir dólar a pesos
# 3- Convertir metros a pies
# 4- Salir
# Cada vez que finalice una de estas acciones debe regresar al menú. El programa
# solo finalizará cuando el usuario elija la opción salir.
while True:
    print("MENU - PEDRO")
    print("1 - Convertir de Celsius a Fahrenhit")
    print("2 - Convertir de dolar a pesos")
    print("3 - Convertir metros a pies")
    print("4 - Salir")

    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        celsius = int(input("Ingrese los grados Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print("Los fahrenheit es de: ", fahrenheit)
    elif opcion == "2":
        tasa_cambio = 58.61
        usd = int(input("Ingrese la cantidad de dolar que quiere cambiar: "))
        dop = usd * tasa_cambio
        print("La tasa de cambio actual es de 58.61, el total en pesos es de: ", dop)
    elif opcion == "3":
        metros = int(input("Ingrese la longitud en metros: "))
        pies = metros * 3.28084
        print(f"{metros} metros equivalen a {pies:.2f} pies.")
    elif opcion == "4":
        break
    else:
        print("Opcion digitada no valida.")

print("****** FIN ejercicio 2 *******")
print("")

# 3- Hacer un programa que genere las tablas de multiplicar de los números
# múltiplos de 5 que hay entre 1 y 1000
print("****** ejercicio 3 *******")
for numero in range(5, 1001, 5):
    print("Tabla de multiplicar del: ", numero)

    for multiplicador in range(1, 13):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")

print("****** FIN ejercicio 3 *******")
print("")

# 4- Realizar un programa que reciba por teclado el sueldo de un empleado y le
# aplique los cálculos de ISR (ver tabla DGII), ARS, y AFP (investigar porcentajes)
print("****** ejercicio 4 *******")
salario = float(input("Digite el salario del empleado: "))
afp = salario * 0.0287
ars = salario * 0.0304

SALARIO_ANUAL = (salario - afp - ars) * 12.00
renta = 0.00
if(SALARIO_ANUAL <= 416220):
    renta = 0.00

if SALARIO_ANUAL >= 416220.01 and SALARIO_ANUAL <= 624329.00:
    renta = (SALARIO_ANUAL - 416220.01) * 0.15

if SALARIO_ANUAL >= 624329.01 and SALARIO_ANUAL <= 867123.00:
    renta = ((SALARIO_ANUAL - 624329.01) * 0.20) + 31216


if SALARIO_ANUAL >= 867123.01:
    renta = ((SALARIO_ANUAL - 867123.01) * 0.25) + 79776

if(renta > 0):
    renta = renta / 12

print("El descuento de AFP es de: ", afp)
print("El descuento de ARS es de: ", ars)
print("El descuento de ISR es de: ", renta)
print("Salario a recibir: ", salario - renta - afp -ars)

print("****** FIN ejercicio 4 *******")
print("")


# 5-Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un
# límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100
# El cajero debe solicitar Banco y monto a retirar. Si el banco es ABC el limite de
# retiro son 10,000 y 2000 pesos por transacción en caso contrario.
# El cajero debe informar si el monto solicitado no puede ser dispensado o si
# excede el límite de transacción. Y debe hacer la distribución de los billetes de
# acuerdo al monto. Por ejemplo, si el usuario solicita 3,900 y hay disponibilidad en
# todos los billetes, el cajero debe dispensar 3 billetes de mil, 1 de quinientos y 4 de
# cien.
print("****** ejercicio 5 *******")
BILLETES_1000 = 9
BILLETES_500 = 19
BILLETES_100 = 99
print("****** FIN ejercicio 5 *******")
print("")