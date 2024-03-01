import os

def modificar_etiquetas(archivo_entrada, archivo_salida, mapeo_clases):
    """
    Modifica las etiquetas en un archivo de formato YOLO según el mapeo de clases dado.
    """
    print("Archivo de entrada:", archivo_entrada)
    print("Archivo de salida:", archivo_salida)
    with open(archivo_entrada, 'r') as f_entrada, open(archivo_salida, 'w') as f_salida:
        for linea in f_entrada:
            partes = linea.strip().split()
            if len(partes) < 5:
                # Verificar si la línea tiene el formato correcto (al menos cinco partes)
                print("Error: etiqueta no válida:", linea)
                continue
            
            clase_original = partes[0]
            if clase_original in mapeo_clases:
                # Reemplazar la clase original por la nueva clase según el mapeo
                nueva_clase = mapeo_clases[clase_original]
                partes[0] = nueva_clase
                # Escribir la línea modificada en el archivo de salida
                f_salida.write(' '.join(partes) + '\n')
                print("Etiqueta modificada:", partes)
            else:
                # Si la clase no está en el mapeo, conservar la etiqueta original
                f_salida.write(linea)


def modificar_etiquetas_multiples(directorio_entrada, directorio_salida, mapeo_clases):
    """
    Modifica las etiquetas en múltiples archivos de formato YOLO en un directorio.
    """
    # Verificar si el directorio de salida existe, si no, crearlo
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    # Iterar sobre cada archivo en el directorio de entrada
    for nombre_archivo in os.listdir(directorio_entrada):
        ruta_entrada = os.path.join(directorio_entrada, nombre_archivo)
        ruta_salida = os.path.join(directorio_salida, nombre_archivo)
        # Modificar las etiquetas para este archivo y guardarlas en el directorio de salida
        modificar_etiquetas(ruta_entrada, ruta_salida, mapeo_clases)


# Directorios de entrada y salida
directorio_entrada = "/home/lucia/uni/practicas formacion/Datasets caidas/Dataset 3 _ ['falls', 'sits', 'squats', 'stands']/valid/labels"
directorio_salida = "/home/lucia/uni/practicas formacion/Datasets caidas/Dataset 3 _ ['falls', 'sits', 'squats', 'stands']/valid/labels_mod"

# Diccionario para mapear clases antiguas a nuevas
mapeo_clases = {
    "0": "0",
    "1": "1",
    "2": "1",
    "3": "2"
}

# Modificar las etiquetas en múltiples archivos
modificar_etiquetas_multiples(directorio_entrada, directorio_salida, mapeo_clases)