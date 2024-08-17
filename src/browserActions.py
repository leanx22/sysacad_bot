from colors import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pageValidators import *

def navigate(driver, url):
    try:
        driver.get(url)
        return True
    except:
        return False

def fill_login_form(driver,user,psw,leg_txtbox_name, pass_txtbox_name):
    time.sleep(1)
    try:        
        user_id_element = driver.find_element(By.NAME, leg_txtbox_name)
        pass_element = driver.find_element(By.NAME, pass_txtbox_name)
        
        user_id_element.clear()
        pass_element.clear()
        
        user_id_element.send_keys(user)
        pass_element.send_keys(psw)
        return True
    except:
        return False
    
def click_login_button(driver,login_btn_name):
    time.sleep(1)
    try:
        driver.find_element(By.NAME, login_btn_name).click()
        return True
    except:
        return False

def click_inscription_link(driver, inscription_link_text):
    try:
        driver.find_element(By.LINK_TEXT, inscription_link_text).click()
        return True
    except:
        return False

def wait_for_url_change(driver, current_url):
    WebDriverWait(driver, 120).until(EC.url_changes(current_url))