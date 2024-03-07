import os
import shutil

def limpiar_carpeta(carpeta, mantener_cada_x):
    """
    Función que mantiene uno de cada mantener_cada_x elementos de una carpeta
    """
    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(carpeta)
    
    # Contador para mantener uno de cada x elementos
    contador = 0
    
    # Iterar sobre los archivos en la carpeta
    for archivo in archivos:
        # Verificar si es un archivo (no un directorio)
        if os.path.isfile(os.path.join(carpeta, archivo)):
            # Mantener solo uno de cada x elementos
            if contador % mantener_cada_x != 0:
                # Eliminar el archivo
                os.remove(os.path.join(carpeta, archivo))
            contador += 1

# Ruta de la carpeta a limpiar
carpeta_a_limpiar = "/home/lucia/Siali/Datasets/Carretillas gsk/dat_almacen_pas_carret/train (copia reducida)/labels_mod"

# Número de elementos a mantener
mantener_cada_x = 6

# Llamar a la función para limpiar la carpeta
limpiar_carpeta(carpeta_a_limpiar, mantener_cada_x)
