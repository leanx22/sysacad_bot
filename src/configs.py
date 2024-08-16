from prints import *
from files import *
from os import system
from driver import print_driver_config

def print_config_menu(configs, clear=True):
    exit = False
    while exit == False:
        if clear:
            sys("cls")

        print_message("CONFIGURACIÓN:\n",True)
        print_message("1. Configurar los datos de ingreso.\n"
            "2. Seleccionar modo de trabajo.\n"
            "3. Seleccionar navegador.\n"
            "4. Reiniciar configuiración.\n"
            "5. Guardar y volver.")
        selection = get_user_input_option(5, "Selección: ", True, tcolors.FAIL+"Reingrese una selección válida: "+tcolors.RESET)
        match selection:
            case 1:
                configs = print_account_settings(configs)
            case 2:
                configs = print_aggro_level(configs)
            case 3:
                configs = print_driver_config(configs)
            case 4:
                configs = restart_all_configs(configs)
            case 5:
                if not save_configs(configs):
                    print_error("[!]No se pudo guardar los cambios en el archivo de guardado.",True,True)
                else:
                    print_message(tcolors.OKGREEN+"Configuraciones guardadas."+tcolors.RESET,False,True)
                exit = True
    return configs

def print_account_settings(configs):
    exit_menu = False
    while exit_menu == False:
        system("cls")
        print_message("DATOS DE INGRESO:\n",True)
        print_message("[OJO] Si bien no es algo dificil, no pienso codear que el bot detecte si el sysacad te rebota las credenciales.\n"
        "Si las escribis mal, nunca va a poder iniciar sesion y lo va a seguir intentado. Asegurate de ponerlas bien.\r\n"
        "************************************************************************************************************\n")
        print_message("1. Configurar legajo. "+(tcolors.FAIL+"[NO CONFIGURADO]"+tcolors.OKCYAN if configs.get("sysacad_user_id") == None else tcolors.OKGREEN+"["+configs.get("sysacad_user_id")+"]"+tcolors.OKCYAN)+"\n"
            "2. Configurar clave de ingreso. "+(tcolors.FAIL+"[NO CONFIGURADO]"+tcolors.OKCYAN if configs.get("psw") == None else tcolors.OKGREEN+"[OK]"+tcolors.OKCYAN)+"\n"
            "3. Volver.")
        selection = get_user_input_option(3, "Selección: ", True, tcolors.FAIL+"Reingrese una selección válida: "+tcolors.RESET)
        match selection:
            case 1:
                system("cls")
                print(">>Ingresa tu legajo: ")
                configs["sysacad_user_id"] = input()
            case 2:
                system("cls")
                print(">>Ingresa tu clave: ")
                configs["psw"] = input()
            case 3:
                exit_menu = True

    return configs

def print_aggro_level(configs):
    exit_menu = False
    while exit_menu == False:
        system("cls")
        print_message("Modo de trabajo:\n",True)
        print_message("MODO ACTUAL -> ["+configs.get("aggro_level")+"]",True)
        print_message("1. Tranqui.\n"
            "2. Normal.\n"
            "3. Agresivo.\n"
            "4. Volver.")
        selection = get_user_input_option(4, "Selección: ", True, tcolors.FAIL+"Reingrese una selección válida: "+tcolors.RESET)
        match selection:
            case 1:
                system("cls")
                configs["aggro_level"] = "1"
            case 2:
                system("cls")
                configs["aggro_level"] = "2"
            case 3:
                system("cls")
                configs["aggro_level"] = "3"
            case 4:
                exit_menu = True

    return configs

def restart_all_configs(configs):
    del configs["sysacad_user_id"]
    configs["aggro_level"] = 2
    configs["navegador"] = "chrome"
    print_message(tcolors.OKGREEN+"Configuración por defecto aplicada."+tcolors.RESET,False,True)
    return configs