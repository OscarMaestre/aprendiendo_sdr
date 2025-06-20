#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from GeneradorOndas import GeneradorOndas

NOMBRE_ARCHIVO="03-distintas-amplitudes.png"
if __name__=="__main__":
    g=GeneradorOndas("Distintas amplitudes", "Tiempo (s)", "Amplitud", 1000, 0,2)
    g.anadir_serie(5, 1, "Onda seno")
    g.anadir_serie_coseno(2, 1, "Onda coseno")
    g.guardar_grafico(NOMBRE_ARCHIVO)
