import numpy as np
import matplotlib.pyplot as plt


class GeneradorOndas(object):
    def __init__(self, titulo, xlabel, ylabel, num_muestras, x_minimo, x_maximo):
        self.titulo=titulo
        self.xlabel=xlabel
        self.ylabel=ylabel
        self.num_muestras=num_muestras
        self.x_minimo=x_minimo
        self.x_maximo=x_maximo
        self.tiempo=np.linspace(x_minimo, x_maximo, num_muestras) 
        self.series=[]
        self.titulo=[]
        self.colores=["red", "green", "blue", "black", "cyan", "magenta"]
    
    def anadir_serie(self, amplitud, frecuencia, titulo):
        onda = amplitud * np.sin(2 * np.pi * frecuencia * self.tiempo)
        self.series.append(onda)
        self.titulo.append(titulo)
    
    def anadir_serie_np(self, np, titulo):
        self.series.append(np)
        self.series.append(titulo)

    def guardar_grafico(self, nombre_archivo):
        # Configuración de la figura
        fig = plt.figure(figsize=(10, 5))
        plt.title("Onda Sinusoidal", fontsize=14)
        plt.xlabel("Tiempo (s)", fontsize=12)
        plt.ylabel("Amplitud", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)

       
        for (serie, titulo, color) in zip(self.series, self.titulo, self.colores):
            # Dibujar la onda
            plt.plot(self.tiempo, serie, color, linewidth=2, label=titulo)
        
        plt.axhline(0, color='black', linewidth=0.5)
        plt.legend(loc='upper right')

        # Guardar la imagen (sin mostrar)
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')

        # Cerrar la figura para liberar memoria
        plt.close(fig)
