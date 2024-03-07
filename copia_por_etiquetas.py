import os
import shutil

def copiar_imagenes_y_etiquetas_con_etiquetas(origen_imagenes, origen_etiquetas, destino_imagenes, destino_etiquetas, etiquetas_objetivo):
    
    """
    codigo copia en otras carpetas de imagen y etiquetas aquellas imagenes y etiquetas que tengan la etiqueta que yo elija
    """

    # Verificar y crear el directorio de destino si no existe
    if not os.path.exists(destino_imagenes):
        os.makedirs(destino_imagenes)
    if not os.path.exists(destino_etiquetas):
        os.makedirs(destino_etiquetas)

    # Obtener la lista de imágenes en el directorio de origen
    imagenes = [f for f in os.listdir(origen_imagenes) if f.endswith(('.jpg', '.png', '.jpeg'))]

    # Iterar sobre cada imagen y su etiqueta asociada
    for imagen in imagenes:
        nombre_base = os.path.splitext(imagen)[0]
        etiqueta_path = os.path.join(origen_etiquetas, nombre_base + '.txt')

        # Verificar si la etiqueta existe y contiene todas las etiquetas objetivo
        if os.path.exists(etiqueta_path):
            with open(etiqueta_path, 'r') as etiqueta_file:
                etiquetas = etiqueta_file.readlines()
                clases = [etiqueta.split()[0] for etiqueta in etiquetas]
                if all(etiqueta_obj in clases for etiqueta_obj in etiquetas_objetivo):
                    # Copiar la imagen y la etiqueta a las carpetas de destino
                    shutil.copy(os.path.join(origen_imagenes, imagen), destino_imagenes)
                    shutil.copy(etiqueta_path, destino_etiquetas)

# Directorios de origen y destino
origen_imagenes = "/home/lucia/Siali/Datasets/Carretillas gsk/dat_alm_carr_europ_muc_etiq/train (copia)/images"
origen_etiquetas = "/home/lucia/Siali/Datasets/Carretillas gsk/dat_alm_carr_europ_muc_etiq/train (copia)/labels"
destino_imagenes = "/home/lucia/Siali/Datasets/Carretillas gsk/dat_alm_carr_europ_muc_etiq/train (copia)/images_forkl"
destino_etiquetas = "/home/lucia/Siali/Datasets/Carretillas gsk/dat_alm_carr_europ_muc_etiq/train (copia)/labels_forkl"

# Etiquetas objetivo que deseas buscar
etiquetas_objetivo = ["1"]

# Llamar a la función para copiar imágenes y etiquetas
copiar_imagenes_y_etiquetas_con_etiquetas(origen_imagenes, origen_etiquetas, destino_imagenes, destino_etiquetas, etiquetas_objetivo)
