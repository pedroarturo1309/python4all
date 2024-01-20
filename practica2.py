#- Ana contrató una maquina expendedora de cigarros en su mercado. Favor ha
# cer un script en python que solicite al usuario el numero de su edad y que
# muestre un mensaje en consola diciendo si es mayor de edad o menor de edad.
print("****** ejercicio 1 *******")
edad = int(input("DIGITE SU EDAD POR FAVOR: "))
if(edad >= 18):
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

print("****** FIN ejercicio 1 *******")
print("")

# Carlos va a ir al cajero a hacer un retiro al cajero.
# en su cuenta tiene un balance de 1584.23.
# El cajero solo entrega billetes de 100.
# haga un script en python que solicite el monto del retiro.
# si el monto del retiro es mayor que el monto disponible,
# debe decirle por consola que no tiene fondos suficientes para la transacción.
# Si ingresa una cantidad que no se puede entregar con billetes de 100
# (ej. 125, 1015, 150, 90) debe decirle que el monto solicitado
# no puede ser dispensado. Si tiene fondos y marca un monto válido,
# debe imprimir en consola la cantidad de billetes de 100 que se dispensaran.
print("****** ejercicio 2 *******")
MONTO_CUENTA = 1584.23
valor_retiro = int(input("Favor digite la cantidad que desea retirar: "))

if (valor_retiro % 100) == 0:
    if(valor_retiro > MONTO_CUENTA):
        print("No tiene fondos suficientes para la transaccion")
    else:
        print("Se han dispensado " + str(valor_retiro / 100) + " billetes de 100")
else:
    print("El valor digitado no puede ser dispensado")


print("****** FIN ejercicio 2 *******")
print("")

#- Luis fue contratado como programador Jr.
# en python con un salario de 55,000 pesos.
# Haga un script en python con el que pueda calcular
# el impuesto sobre la renta, que le descontarán mensualmente.
# (ver tabla ISR DGII)
print("****** ejercicio 3 *******")
salario = 55000.00
SALARIO_ANUAL = salario * 12.00
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
print("El impuesto a pagar es de: ", renta)
print("****** FIN ejercicio 3 *******")
print("")

#- Maria fue a solicitar un préstamo de 100,000 pesos al banco BHD,
# y lo quiere a 12 meses. El banco le presta a una tasa de interés anual
# del 16.33%. Haga un script en python que le permita a
# Maria conocer el monto de la cuota a pagar.
# (Usar la formula de amortización francés, y comparar
# el resultado con la calculadora de prestamos de ProUsuario que debe dar igual)
# C= V / (1- (1/ (1+i))^N)/i)
print("****** ejercicio 4 *******")
VALOR_PRESTAMO = 100000
TASA = 16.33
TOTAL_CUOTAS = 12
tasa_interes_mensual = TASA / (12 * 100)
monto_cuota = (VALOR_PRESTAMO * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual)**(-TOTAL_CUOTAS))
print("El monto de la cuota mensual es de : ", monto_cuota)
print("****** FIN ejercicio 4 *******")
print("")