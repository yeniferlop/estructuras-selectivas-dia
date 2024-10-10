# estructura condicional simple
a = 33
b = 200
if b > a:
    print(b," es mayor que ",a)



#Doble
y = 200
z = 333
if y > z:
    print(y," es mayor que ",z)
else:
    print(y,"no es mayor que",z)

#Multiple
a = 200
b = 207
if a > b:
    print(a, "es mayorque ",b)
elif a < b:
    print(a,"Es menor que",b)
else:
    print(a,"es igual que",b)

#Enlazadas
x = 28

if x > 10:
    print("Por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("Pero no por encima de 20.")

# end y sep

print("estudiar los sabados", end= '')
print("es genial")

print(" estudiar los sabados")
#print("es genial)


P_SEMCILLAS = 20000
P_DOBLE = 25000
P_TRIPLE = 28000
IMPUESTOS_TARJETA = 0.07


def calcular_precio(tipo_hamburguesa, medio_pago, cantidad):
    if tipo_hamburguesa == 1:
        precio = P_SEMCILLAS
        descripcion = "sencilla"
    elif tipo_hamburguesa == 2:
        precio = P_DOBLE
        descripcion = "doble"
    elif tipo_hamburguesa == 3:
        precio = P_TRIPLE
        descripcion = " triple"
    else:
        return None

    total_sin_cargo = precio * cantidad

    if medio_pago == 1:
        impuesto = round(total_sin_cargo * IMPUESTOS_TARJETA)
    else:
        impuesto = 0

    total = round(total_sin_cargo + impuesto)

    return descripcion, precio, cantidad, impuesto, total

def generar_mensaje (descripcion, precio,cantidad, impuesto, total):
    return (f"Tipo de hamburguesa: {descripcion}\n"
            f"Precio: ${precio}\n"
            f"cantidad: {cantidad}\n"
            f"Impuesto: {impuesto}\n"
            f"Total: ${total}")

def validar_datos (tipo_hamburguesa, medio_pago,cantidad):
    if 1 <= tipo_hamburguesa <= 3 and 1 <= medio_pago <= 2 and cantidad >0:
        resultado = calcular_precio(tipo_hamburguesa, medio_pago,cantidad)

        descripcion, precio, cantidad, impuesto, total = resultado
        mensaje = generar_mensaje(descripcion,precio, cantidad, impuesto, total)

        print("-----------------\n"+ mensaje)
    else:
        print("verifique las pciones ingresadas.")

#entradas
tipo_hamburguesa = int(input("ingrese tipo de hamburguesa \n1. sencilla \n2. doble \n3. triple \n"))
medio_pago = int(input("ingrese medio de pago \n1. tarjeta \n2. otro \n"))
cantidad = int(input("ingrese cantidad: "))

#salida
validar_datos(tipo_hamburguesa, medio_pago, cantidad)