
#CASO Sistema de matricula UNSCH
#Primer diseño con herencia multiple
class Matricula:
    def calcular_monto(self):
        return 60.00

class MatriculaExtemporanea(Matricula):
    def calcular_monto(self):
        return super().calcular_monto() + 15.00

class IndiceDesaprobatorio(Matricula):
    def calcular_monto(self):
        return super().calcular_monto() + 15.00

class BecaViolenciaSociopolitica(Matricula):
    def calcular_monto(self):
        return super().calcular_monto() / 2

#Primera version del programador:
class MatriculaCombinada1( BecaViolenciaSociopolitica, IndiceDesaprobatorio, MatriculaExtemporanea):
    pass
#Segunda version del programador:
class MatriculaCombinada2(IndiceDesaprobatorio, MatriculaExtemporanea, BecaViolenciaSociopolitica):
    pass
#prueba con estudiantes con las mismas condiciones
luis = MatriculaCombinada1()
rosa = MatriculaCombinada2()

print("Prueba n1")
print("Monto de Luis:")
print(f"Monto pagado por Luis: S/ {luis.calcular_monto():.2f}")
print("Monto de Rosa:")
print(f"Monto pagado por Rosa: S/ {rosa.calcular_monto():.2f}")


#En la primera versión, Python resuelve el cálculo siguiendo el 
# orden: beca, índice desaprobatorio, matrícula extemporánea y matrícula general. 
# Sin embargo, al retornar el resultado, primero aplica los recargos y 
# finalmente la beca, por lo que Luis paga S/ 45.00: \((60 + 15 + 15) / 2\). En la segunda 
# versión, el orden es índice desaprobatorio, matrícula extemporánea, beca y matrícula 
# general; por ello primero se aplica la beca y después los recargos, 
# haciendo que Rosa pague S/ 60.00: \((60 / 2) + 15 + 15\). La diferencia ocurre 
# porque super() sigue el orden de resolución de métodos o MRO, determinado por el 
# orden de las clases en la herencia múltiple. Ninguno de los programadores 
# cometió un error de sintaxis, ya que ambas jerarquías son válidas para Python; el 
# problema es que no se definió la regla de negocio sobre cuándo aplicar la beca. 
# Si se intentara escribir primero la clase general, por ejemplo 
# class MatriculaIncorrecta(Matricula, BecaViolenciaSociopolitica), 
# Python mostraría un TypeError, porque la clase de beca ya hereda de Matricula y 
# se produciría un conflicto en el orden de herencia.

#Rediseño sin herencia multiple
class MatriculaRedisenada:
    def __init__(self, nombre_estudiante):
        self.nombre_estudiante = nombre_estudiante
        self.monto = 60.00

    def aplicar_extemporanea(self):
        self.monto += 15.00

    def aplicar_indice_desaprobatorio(self):
        self.monto += 15.00

    def aplicar_beca(self):
        self.monto /= 2

    def calcular_monto(self, orden_reglas):
        self.monto = 60.00
        for regla in orden_reglas:
            if regla == "extemporanea":
                self.aplicar_extemporanea()

            elif regla == "indice_desaprobatorio":
                self.aplicar_indice_desaprobatorio()

            elif regla == "beca":
                self.aplicar_beca()

        return self.monto


print("\nRediseño propuesto")
print("Prueba n2")
print("Aplicacion: primero los recargos y luego la beca")
orden_beca_al_final = ["extemporanea", "indice_desaprobatorio", "beca"]

estudiante1 = MatriculaRedisenada("Luis")

monto1 = estudiante1.calcular_monto(orden_beca_al_final)

print(f"{estudiante1.nombre_estudiante}")
print(f"Beca aplicada al final: S/ {monto1:.2f}")


print("\nAplicacion: primero la beca y despues los recargos")
orden_beca_al_inicio = ["beca", "extemporanea", "indice_desaprobatorio"]

estudiante2 = MatriculaRedisenada("Rosa")

monto2 = estudiante2.calcular_monto(orden_beca_al_inicio)

print(f"{estudiante2.nombre_estudiante}")
print(f"Beca aplicada al inicio: S/ {monto2:.2f}")