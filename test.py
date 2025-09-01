# Autor: Isaac Alfredo
# Algoritmos  "básicos" en Python, Profe ayuda No entiendo :(.

print("hola a todos")

#AX = B - C
#encontrar el valor de X

mensaje = "El valor de la variable es:"
#implementar la funcion input,explicar cada parametro afectuado.

# A inpt("escriba un numero")

A=int("1")

result = A + A
print(type(result), result)

# Conversión de decimal a entero

B = 37.4
print(type(B), B)  
Au = int(B)  # se trunca el valor decimal
print("Decimal que se combirtio en entero:", Au, type (Au))

# Conversión de palabra a entero

p= "25"
n = int(p)
print("Palabra convertida a un numero entero:",n ,type(n))

# Conversión de un decimal a una palabra

d= 45.6
tx= str(d)
print("Decimal convertido a una palabra:", tx,type(tx))


# Conversión de palabra a decimal

pd = "19"
d = float(pd)
print("Palabra convertida a decimal:",d, type(d))

# 5. Conversión de un entero a decimal

e= 15
de = float(e)
print("Entero convertido a decimal:", de, type(de))

# 6. Conversión de entero a palabra
en = 42
pa= str(en)
print("Entero convertido a palabra:", pa, type(pa))


#Estructura de control, operaciones logicas 

#Booleado, 1,0

#A MAYOR A
if(A>5):
    print("este resultado del if es verdadero")
    print(f"la variable a es igual a: {A}")

else:
    print("no se cumple")
#A MENOR A 
if(A<12):
    print("este resultado del if es verdadero")
    print(f"la variable a es mayor a: {A}")

else:
    print("no se cumple")
#A IGUAL A

21212

if(A==10):
    print("este resultado del if si se cumple")
    print(f"la variabla es igual a: {A}")

else:
    print("no se cumple")
#A MAYOR IGUAL A 
if(A>=3):
    print("este  resultado del if si se cumple")
    print(f"la variable es:{A}")

else:
    print("no see cumple")

#A MENOR IGUAL A 
if(A<=76):
    print("este resultado del if si se cumple")

else:
    print("este resultado no se cumple")
