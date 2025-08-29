# string1 = "hola soy un cadena"
# string2 = "hola soy un"
# string3 = "hola"

# print(string1)

# nuestraVariable = "holAAAA a todOs"

# centralizar = nuestraVariable.capitalize()

# mayuscula = nuestraVariable.upper()
# minuscula = nuestraVariable.lower()

# print(minuscula)

# a = 5
# b = 7
# c = a + b 

# print(c)

# numero = 10
# numero += 10

# print(numero)

# nombre = "kevin"
# saludo = "bienvenido al olimpo"

# saludo_glorioso = nombre + ", " + saludo
# saludo_glorioso2 = f"bienvenido {nombre} al olimpo"
# print(saludo_glorioso)
# print(saludo_glorioso2)

# edad = int(input("cual es tu edad: "))
# if edad >= 18:
#     print("puedes pasar")
# else:
#     print("no puedes pasar")

# print("Bienvenido profesor, ingrese las notas de su feo estudiante")

# print("ingrese las 3 notas")
# nota1= float(input("nota 1: "))
# nota2= float(input("nota 2: "))
# nota3= float(input("nota 3: "))

# promedio3notas = round((nota1 + nota2 + nota3)/3, 2)  # redondea a 2 decimales


# if promedio3notas > 3.9:
#     print("de alguna manera paso de curso con: ",promedio3notas)
# else:
#     print("su estudiante reprobo con: ",promedio3notas)

# miLista = ["kevin","estudiante", 26, 3.00, "curso de programacion"]
# print(miLista[2])

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# numeros.append(11)
# numeros.remove(5)

# print(numeros)

# print("operaciones matematicas!, veremos ejemplos de suma, resta, multiplicar y dividir")
# print("ingresa 2 numeros para ver los ejemplos")
# numero1 = float(input("numero 1: "))
# numero2 = float(input("numero 2: "))

# suma = numero1+numero2
# resta = numero1-numero2
# multiplicacion = numero1*numero2
# division = numero1/numero2

# print("esto es lo que puedes hacer con tus numeros!")
# print("con sumas los numeros: ", numero1," + ",numero2, " es: ",suma)
# print("con resta los numeros: ", numero1," + ",numero2, " es: ",resta)
# print("con multiplicacion los numeros: ", numero1," + ",numero2, " es: ",multiplicacion)
# print("con division los numeros: ", numero1," + ",numero2, " es: ",division)

# print("bienvenido al inventario esclavo de la sociedad, este es nuestro inventario (●'◡'●).")

# productos = ["Mouse inalámbrico", "Teclado mecánico", "Monitor LG 24''", "Disco SSD 480GB"]
# precios = [15.99, 39.99, 129.99, 42.50]
# existencias = [25, 10, 7, 14]

# for i in range(len(productos)):
#     print(f"{productos[i]} | ${precios[i]} | Stock: {existencias[i]} | valor total del inventario: ${precios[i]*existencias[i]:.2f}")
#     print("="*40)

# class Mago:
#     def __init__(self, nombre, hp, energia):
#         self.nombre = nombre
#         self.hp = hp
#         self.energia = energia
        

#     def mostrar_nombre(self):
#         print(f"El nombre del mago es {self.nombre}")
#         print(f"sus puntos de vida son: {self.hp} HP")
#         print(f"sus puntos de energia son {self.energia} EP")

# # Crear un objeto de la clase Mago
# mago1 = Mago("Gandalf", hp=100, energia=10)
# mago1.mostrar_nombre()

from Producto import Sandwish

# Ejemplo de uso, tiene un nombre de pan, precio y multiples ingredientes en un arreglo
# nombre de la funcion: pedido


s = Sandwish("Pollo BBQ", 150, ["pollo", "barbacoa", "queso", "lechuga"])
s.pedido()

mi_sandwish = Sandwish("Carne Queso", 20000,["carne","queso","pan blanco"])
mi_sandwish.pedido()




