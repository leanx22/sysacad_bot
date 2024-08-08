import sys
from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time
import data
from colors import *

###############ENTRY_POINT####################
def start_camp(user_id, user_password):
    os.system("cls")
    print("Iniciando driver para Firefox...")
    driver = start_driver()

    print("Intentando navegar al login de sysacad...")
    while navigate(driver, data.botData.SYS_LOGIN_LINK) == False:
        tries += 1
        print(tcolors.FAIL+tcolors.BOLD+"("+str(tries)+")"+"No se pudo acceder a la página de login de sysacad."+tcolors.RESET)
        print("Reintentando en 2 segundos...")
        time.sleep(2)

    print("Autocompletando datos de usuario...")
    if fill_login_form(driver, user_id, user_password) == False:
        print(tcolors.FAIL+tcolors.BOLD+"Error fatal al intentar autocompletar los datos del usuario.\nIntentá ver si hay alguna actualizacion del bot.")
        kill(driver,1)

    if click_login_button(driver) == False:
        print(tcolors.FAIL+tcolors.BOLD+"Error fatal al intentar iniciar sesión.\nIntentá ver si hay alguna actualizacion del bot.")
        kill(driver,1)

    print(tcolors.RESET+tcolors.OKCYAN+"Intentando navegar al menu principal...")
    WebDriverWait(driver, 120).until(EC.url_changes(driver.current_url))
    tries = 0
    while check_menu_page(driver) == False:
        tries+=1
        cause = "Sysacad está detonado" if check_sysacad_error(driver) else "Desconocida/timeOut"
        print(tcolors.FAIL+tcolors.BOLD+"[i."+str(tries)+"] No se pudo acceder al menu alumno | CAUSA -> "+cause+" | Reintentando..."+tcolors.RESET)
        time.sleep(1)
        driver.back()
        time.sleep(1)
        fill_login_form(driver, user_id, user_password)
        click_login_button(driver)
        WebDriverWait(driver, 120).until(EC.url_changes(driver.current_url))
    
    print(tcolors.BOLD+tcolors.OKGCYAN+"Intentando ingresar a las inscripciones...")
    click_inscription_link(driver)
    WebDriverWait(driver, 120).until(EC.url_changes(driver.current_url))
    #while check inscrip page == false
    while check_inscription_page(driver) == False:
        break


###############FUNCTIONS####################
def logIn(driver):
    return


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
        print(tcolors.FAIL+tcolors.BOLD+"Error fatal al iniciar el driver.")
        input()
        sys.exit(1)

def fill_login_form(driver, user_id, user_password):
    try:
        time.sleep(1)
        user_id_element = driver.find_element(By.NAME, data.botData.LEG_TEXTBOX_NAME)
        pass_element = driver.find_element(By.NAME, data.botData.PASS_TEXTBOX_NAME)
        
        user_id_element.clear()
        pass_element.clear()
        
        user_id_element.send_keys(user_id)
        pass_element.send_keys(user_password)
        return True
    except:
        return False
    
def click_login_button(driver):
    try:
        driver.find_element(By.NAME, data.botData.LOGIN_BUTTON_NAME).click()
        return True
    except:
        return False

def click_inscription_link(driver):
    try:
        driver.find_element(By.LINK_TEXT, data.botData.INSCRIPTION_LINK_TEXT).click()
        return True
    except:
        return False

###############PAGE_CHECKS####################
def check_menu_page(driver):
    try:
        driver.find_element(By.LINK_TEXT, data.botData.INSCRIPTION_LINK_TEXT)
        return True
    except:
        return False

def check_inscription_page(driver):
    #editar
    try:
        driver.find_element(By.LINK_TEXT, data.botData.INSCRIPTION_LINK_TEXT).click()
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
def kill(driver, code=0):
    input("Presioná ENTER para continuar...")
    driver.quit()
    sys.exit(code)