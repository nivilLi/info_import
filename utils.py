from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from p1 import main


driver = webdriver.Chrome()
driver.get('http://cpadisc4.cpad.gov.cn/cpad/main')


def input_text(text, e_id):
    idcard = WebDriverWait(driver, 6000, 1).until(
        EC.presence_of_element_located((By.ID, e_id))
    )
    # idcard = driver.find_element("id", 'aab004')\
    idcard.clear()
    idcard.send_keys(text)

def selector(feeds, e_id):
    __selector__ = WebDriverWait(driver, 6000, 1).until(
        EC.presence_of_element_located((By.ID, e_id))
    )
    __selector__.click()
    for i in range(0, feeds):
        pyautogui.press('down')

    pyautogui.press("enter")

def on_save():
    WebDriverWait(driver, 6000, 1).until(
        EC.presence_of_element_located((By.ID, 'on_save'))
    ).click()

def click(xpath):
    WebDriverWait(driver, 6000, 1).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    ).click()


def isElementExist(xpath):
    flag = True
    try:
        driver.find_element_by_css_selector(By.XPATH, xpath)
        return flag

    except:
        flag = False
        return flag

def find_poor():
    try:
        return driver.find_element(By.XPATH, '//*[@id="swal2-content"]').text.find("脱贫户已存在") != -1
    except Exception:
        return False

def input_text_byXpath(text, xpath):
    idcard = WebDriverWait(driver, 6000, 1).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    # idcard = driver.find_element("id", 'aab004')\
    idcard.clear()
    idcard.send_keys(text)