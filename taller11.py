class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie


class Veterinaria:
    def __init__(self, nombre_negocio):
        self.nombre_negocio = nombre_negocio
        # Listas para almacenar los registros del día
        self.registro_peluqueria = []
        self.registro_clinica = []
        self.ventas_alimentos = []

    # Métodos para registrar actividades
    def registrar_peluqueria(self, mascota):
        self.registro_peluqueria.append(mascota)
        print(f"✔ {mascota.nombre} registrado para Peluquería.")

    def registrar_clinica(self, mascota, motivo):
        self.registro_clinica.append({"mascota": mascota, "motivo": motivo})
        print(f"✔ {mascota.nombre} registrado en Clínica por: {motivo}.")

    def registrar_venta_alimento(self, producto, monto):
        self.ventas_alimentos.append({"producto": producto, "monto": monto})
        print(f"✔ Venta registrada: {producto} (${monto}).")

    # Método para generar reportes al final del día
    def generar_reportes(self):
        print(f"\n--- REPORTE DIARIO: {self.nombre_negocio} ---")

        print("\n1. Peluquería (Baños y Cortes):")
        for m in self.registro_peluqueria:
            print(f"- {m.nombre} ({m.especie})")

        print("\n2. Atenciones Médicas:")
        for atencion in self.registro_clinica:
            m = atencion["mascota"]
            print(f"- {m.nombre} ({m.especie}) | Motivo: {atencion['motivo']}")

        print("\n3. Ventas de Alimentos:")
        total = 0
        for venta in self.ventas_alimentos:
            print(f"- {venta['producto']}: ${venta['monto']}")
            total += venta['monto']
        print(f"TOTAL VENTAS: ${total}")


# Inicializamos la veterinaria
mi_veterinaria = Veterinaria("PythonS.A.")

# Creamos algunas mascotas
pet1 = Mascota("Firulais", "Perro")
pet2 = Mascota("Michi", "Gato")
pet3 = Mascota("Rex", "Perro")

# Registramos movimientos del día
mi_veterinaria.registrar_peluqueria(pet1)
mi_veterinaria.registrar_clinica(pet2, "Vacunación anual")
mi_veterinaria.registrar_venta_alimento("Croquetas Premium 5kg", 45.0)
mi_veterinaria.registrar_peluqueria(pet3)
mi_veterinaria.registrar_venta_alimento("Sobre de alimento húmedo", 2.5)

# Generamos los reportes solicitados
mi_veterinaria.generar_reportes()