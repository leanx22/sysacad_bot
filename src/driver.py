from prints import *

from selenium import webdriver

from selenium.webdriver.firefox.service import Service as fserv
from selenium.webdriver.chrome.service import Service as chserv

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import os
from os import system

def print_driver_config(configs):    
    exit_menu = False
    while exit_menu == False:
        system("cls")
        print_message("SELECCIÓN DE NAVEGADOR:\n",True)
        print_message("ACTUAL -> ["+configs.get("navegador")+"]:\n",True)
        print_message("Navegadores disponibles:\n")
        
        print_message("1. Chrome\n"
                      "2. Firefox\n"
                      "3. Volver",True)
        selection = get_user_input_option(3, "Selección: ", True, tcolors.FAIL+"Reingrese una selección válida: "+tcolors.RESET)
        match selection:
            case 1:
                configs["navegador"] = "chrome"
            case 2:
                configs["navegador"] = "firefox"
            case 3:
                exit_menu = True
                
    return configs

def get_driver(driver_name):
    driver = None
    driver_name = str(driver_name).lower()
    print("Cargando driver...\n")
    match driver_name:
        case "chrome":
            driver = webdriver.Chrome(service=chserv(ChromeDriverManager().install()))
        case "firefox":
            driver = webdriver.Firefox(service=fserv(GeckoDriverManager().install()))
        case other:
            driver = webdriver.Chrome(service=chserv(ChromeDriverManager().install()))
            print_error("Error al cargar driver, utilizando chrome por default.",True,True)
    return driver