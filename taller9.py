class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def data(self):
        if self.age >= 18 and self.gender == "F":
            print(f"{self.name} eres mayor de edad y eres del género femino")
        else:
            print(f"{self.name} no eres mayor de edad o no eres del género femino")

name = input("Ingrese su nombre: ")
gender = input("Ingrese su genero (M / F): ").upper()
age = int(input("Ingrese su edad: "))

person1 = Person(name, gender, age)
person1.data()

#####################################Ejercicio 2##############################################
class Empleado:
    def __init__(self, nombre, sueldo_bruto):
        self.nombre = nombre
        self.sueldo_bruto = sueldo_bruto

    def mostrar_resultado(self):
        impuesto_educativo = self.sueldo_bruto * 0.005  # 0.50%
        impuesto_renta = self.sueldo_bruto * 0.17  # 17%

        salario_neto = self.sueldo_bruto - (impuesto_educativo + impuesto_renta)

        print("\n--- RESULTADOS ---")
        print(f"Nombre: {self.nombre}")
        print(f"Salario Bruto: {self.sueldo_bruto}")
        print(f"Salario Neto: {salario_neto}")

nom = input("Ingrese su nombre: ")
sueldo = float(input("Ingrese su sueldo bruto: "))

persona = Empleado(nom, sueldo)
persona.mostrar_resultado()