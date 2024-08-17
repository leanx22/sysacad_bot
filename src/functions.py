import os
import time
import data

from colors import *
from pageValidators import *
from browserActions import *
from IO import *

def start_task(driver, configs):
    userid = configs.get("sysacad_user_id")
    password = configs.get("psw")
    
    os.system("cls")
    print_message("- Navegando a la página de login.")
    
    login_nav_tries = 0
    while navigate(driver, data.botData.SYS_LOGIN_LINK) == False:
        login_nav_tries += 1
        print_error("["+str(login_nav_tries)+"]"+" >>No se pudo acceder | Reintentando<<",False,False)

    login_url = driver.current_url
    print_message("- Intentando acceder.")
    logIn(driver,configs)    
    wait_for_url_change(driver, login_url)
    
    menu_nav_tries = 0
    while is_student_menu(driver, data.botData.INSCRIPTION_LINK_TEXT) == False:
        menu_nav_tries+=1
        print_error("["+str(menu_nav_tries)+"]"+" >>No se pudo acceder al menu alumno | Reintentando<<",False,False)
        driver.back()
        time.sleep(1)
        logIn(driver,configs)
        wait_for_url_change(driver, login_url)
        if is_student_menu(driver, data.botData.INSCRIPTION_LINK_TEXT) == True:
            break
    
    print_message("- Intentando acceder a las inscripciones.")
    student_menu_url = driver.current_url
    click_inscription_link(driver, data.botData.INSCRIPTION_LINK_TEXT)
    wait_for_url_change(driver, student_menu_url)

    #validate session expiration

    inscription_nav_tries = 0
    while is_inscription_page(driver, data.botData.INSCRIPTION_PRINT_BUTTON) == False:
        if are_inscriptions_closed(driver, data.botData.SYS_ERR_CLASS, data.botData.SYS_CLSD_INSC_TEXT) == True:
            raise Exception("Las inscripciones aún no están disponibles")
        if is_login_page(driver, data.botData.PSW_TEXTBOX_NAME) == True:
            raise Exception("La sesión de sysacad expiró, reiniciá el procedimiento")
        inscription_nav_tries+=1
        print_error("["+str(inscription_nav_tries)+"]"+" >>No se pudo acceder a la página de inscripciones | Reintentando<<",False,False)
        driver.back()
        time.sleep(1)
        click_inscription_link(driver, data.botData.INSCRIPTION_LINK_TEXT)
        wait_for_url_change(driver, student_menu_url)
        if is_inscription_page(driver, data.botData.INSCRIPTION_PRINT_BUTTON) == True:
            break

    return True

def logIn(driver, configs):
    if fill_login_form(driver,configs.get("sysacad_user_id"),configs.get("psw"),data.botData.LEG_TEXTBOX_NAME, data.botData.PASS_TEXTBOX_NAME) == False or click_login_button(driver, data.botData.LOGIN_BUTTON_NAME) == False:
        raise ValueError("El elemento necesario no se encuentra o es nulo")
