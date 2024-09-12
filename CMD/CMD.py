import time
import os

# Animación de entrada
for _ in range(10):
    print('.', end=" ", flush=True)
    time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo

while True:
    #titulo del software
    print(r"""

 ▄████████   ▄▄▄▄███▄▄▄▄   ████████▄              
███    ███ ▄██▀▀▀███▀▀▀██▄ ███   ▀███             
███    █▀  ███   ███   ███ ███    ███             
███        ███   ███   ███ ███    ███             
███        ███   ███   ███ ███    ███             
███    █▄  ███   ███   ███ ███    ███             
███    ███ ███   ███   ███ ███   ▄███             
████████▀   ▀█   ███   █▀  ████████▀              
                                                  
    ███        ▄████████    ▄██████▄     ▄████████
▀█████████▄   ███    ███   ███    ███   ███    ███
   ▀███▀▀██   ███    ███   ███    █▀    ███    █▀ 
    ███   ▀   ███    ███  ▄███          ███       
    ███     ▀███████████ ▀▀███ ████▄  ▀███████████
    ███       ███    ███   ███    ███          ███
    ███       ███    ███   ███    ███    ▄█    ███
   ▄████▀     ███    █▀    ████████▀   ▄████████▀ 

""")
    print("/*opciones 1-10*/")
    print("[+]ver Ipv4")
    print("[+]ver mi usuario")
    print("[+]cambiar de color")
    print("[+]lista de red wifis")
    print("[+]ver redes wifi a las que te conctastes anteriormente")
    print("[+]ver el almacenamiento")
    print("[+]ver informacion del sistema")
    print("[+]estado de la red")
    print("[+]ver servicios activos")
    print("[+]ver tareas en ejecucion")
    respuesta = input(": ")
    if respuesta == "1":
        os.system('ipconfig')  # Ejecuta el comando para Windows
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    elif respuesta == "2":
        os.system('net user')  # Ejecuta el comando para Windows
        input("Presiona Enter para continuar...")
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
        os.system("netsh wlan show networks")
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    elif respuesta == "5":
        os.system("netsh wlan show profiles")
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    elif respuesta == "6":
        os.system("wmic logicaldisk get size,freespace,caption")
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    elif respuesta == "7":
        os.system("systeminfo")
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    elif respuesta == "8":
        os.system("netstat")
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    elif respuesta == "9":
        os.system("net start")
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    elif respuesta == "10":
        os.system("tasklist")
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        input("")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo