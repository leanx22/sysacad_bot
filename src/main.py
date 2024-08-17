from os import system

from playsound import playsound

from files import *
from colors import *
from IO import *
from configs import print_config_menu
from driver import get_driver
from functions import start_task

exit_menu = False
configs = get_configs("./src/config.txt");
print_welcome_message(2)

while exit_menu == False:
    print_menu()
    selected_option = get_selected_menu_option_from_user(3)

    match selected_option:
        case 1:
            configs = print_config_menu(configs,True)
        case 2:
            if(configs.get("psw") == None or configs.get("sysacad_user_id") == None):
                print_error("Debe configurarse los datos de ingreso antes de iniciar la tarea.")
                continue

            system("cls")
            try:
                driver = get_driver(configs.get("navegador"))
            except:
                print_error("Error al iniciar driver y/o navegador ["+configs.get("navegador")+"]. Verifique que el driver correcto esté seleccionado y el navegador esté instalado.",True,True)
                continue

            try:
                if start_task(driver, configs):
                    #success sound
                    print_success("[LISTO]",True, False)
                    playsound("./src/assets/success_song.mp3")
                    print_warn("AL PRESIONAR CONTINUAR EL NAVEGADOR VA A CERRARSE, ASEGURATE DE TERMINAR TU INSCRIPCION ANTES DE CONTINUAR",True,True)
            except ValueError as VE:
                playsound("./src/assets/error_sound.mp3")
                print_error("Ocurrió un error inesperado durante la ejecución: ("+str(VE)+".) | Abortando ejecución.",True,True)
            except TimeoutError as TE:
                playsound("./src/assets/error_sound.mp3")
                print_error("Se pasó el límite de tiempo: ("+str(TE)+".) | Abortando ejecución.",True,True)
            except Exception as E:
                playsound("./src/assets/error_sound.mp3")
                print_error("Ocurrió un error: ("+str(E)+".) | Abortando ejecución.",True,True)
            finally:
                driver.quit()
        case 3:
            system("cls")
            print(tcolors.OKCYAN+"Cerrando...")
            exit_menu = True
        case other:
            #it should never reach here btw
            #but just in case, if that happens, it will print the menu again so np.
            break
exit(0)