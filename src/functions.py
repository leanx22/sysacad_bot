import sys
from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from playsound import playsound

import os
import time
import data
from colors import *

userid = ""
password = ""

###############ENTRY_POINT####################
def start_camp(user_id, user_password):
    global userid 
    userid = user_id
    global password 
    password = user_password
    os.system("cls")
    print("Iniciando driver para Firefox...")
    driver = start_driver()

    print("Intentando navegar al login de sysacad...")
    while navigate(driver, data.botData.SYS_LOGIN_LINK) == False:
        tries += 1
        print(tcolors.FAIL+tcolors.BOLD+"("+str(tries)+")"+"No se pudo acceder a la página de login de sysacad."+tcolors.RESET)
        print("Reintentando en 2 segundos...")
        time.sleep(2)

    logIn(driver)

    
    
    print(tcolors.BOLD+tcolors.OKCYAN+"Intentando ingresar a las inscripciones...")
    click_inscription_link(driver)
    WebDriverWait(driver, 120).until(EC.url_changes(driver.current_url))
    #while check inscrip page == false
    while check_inscription_page(driver) == False:
        break


###############FUNCTIONS####################
def logIn(driver):
    if fill_login_form(driver) == False:
        print(tcolors.FAIL+tcolors.BOLD+"No se puede encontrar los elementos del formulario para colocar la información. Abortando el proceso.")
        kill(driver,"No se encuentran los elementos necesarios en el DOM.")

    if click_login_button(driver) == False:
        print(tcolors.FAIL+tcolors.BOLD+"No se puede encontrar el botón de inicio de sesión. Abortando el proceso.")
        kill(driver, "No se encuentra el botón en el DOM. No se puede continuar.")
    
    wait_for_user_menu(driver)

def wait_for_user_menu(driver):
    while check_menu_page(driver) == False:
        cause = "Sysacad está detonado" if check_sysacad_error(driver) else "Desconocida/timeOut"
        print(tcolors.FAIL+tcolors.BOLD+"[ERR] No se pudo acceder al menu alumno | CAUSA -> "+cause+" | Reintentando..."+tcolors.RESET)
        time.sleep(1)
        driver.back()
        time.sleep(1)
        logIn(driver)
    click_inscription_link(driver)
    wait_for_inscription_page(driver)

def wait_for_inscription_page(driver):
    while check_inscription_page(driver) == False:
        cause = "Sysacad está detonado" if check_sysacad_error(driver) else "Desconocida/timeOut"
        print(tcolors.FAIL+tcolors.BOLD+"[ERR] No se pudo acceder a las inscripciones | CAUSA -> "+cause+" | Reintentando..."+tcolors.RESET)
        time.sleep(1)
        driver.back()
        time.sleep(1)
        click_inscription_link(driver)
    print(tcolors.BOLD+tcolors.OKGREEN+"YA ESTAS EN LA PAGINA DE INSCRIPCIONES...")
    playsound("./src/assets/completed.mp3")
    input("Presione ENTER para cerrar todo (navegador incluido OJO!)...")
    kill(driver, 0)

###############AUTOMATED_USER_ACTIONS####################
def navigate(driver, url):
    try:
        driver.get(url)
        return True
    except:
        return False

def start_driver():    
    try:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        return driver
    except:
        print(tcolors.FAIL+tcolors.BOLD+"No se pudo iniciar el driver. No se puede continuar.")
        input()
        sys.exit(1)

def fill_login_form(driver):
    print(tcolors.OKCYAN+"Autocompletando formulario...")
    time.sleep(1)
    try:        
        user_id_element = driver.find_element(By.NAME, data.botData.LEG_TEXTBOX_NAME)
        pass_element = driver.find_element(By.NAME, data.botData.PASS_TEXTBOX_NAME)
        
        user_id_element.clear()
        pass_element.clear()
        
        user_id_element.send_keys(userid)
        pass_element.send_keys(password)
        return True
    except:
        return False
    
def click_login_button(driver):
    print(tcolors.OKCYAN+"Intentando iniciar sesión...")
    try:
        driver.find_element(By.NAME, data.botData.LOGIN_BUTTON_NAME).click()
        WebDriverWait(driver, 120).until(EC.url_changes(driver.current_url))
        return True
    except:
        return False

def click_inscription_link(driver):
    print(tcolors.OKCYAN+"Intentando ingresar a las inscripciones...")
    try:
        current_url = driver.current_url
        driver.find_element(By.LINK_TEXT, data.botData.INSCRIPTION_LINK_TEXT).click()
        WebDriverWait(driver, 120).until(EC.url_changes(current_url))
        if check_inscription_page(driver) == False:
            if check_login_page(driver):
                logIn(driver)
            time.sleep(2)
            driver.back()
            time.sleep(1)
            click_inscription_link(driver)
    except:
        print(tcolors.FAIL+tcolors.BOLD+"No se encuentra el boton de inscripciones. No se puede continuar.")
        kill(driver, "No se encuentra el elemento en el DOM.")

###############PAGE_CHECKS####################
def check_login_page(driver):
    try:        
        user_id_element = driver.find_element(By.NAME, data.botData.LEG_TEXTBOX_NAME)
        pass_element = driver.find_element(By.NAME, data.botData.PASS_TEXTBOX_NAME)
        return True
    except:
        return False

def check_menu_page(driver):
    try:
        driver.find_element(By.LINK_TEXT, data.botData.INSCRIPTION_LINK_TEXT)
        return True
    except:
        return False

def check_inscription_page(driver):
    try:
        driver.find_element(By.LINK_TEXT, data.botData.INSCRIPTION_PRINT_BUTTON)
        return True
    except:
        return False

def check_sysacad_error(driver):
    try:
        driver.find_element(By.CLASS_NAME, data.botData.SYS_ERR_CLASS)
        return True
    except:
        return False

###########OTHERS####################
def kill(driver, code):
    input("Presioná ENTER para finalizar...")
    sys.exit(code)