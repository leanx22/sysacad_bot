from os import system
from files import *
from colors import *
from prints import *
from configs import print_config_menu
from driver import get_driver
from functions import start_camp

exit_menu = False
print("Cargando configuraciones del usuario...")
configs = get_configs("./src/config.txt");
system("cls")
print_welcome_message(2)

while exit_menu == False:
    system("cls")
    print_menu()

    selected_option = get_user_input_option(3)
    while selected_option == -1:
        system("cls")
        print_menu()
        selected_option = get_user_input_option(3,get_formated_error_string("Reingrese selección válida: "))
    
    match selected_option:
        case 1:
            configs = print_config_menu(configs,True)
        case 2:
            if(configs.get("psw") == None or configs.get("sysacad_user_id") == None):
                print_error("Debe configurarse los datos de ingreso antes de iniciar la tarea.")
            else:
                system("cls")
                driver = get_driver(configs.get("navegador"))
                start_camp(driver, configs)
        case 3:
            system("cls")
            print(tcolors.OKCYAN+"Chau Chau.")
            exit_menu = True
        case other:
            #it should never reach here btw
            #but just in case, if that happens, it will print the menu again so np.
            break
exit(0)