import os
import time
import pathlib

# Animación de entrada
for _ in range(10):
    print('.', end=" ", flush=True)
    time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo

directorio_actual = os.getcwd()

while True:
    # Título del software
    print(r"""
 ____  __ __  ______  __ __   ___   ____       _____  ____  _        ___   
|    \|  T  T|      T|  T  T /   \ |    \     |     |l    j| T      /  _]  
|  o  )  |  ||      ||  l  |Y     Y|  _  Y    |   __j |  T | |     /  [_   
|   _/|  ~  |l_j  l_j|  _  ||  O  ||  |  |    |  l_   |  | | l___ Y    _]  
|  |  l___, |  |  |  |  |  ||     ||  |  |    |   _]  |  | |     T|   [_   
|  |  |     !  |  |  |  |  |l     !|  |  |    |  T    j  l |     ||     T  
l__j  l____/   l__j  l__j__j \___/ l__j__j    l__j   |____jl_____jl_____j  
                                                                           
 ___ ___   ____  ____    ____   ____    ___  ___ ___    ___  ____   ______ 
|   T   T /    T|    \  /    T /    T  /  _]|   T   T  /  _]|    \ |      T
| _   _ |Y  o  ||  _  YY  o  |Y   __j /  [_ | _   _ | /  [_ |  _  Y|      |
|  \_/  ||     ||  |  ||     ||  T  |Y    _]|  \_/  |Y    _]|  |  |l_j  l_j
|   |   ||  _  ||  |  ||  _  ||  l_ ||   [_ |   |   ||   [_ |  |  |  |  |  
|   |   ||  |  ||  |  ||  |  ||     ||     T|   |   ||     T|  |  |  |  |  
l___j___jl__j__jl__j__jl__j__jl___,_jl_____jl___j___jl_____jl__j__j  l__j  
                                                                           
  _____   __  ____   ____  ____  ______  _____                             
 / ___/  /  ]|    \ l    j|    \|      T/ ___/                             
(   \_  /  / |  D  ) |  T |  o  )      (   \_                              
 \__  T/  /  |    /  |  | |   _/l_j  l_j\__  T                             
 /  \ /   \_ |    \  |  | |  |    |  |  /  \ |                             
 \    \     ||  .  Y j  l |  |    |  |  \    |                             
  \___j\____jl__j\_j|____jl__j    l__j   \___j                             
""")
    print("[+]crear un archivo")
    print("[+]crear una carpeta")
    print("[+]cambiar de color")
    print("[+]ver archivos o carpetas")
    print("[+]ver archivos o carpetas de dicha ruta")
    print("[+]borrar archivos")
    print("[+]borrar carpetas")
    print("[+]moverse de escritorio")
    print("[+]mover archivos")
    print("[--]help")
    respuesta = input(": ")
    if respuesta == "1":
        texto_archivo = input("texto que va dentro del archivo : ")
        print("coloque tambien el tipo de extencion (ejemplo '.txt, .html , .js , .cpp , .py , etc') : ")
        nombre_archivo = input("nombre del archivo : ")
        comando_archivo = f"echo \"{texto_archivo}>{nombre_archivo}\""
        os.system(f"echo {texto_archivo}>{nombre_archivo}")
        input("presione enter para continuar....")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    elif respuesta == "2":
        nombre_carpeta = input("nombre de la carpeta : ")
        comando_carpeta = f"mkdir \"{nombre_carpeta}\""
        os.system(comando_carpeta)
        input("presione enter para continuar....")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    elif respuesta == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("#"*55)
        print("1)azul")
        print("2)verde")
        print("3aqua")
        print("4)rojo")
        print("5)purpura")
        print("6)amarillo")
        print("7)gris")
        print("#"*55)
        color_change = input(": ")
        if color_change == "1":
            print("cambiando de color")
            for i in range(3):
                print(".", end=" ",flush=True)
                time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('color 1')
            input("presione enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif color_change == "2":
            print("cambiando de color")
            for i in range(3):
                print(".", end=" ",flush=True)
                time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('color 2')
            input("presione enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif color_change == "3":
            print("cambiando de color")
            for i in range(3):
                print(".", end=" ",flush=True)
                time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('color 3')
            input("presione enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif color_change == "4":
            print("cambiando de color")
            for i in range(3):
                print(".", end=" ",flush=True)
                time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('color 4')
            input("presione enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif color_change == "5":
            print("cambiando de color")
            for i in range(3):
                print(".", end=" ",flush=True)
                time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('color 5')
            input("presione enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif color_change == "6":
            print("cambiando de color")
            for i in range(3):
                print(".", end=" ",flush=True)
                time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('color 6')
            input("presione enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif color_change == "7":
            print("cambiando de color")
            for i in range(3):
                print(".", end=" ",flush=True)
                time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('color 8')
            input("presione enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            input("")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    elif respuesta == "4":
        os.system("dir")
        input("presione enter para continuar....")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif respuesta == "5":
        ruta_ver = input("Coloque la ruta que desea ver (ejemplo C:/Ruta/A/La/Carpeta): ")
        #Asegurarse de que la ruta esté entre comillas dobles para manejar espacios
        comando = f'dir "{ruta_ver}"'
        # Ejecutar el comando dir
        os.system(comando)
        # Esperar la entrada del usuario para continuar
        input("Presione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif respuesta == "6":
        nombre_archivo_borrar = input("coloque el nombre del archivo y su extencion : ")
        comando_archivo_borrar = f"del {nombre_archivo_borrar}"
        os.system(comando_archivo_borrar)
        input("Presione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif respuesta == "7":
        nombre_carpeta_borrar = input("coloque el nombre de la carpeta : ")
        comando_carpeta_borrar = f"rmdir /s {nombre_carpeta_borrar}"
        os.system(comando_carpeta_borrar)
        input("Presione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif respuesta == "8":
        nuevo_directorio = input("coloque (C:/ruta/a/la/carpeta) : ")
        if os.path.isdir(nuevo_directorio):
            directorio_actual = nuevo_directorio
            os.chdir(directorio_actual)
            print(f"directorio cambiado a {directorio_actual}")
        else:
            print("La ruta especificada no es válida.")
            input("Presione Enter para continuar....")
            os.system('cls' if os.name == 'nt' else 'clear')
    elif respuesta == "9":
        # Solicitar la ruta de destino y el archivo a mover
        directorio = input("Coloque la ruta de destino (ejemplo C:/ruta/a/mover): ")
        archivo = input("Coloque el nombre del archivo con su extensión (ejemplo archivo.txt): ")
        # Verificar si el archivo existe en el directorio actual
        if not os.path.isfile(archivo):
            print(f"El archivo {archivo} no existe en el directorio actual.")
        else:
                comando_mover = f"move {archivo} {directorio}"
        os.system(comando_mover)
        # Limpiar la pantalla
        input("Presione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif respuesta == "help":
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system("color 4" if os.name == 'nt' else '"\033[31m", end=""')
        print("para moverse en rutas de los archivos es (C:/users/'nombreDeTuDispositivo'/desktop/rutaDeArchivoDeseado') \n tambien puedes escribir (C:/users/rutaDeArchivoDeseado) \n tambien puedes escribir (C:/users/'nombreDeTuDispositivo'/rutaDeArchivoDeseado)")
        print("\n al crear o borrar un archivo, coloquele al final un '.NombreDeLaExtencion' => (ejemplo.txt ; ejemplo.cpp ; ejemplo.py ; ejemplo.js ; ejemplo.css , ETC) ")
        input("Presione Enter para continuar...")
        os.system("color 7" if os.name == 'nt' else '"\033[37m", end=""')
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        input("")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo