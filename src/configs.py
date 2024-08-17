from IO import *
from files import *
from os import system

def print_config_menu(configs, clear=True):
    exit_menu = False
    
    while exit_menu == False:        
        if clear:
            sys("cls")

        print_message(">>CONFIGURACIÓN<<\n",True)
        print_message("1. Configurar datos de ingreso.\n"
            "2. Seleccionar modo.\n"
            "3. Seleccionar navegador.\n"
            "4. Reiniciar configuiraciones.\n"
            "5. Guardar y volver.")
        selected_option = get_selected_menu_option_from_user(5, ">> ", "Reingrese una selección válida.")
        match selected_option:
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
                    print_error("No se pudo guardar los cambios en el archivo de guardado, pero sí en memoria.",True,True)
                exit_menu = True
    return configs

def print_account_settings(configs):
    exit_menu = False
    while exit_menu == False:
        system("cls")
        print_message(">>DATOS DE INGRESO<<",True)
        print_warn("[OJO] El bot no controlará si sysacad rebota tus credenciales | No se realiza validación alguna de los datos que ingreses.\n",False,False)
        print_message(
            "1. Configurar legajo. "+(tcolors.FAIL+"[NO CONFIGURADO]"+tcolors.OKCYAN if configs.get("sysacad_user_id") == None else tcolors.OKGREEN+"["+configs.get("sysacad_user_id")+"]"+tcolors.OKCYAN)+"\n"
            "2. Configurar clave de ingreso. "+(tcolors.FAIL+"[NO CONFIGURADO]"+tcolors.OKCYAN if configs.get("psw") == None else tcolors.OKGREEN+"[OK]"+tcolors.OKCYAN)+"\n"
            "3. Volver.")
        
        selection = get_selected_menu_option_from_user(3, ">> ","Reingrese una selección válida.")
        match selection:
            case 1:
                system("cls")
                print_message(">>Ingresa tu legajo: ")
                configs["sysacad_user_id"] = input()
            case 2:
                system("cls")
                print_message(">>Ingresa tu clave: ")
                configs["psw"] = input()
            case 3:
                exit_menu = True

    return configs

def print_aggro_level(configs):
    exit_menu = False
    while exit_menu == False:
        system("cls")
        print_message(">>MODO DE TRABAJO<<\n",True)
        print_message("MODO ACTUAL -> ["+str(configs.get("aggro_level"))+"]\n",True)
        print_message("1. Tranqui.\n"
            "2. Normal.\n"
            "3. Agresivo.\n"
            "4. Volver.")
        selection = get_selected_menu_option_from_user(4, ">> ","Reingrese una selección válida.")
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

def print_driver_config(configs):    
    exit_menu = False
    while exit_menu == False:
        system("cls")
        print_message(">>NAVEGADOR<<\n",True)
        
        print_message("ACTUAL -> ["+configs.get("navegador")+"]:\n",True)
        
        print_message("Navegadores disponibles:")
        print_message("1. Chrome\n"
                      "2. Firefox\n"
                      "3. Volver",True)
        selection = get_selected_menu_option_from_user(3, "Selección: ","Reingrese una selección válida.")
        match selection:
            case 1:
                configs["navegador"] = "chrome"
            case 2:
                configs["navegador"] = "firefox"
            case 3:
                exit_menu = True               
    return configs

def restart_all_configs(configs):
    if(configs.get("sysacad_user_id") != None):
        del configs["sysacad_user_id"]
    configs["aggro_level"] = 2
    configs["navegador"] = "chrome"
    print_success("Valores por defecto reestablecidos.",True,True)
    return configs