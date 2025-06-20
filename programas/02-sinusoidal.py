#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from GeneradorOndas import GeneradorOndas

NOMBRE_ARCHIVO="02-sinusoidal.png"
if __name__=="__main__":
    g=GeneradorOndas("Onda sinusoidal", "Tiempo (s)", "Amplitud", 1000, 0,2)
    g.anadir_serie(2, 1, "Onda 1")
    g.guardar_grafico(NOMBRE_ARCHIVO)
