from IO import *

from selenium import webdriver

from selenium.webdriver.firefox.service import Service as fserv
from selenium.webdriver.chrome.service import Service as chserv

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(driver_name):
    driver = None
    driver_name = str(driver_name).lower()
    print_message("Cargando driver y abriendo navegador ["+driver_name+"]\n")
    match driver_name:
        case "chrome":
            driver = webdriver.Chrome(service=chserv(ChromeDriverManager().install()))
        case "firefox":
            driver = webdriver.Firefox(service=fserv(GeckoDriverManager().install()))
        case other:
            raise ValueError("Unknown driver "+driver_name)
    return driver