"""Ejercicio 1:
programa para verificar si una persona 
es mayor de edad"""

print("---------------------------")
print("---------MAYOR DE EDAD-----")
print("---------------------------")

# input
edad = int(input("Digite la edad: "))

# processing
if edad >= 18:
    print("la persona es MAYOR DE EDAD")
else:
    print("la persona es MENOR DE EDAD")