

try:
        import time
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
    |||||||||||||||||||||||||||||||||||||||||                                       
    #                                       #
    #   BY | Mohammed Alaa                  #
    #                                       #
    #   Tool Name | Encryption Tool         #
    #                                       #
    #   Date | 2025 - 1 - 1                 #
    #                                       #
    #   Language | {}                       #
    #                                       #
    |||||||||||||||||||||||||||||||||||||||||
    \33[39;0m""".format(set_user_language))    




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


    else:
        print(f"The system is {platform.system()}. Exiting...")
        quit()

#==========================================================================================
#==========================================================================================
#==========================================================================================

def AR_LANG (lang= False) -> None:
            
            if set_user_language == "en":

                return lang 

            pass



def EN_LANG (lang = False) -> None:

            return lang

            pass


set_user_language = input("\33[96;1m[\33[39;0m\33[91;1m-\33[39;0m\33[36;1m]\33[39;0m Set A You Need Use Language...[EN / AR] : \33[39;0m")
if set_user_language == '': 

        choose = Write.Print("\n [→] Please Set a Format Language To Start or Set -h To Help... or set -ex To Exit\n\n\n",Colors.yellow,interval=.05)

elif set_user_language == '-h':

            print("\n\33[95;1m [→] Please Set Formating a Language To Use Tool...\n\33[39;0m")

elif set_user_language != 'ar' and set_user_language != 'en':
            
            print("\n\33[92;1m [X] Please Set a Language...\n\33[39;0m")
            exit()
        
elif set_user_language == 'ar' or set_user_language == 'en':

            START()

elif set_user_language == '-ex':

            quit()