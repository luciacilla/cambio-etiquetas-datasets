"""
Script para recortar las imagenes y quedarnos unicamente con la caja como imagen
"""
import os
import cv2
import matplotlib.pyplot as plt

def recortar_imagen(imagen, etiquetas, carpeta_destino):
    # Leer la imagen
    img = cv2.imread(imagen)
    ancho_or = img.shape[0]
    alto_or  = img.shape[1]
    
    # Leer las etiquetas del archivo de texto
    with open(etiquetas, 'r') as file:
        for linea in file:
            valores = linea.split()
            if len(valores) >= 5:  # Verificar si hay suficientes valores
                clase = valores[0].strip()  # Clase
                x_centro, y_centro = map(float, valores[1:3])  # Posición x e y del centro
                ancho, alto = map(float, valores[3:5])  # Ancho y alto de la caja
                
                # Calcular las coordenadas de la esquina superior izquierda y la esquina inferior derecha
                x1 = int( (x_centro - ancho / 2) * ancho_or)
                y1 = int((y_centro - alto / 2) * alto_or)
                x2 = int((x_centro + ancho / 2) * ancho_or)
                y2 = int((y_centro + alto / 2) * alto_or)

                
                # Recortar la región de interés de la imagen
                img_copy = img.copy()

                trozo = img_copy[y1:y2, x1:x2]
 
                # Generar la ruta de la carpeta de destino basada en la clase
                carpeta_clase = os.path.join(carpeta_destino, clase)
                os.makedirs(carpeta_clase, exist_ok=True)
                
                # Generar el nombre de la imagen recortada
                nombre_trozo = os.path.splitext(os.path.basename(imagen))[0] + f"_{x1}_{y1}_{x2}_{y2}.jpg"
                ruta_trozo = os.path.join(carpeta_clase, nombre_trozo)
                
                # Guardar el trozo recortado
                cv2.imwrite(ruta_trozo, trozo)


            else:
                print("La línea no contiene suficientes valores:", valores)

# Directorio de las imágenes y archivos de etiquetas
directorio_imagenes = "/home/lucia/uni/practicas formacion/Datasets caidas/Dataset_total/valid (copia)/images"
directorio_etiquetas = "/home/lucia/uni/practicas formacion/Datasets caidas/Dataset_total/valid (copia)/labels"

# Carpeta de destino para las imágenes recortadas
carpetas_destino = {
    '0': "/home/lucia/uni/practicas formacion/Datasets caidas/Dataset_total/valid (copia)",
    '1': "/home/lucia/uni/practicas formacion/Datasets caidas/Dataset_total/valid (copia)",
    '2': "/home/lucia/uni/practicas formacion/Datasets caidas/Dataset_total/valid (copia)"
}

# Listar los archivos de imágenes y etiquetas
archivos_imagenes = os.listdir(directorio_imagenes)
archivos_etiquetas = os.listdir(directorio_etiquetas)

# Recorrer cada par de archivos de imagen y etiquetas
for imagen in archivos_imagenes:
    nombre_imagen, extension = os.path.splitext(imagen)
    ruta_imagen = os.path.join(directorio_imagenes, imagen)
    # Verificar si hay un archivo de etiquetas correspondiente
    if nombre_imagen + ".txt" in archivos_etiquetas:
        ruta_etiquetas = os.path.join(directorio_etiquetas, nombre_imagen + ".txt")
        # Recortar la imagen basada en las etiquetas y guardar los trozos recortados
        for clase, carpeta_destino in carpetas_destino.items():
            recortar_imagen(ruta_imagen, ruta_etiquetas, carpeta_destino)
