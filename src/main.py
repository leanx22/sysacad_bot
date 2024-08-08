from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

import os
import time

from colors import *
from data import botData as consts
from functions import *

exit = False
user_id = ""
user_password = ""

while exit == False:
    os.system("cls")

    print(tcolors.OKCYAN+tcolors.BOLD+"BOT PARA CAMPEAR EL SYSACAD [LEAN] - [V"+str(consts.BOT_VERSION)+"]"+tcolors.RESET)
    time.sleep(1)

    print(tcolors.BOLD+tcolors.OKCYAN+"MENU PRINCIPAL: ")
    print("Usuario actual: "+user_id+"\n"+tcolors.RESET)
    print(tcolors.OKCYAN+"1. Configurar inicio de sesión.\n"+
        "2. Comenzar a campear.\n"+
        "3. Salir.\n")
    option = input("Seleccion: ")
    match option:        
        case "1":
            os.system("cls")            
            user_id = input("Ingresá tu legajo: ")
            user_password = input("Ingresá tu contraseña de sysacad: ")
            continue
        case "2":
            start_camp(user_id, user_password)
            break
        case "3":
            os.system("cls")
            print(tcolors.OKCYAN+"Saliendo del programa...")
            exit = True
            break
        case other:
            print(tcolors.FAIL+"Opción inválida.")
            input("Presioná ENTER para continuar...")
            os.system("cls")


sys.exit(0)