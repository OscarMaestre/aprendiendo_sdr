#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from GeneradorOndas import GeneradorOndas

NOMBRE_ARCHIVO="02-cosinusoidal.png"
if __name__=="__main__":
    g=GeneradorOndas("Onda cosinusoidal", "Tiempo (s)", "Amplitud", 1000, 0,2)
    g.anadir_serie_coseno(2, 1, "Onda coseno")
    g.guardar_grafico(NOMBRE_ARCHIVO)
