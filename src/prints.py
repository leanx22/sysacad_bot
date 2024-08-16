from colors import *
from os import system as sys
from time import sleep

#OUTPUT
def print_welcome_message(time = 2, clear=True):
    print(tcolors.OKCYAN+tcolors.BOLD+"BOT DE AUTO-CAMPEO DE SYSACAD - [por LEAN]..."+tcolors.RESET)
    sleep(time)
    if clear:
        sys("cls")

def print_menu(clear=False):
    if clear:
        sys("cls")
    print(tcolors.OKCYAN+tcolors.BOLD+">>Menú"+tcolors.RESET)
    print(tcolors.OKCYAN+"1. Configuración.\n"
        "2. Iniciar tarea.\n"
        "3. Salir.\n")

def print_error(message, bold=False, wait_for_input=True):
    if(bold):
        print(tcolors.FAIL+tcolors.BOLD+message+tcolors.RESET,flush=True)
    else:
        print(tcolors.FAIL+message+tcolors.RESET,flush=True)

    if wait_for_input:
        input(">> Presioná ENTER para continuar <<")
    return

def get_formated_error_string(message, bold=False):
    if bold:
        return tcolors.FAIL+tcolors.BOLD+message+tcolors.RESET
    else:
        return tcolors.FAIL+message+tcolors.RESET

def print_message(message, bold=False, wait_for_input=False):
    if(bold):
        print(tcolors.OKCYAN+tcolors.BOLD+message+tcolors.RESET)
    else:
        print(tcolors.OKCYAN+message+tcolors.RESET)
    if wait_for_input:
        input(">> Presioná ENTER para continuar <<")

#INPUT
def get_user_input_option(count=1,input_message="Selección: ", inner_validation=False,error_message=tcolors.FAIL+tcolors.BOLD+"Opción inválida, reingrese: "+tcolors.RESET):
    user_input = input(input_message)
    try:
        user_input = int(user_input)
    except:
        return -1
    
    if(not inner_validation):
        if user_input > count or user_input < 1:
            return -1
        return user_input
    
    while user_input > count or user_input < 1:
        print_error(error_message,False,False)
        try:
            user_input = int(input(input_message))
        except:
            continue
    return user_input

def get_user_id_input(inner_validation=True, input_message="Ingresá tu legajo: ", error_message=tcolors.FAIL+tcolors.BOLD+"Legajo inválido, reingrese: "+tcolors.RESET):
    user_id = input(input_message)
    if(not inner_validation):
        if not user_id.isdigit():
            return -1
        return user_id
    
    while not user_id.isdigit():
        print_error(error_message)
        user_id = input(input_message)
    return user_id