from colors import *
from os import system as sys
from time import sleep

#OUTPUT
def print_welcome_message(time = 2, clear=True):
    print(tcolors.OKCYAN+tcolors.BOLD+"<<|SYSACAD_BOT - POR LEAN - 2024 - v1.2>>"+tcolors.RESET)
    sleep(time)
    if clear:
        sys("cls")

def print_menu(clear=True):
    if clear:
        sys("cls")
    print_message(">>INICIO<<\n",True)
    print_message("1. Cambiar config.\n"
        "2. Iniciar.\n"
        "3. Salir.\n")

def print_error(message, bold=False, wait_for_input=True):
    if(bold):
        print(tcolors.FAIL+tcolors.BOLD+message+tcolors.RESET)
    else:
        print(tcolors.FAIL+message+tcolors.RESET)

    if wait_for_input:
        input(tcolors.FAIL+">> Presioná ENTER para continuar <<"+tcolors.RESET)
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
        input(tcolors.OKCYAN+">> Presioná ENTER para continuar <<"+tcolors.RESET)

def print_success(message, bold=False, wait_for_input=False):
    if(bold):
        print(tcolors.OKGREEN+tcolors.BOLD+message+tcolors.RESET)
    else:
        print(tcolors.OKGREEN+message+tcolors.RESET)
    if wait_for_input:
        input(tcolors.OKGREEN+">> Presioná ENTER para continuar <<"+tcolors.RESET)

def print_warn(message, bold=False, wait_for_input=False):
    if(bold):
        print(tcolors.WARNING+tcolors.BOLD+message+tcolors.RESET)
    else:
        print(tcolors.WARNING+message+tcolors.RESET)
    if wait_for_input:
        input(tcolors.WARNING+">> Presioná ENTER para continuar <<"+tcolors.RESET)


#INPUT
def get_selected_menu_option_from_user(number_of_options=1,input_message=">> ",error_message="Opción no válida."):
    if(number_of_options < 1):
        raise ValueError("Number of options must be greater than 0")
    
    while True:
        user_input = input(input_message)
        try:
            user_input = int(user_input)
            if(user_input > number_of_options or user_input < 1):
                raise ValueError("invalid selected option.")
            break
        except:
            print_error(error_message,False,False)

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