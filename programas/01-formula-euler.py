#!/usr/bin/python3
import sys
import math, cmath


def mostrar_informe(texto, valor):
    print(f"* {texto}, {valor:.2f}")
if __name__=="__main__":
    angulo             = float(sys.argv[1])
    exponente_complejo = complex(0, angulo)
    exponencial        = cmath.exp(exponente_complejo)
    coseno             = math.cos(angulo)
    seno               = math.sin(angulo)
    
    print("Resultados:")
    mostrar_informe("El ángulo pasado (se asume en radianes)", angulo)
    mostrar_informe("Exponente complejo", exponente_complejo)
    mostrar_informe("e ^ exponente_complejo", exponencial)
    mostrar_informe(f"El coseno de {angulo} radianes", coseno)
    mostrar_informe(f"El seno de {angulo} radianes", seno)