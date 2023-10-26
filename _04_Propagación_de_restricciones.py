# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# instalar el módulo python-constraint. 
pip install python-constraint


# problema de asignación de colores a regiones en un mapa:
from constraint import Problem, AllDifferentConstraint

# Crear una instancia de un problema CSP
problem = Problem()

# Definir variables y sus dominios
regions = ["A", "B", "C", "D"]
colors = ["Red", "Green", "Blue"]

problem.addVariables(regions, colors)

# Definir restricciones
def not_adjacent(region1, region2, color1, color2):
    return region1 != region2 or color1 != color2

problem.addConstraint(AllDifferentConstraint(), regions)
problem.addConstraint(not_adjacent, ("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "D"))

# Encontrar una solución
solutions = problem.getSolutions()

# Mostrar las soluciones encontradas
for solution in solutions:
    print(solution) 
