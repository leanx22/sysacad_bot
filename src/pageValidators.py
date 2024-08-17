from selenium.webdriver.common.by import By

def is_student_menu(driver, inscription_link_text):
    try:
        driver.find_element(By.LINK_TEXT, inscription_link_text)
        return True
    except:
        return False
    
def is_inscription_page(driver, inscription_print_button):
    try:
        driver.find_element(By.LINK_TEXT, inscription_print_button)
        return True
    except:
        return False
    
def are_inscriptions_closed(driver, sys_err_class, sys_clsd_insc_text):
    err_text = driver.find_element(By.CLASS_NAME, sys_err_class).text
    if(err_text == sys_clsd_insc_text):
        return True
    return False

def is_login_page(driver, psw_textbox_name):
    try:        
        pass_element = driver.find_element(By.NAME, psw_textbox_name)
        return True
    except:
        return False
    
def is_sysacad_error_page(driver,sys_err_class):
    try:
        driver.find_element(By.CLASS_NAME, sys_err_class)
        return True
    except:
        return False