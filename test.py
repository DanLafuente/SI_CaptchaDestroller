from PIL import Image


directorio_input = 'samples/'
directorio_output = 'samples_transform/'
def convertir_imagen(ruta_input, ruta_output, dimension=(200, 50)):

    # Abrir imagen
    imagen = Image.open(ruta_input)
    
    # Cambiar tamaño
    imagen = imagen.resize(dimension)
    
    # Convertir a blanco y negro
    imagen_bn = imagen.convert('L')  # 'L' es modo de 8 bits en escala de grises
    
    # Guardar la nueva imagen
    imagen_bn.save(ruta_output)


# Convertir 'test' imagenes a blanco y negro y tamaño 200x50
for nombre_archivo in os.listdir(directorio_input):
    break

    # Convertir todas las imagenes del directorio a blanco y negro y dimension establecidos
    archivo_original = directorio_input + nombre_archivo
    archivo_nuevo = directorio_output + nombre_archivo
    nDataset = nDataset + 1
    convertir_imagen(archivo_original, archivo_nuevo)
    matriz = imagen_a_matriz(archivo_nuevo)

    ## mostrar_matriz(matriz)

print("HOLA")