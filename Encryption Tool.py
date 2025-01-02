ROKE = "|"*50
line = "\n"

try:
        import time
        import getpass
        from getpass import getpass
        import socket
        from colorama import Fore, Style
        import pyfiglet
        import requests
        import platform
        import os
        import datetime
        from pystyle import *
except ModuleNotFoundError:
            os.system("pip install pyfiglet") 
            os.system("pip install colorama")    
            os.system("pip install pystyle") 

os.system("cls") # cleaer screen
#==========================================================================================
#==========================================================================================
#==========================================================================================

def Start_Tool () -> None :

    

    print(Fore.LIGHTGREEN_EX,pyfiglet.figlet_format('Encryption Tool',font="standard"))

    print("\33[39;0m")

    print (Fore.LIGHTRED_EX,""" 
    |||||||||||||||||||||||||||||||||||||||||||||                                       
    #                                           #
    #   BY | Mohammed Alaa                      #      
    #                                           #
    #   Tool Name | Encryption Tool             #
    #                                           #
    #   Date | 2025 - 1 - 1                     #
    #                                           #
    #   Language | {}                           #
    #                                           #
    |||||||||||||||||||||||||||||||||||||||||||||
    \33[39;0m""".format(set_user_language.title()))    




#==========================================================================================
#==========================================================================================
#==========================================================================================


# Check Your Platform is a Windows
def START () -> None :
    if platform.system() == 'Windows':

        ()
        
        # Import The Fun to Start Tool....
        Start_Tool()

    elif platform.system() == 'Linux':

        print("The system is Linux.")
        Start_Tool()


    else:
        print(f"The system is {platform.system()}. Exiting...")
        quit()

#==========================================================================================
#==========================================================================================
#==========================================================================================



def __Options__ () -> None :

    Write.Print (""+"System Check [■■■■■■■■■■] 100% \nModels Check [■■■■■■■■■■] 100% \nLast Update Check [■■■■□□□□□□] 40% \nAll Steps [■■■□□□□] 50%\n\b"*1,Colors.green,interval=.030)

    while True :

        user_options = ("""\33[36;1m
        1 - Set File To Encryption as [.txt]
        2 - Set File To Dec as [.txt]
        3 - Set File To Set Passcode as ["*"]
        4 - Set File To Checking All Details as [.py]
        5 - If You Want Tool Edit 
        0 - Exit
        \33[39;0m""")

        print(user_options)

        user_set = input ('\f\n\33[96;1m[\33[39;0m\33[91;1m-\33[39;0m\33[36;1m]\33[39;0m\33[3;1m Choose Number of The List -> \33[39;0m')


        if user_set == '1' :

            host = socket.gethostname()
            ip = socket.gethostbyname(host)

            print(Fore.LIGHTRED_EX,"\nPC Name --> {} \n\nIP Add --> {}\n".format(host,ip))    
            print("\33[39;0m")
            print("{}".format(ROKE))

        elif user_set == '2' :

            pass


        elif user_set == '5':
        
            LUI_SAVE = []
            username = input ("\n[→] Set a Username of Your Account GitHub | ")
            code = getpass ("\n[→] Set a Password Account GitHub | ")
        
            LUI_SAVE.append(username)
            LUI_SAVE.append(code)

            # print("\33[92;1m\nYour Username is a --> [{}] ⇄ Passcode is a --> [{}] \33[39;0m".format(username,code))
            
            print(Fore.LIGHTBLUE_EX,"\nAll Data is at Save...")

            # print(LUI_SAVE)

        elif user_set == '':

            print("\n\33[33;1m [❌] Choose a Number of Liste...\33[39;0")


        elif user_set == '0':
            break
        else:
            print("\n\t\33[91;1m Number Not Found of a List")
#==========================================================================================         #==========================================================================================   
#==========================================================================================


                                                # ================= This is a Main Tool ======================


set_user_language = input("\33[96;1m[\33[39;0m\33[91;1m-\33[39;0m\33[36;1m]\33[39;0m Set A You Need Use Language...[EN / AR] : \33[39;0m").lower()
if set_user_language == '': 

        choose = Write.Print("\n [→] Please Set a Format Language To Start or Set -h To Help... or set -ex To Exit\n\n\n",Colors.yellow,interval=.05)

elif set_user_language == '-h':

            print("\n\33[95;1m [→] Please Set Formating a Language To Use Tool...\n\33[39;0m")

elif set_user_language != 'ar' and set_user_language != 'en':
            
            print("\n\33[92;1m [X] Please Set a Language...\n\33[39;0m")
            exit()
        
elif set_user_language == 'ar' or set_user_language == 'en':
            START()
            __Options__()

elif set_user_language == '-ex':

            quit()

