#1) Hacer un script en python que solicite 2
# numeros al usuario y si el primero es menor que el segundo
# imprima los numeros que estan en el rango indicando si es par
# o impar. Ejemplo, si ingresa 4 y 8 debe mostrar:
#                    5 impar
#                   6 par
#                  7 impar
print("****** ejercicio 1 *******")
primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
if(primer_numero < segundo_numero):
    for numero in range(primer_numero + 1, segundo_numero):
        str = "par" if numero % 2 == 0 else "impar"
        print(f"{numero} {str}")
print("****** FIN ejercicio 1 *******")
print("")
# 2) Escriba un programa que pregunte cuántos números se
# van a introducir, pida esos números,
# y muestre un mensaje cada vez que un
# número no sea mayor que el primero.
# " el numero x introducido no es mayor que el x primero"
print("****** ejercicio 2 *******")
cantidad_numeros = int(input("Ingrese cuántos números va a introducir: "))

if cantidad_numeros < 1:
    print("Debe introducir al menos un número.")
else:
    primer_numero = float(input("Ingrese el primer número: "))
    for i in range(1, cantidad_numeros):
        numero = float(input(f"Ingrese el número {i + 1}: "))

        if numero <= primer_numero:
            print(f"El número {numero} no es mayor que el primero ({primer_numero}).")
print("****** FIN ejercicio 2 *******")
print("")
# 3) un programa que genere la tabla de amortización
# de un préstamo (usar la formula de amortización
# francés que usó en el calculo de las cuotas de préstamo)
print("****** ejercicio 3 *******")
valor_prestamo = float(input("Digite el valor del prestamo que desea tomar: "))
TASA = float(input("Digite la tasa anual del prestamo: "))
TOTAL_CUOTAS = int(input("Digite la cantidad de meses que desea tomar el prestamo: "))
tasa_interes_mensual = TASA / (12 * 100)
monto_cuota = (valor_prestamo * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual)**(-TOTAL_CUOTAS))
balance = valor_prestamo
for numero in range (1, TOTAL_CUOTAS + 1):
    interes_couta = balance * tasa_interes_mensual
    capital = monto_cuota - interes_couta
    balance = balance - capital
    print(f"Pago #{numero} ----> Cuota: {monto_cuota} ----> Capital: {capital} ----> Interes: {interes_couta} ----> Balance: {balance} ")
print("****** FIN ejercicio 3 *******")
print("")