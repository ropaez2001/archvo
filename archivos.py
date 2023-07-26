"""▪ 1- Escribir un programa que abra un archivo, lea todas sus líneas y cuente cuantas
líneas existen en el mismo"""

""""def contar_lineas(archivo):
    file=open(archivo, 'r') 
    lineas = file.readlines()
        
    return len(lineas)

nombre_archivo = 'archivo.txt'  

cantidad_lineas = contar_lineas(nombre_archivo)
print(f"El archivo {nombre_archivo} tiene {cantidad_lineas} líneas.")"""

"""▪ 2- Utilizar Python para escribir un archivo de texto que tenga 11 líneas, en cada una
escribir lo que deseen y cerrar el archivo. Luego mostrar el contenido del archivo."""


def contenido_Archivo(archivo):
    
    file=open(archivo, "r")
    line=file.readlines()
    
    
     
    return archivo
nombre_archivo = 'archivo.txt'
leer_contenido=contenido_Archivo(nombre_archivo)
print(nombre_archivo)

