# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# instalar la biblioteca PuLP
pip install pulp

from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Datos del problema
longitud_bobina = 100
demandas = [20, 15, 10]
longitudes_restantes = [longitud_bobina] * len(demandas)
n = len(demandas)

# Crear un problema de programaci�n lineal entera
problem = LpProblem("Problema de Corte", LpMaximize)

# Crear variables
x = [LpVariable(f"x{i}", lowBound=0, upBound=demandas[i], cat="Integer") for i in range(n)]

# Funci�n objetivo
problem += lpSum(x), "M�xima utilizaci�n de la bobina"

# Restricciones
for i in range(n):
    problem += x[i] <= demandas[i], f"Demanda m�xima {i}"
    problem += lpSum(x[i] * demandas[i] for i in range(n)) <= longitud_bobina, "M�xima longitud de la bobina"

# Resolver el problema
problem.solve()

# Imprimir la soluci�n
print("Estado:", problem.status)
print("Soluci�n �ptima:", LpMaximize if problem.status == 1 else "No encontrada")

if problem.status == 1:
    for i in range(n):
        print(f"Bobina {i + 1}: {int(x[i].varValue)} piezas")
