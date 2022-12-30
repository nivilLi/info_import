from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from openpyxl import *
from p1.utils import *
from p1.main import *
import time

# groups = ['新光组', '老光组', '华六组', '大屋组', '志合组', '曹云组', '仓场组', '五桂组', '羊角组', '羊冲组', '祝库组', '羊久组'
#           ,'茂雅组', '胡塘组', '汪家组', '荷叶组', '周关组', '大皂组', '祖堂组', '石莫组', '龙志组']
groups = ['将军组', '井冲组', '大元组', '毛公组', '上湖组', '下湖组', '宋老屋组', '从山组', '均陂组', '何家组', '伍祠组', '贺大屋组'
          ,'曾冲组', '埠头组', '厚冲组']
username = driver.find_element("id", 'username')
password = driver.find_element("id", 'password')
# jcaptcha_response = driver.find_element("id", 'jcaptcha_response')
username.send_keys("43042110501")
password.send_keys('YB10501')

i = 0
rows = getrows()
while True:
    i = i + 1
    flag = False
    row = rows.__next__()
    if i >= 473:
        break
def iter_fill():
    j = 0
    global i
    global row
    while True:
        i = i + 1
        print(i)
        row = rows.__next__()
        j = 0
        # driver.execute_script('alert("是否继续")')
        for cell in row:
            j += 1
            if j == 1:
                time.sleep(3)
                idcart = ws.cell(i, 10).value
                input_text(idcart.upper(), "aab004")
                query = driver.find_element("id", 'on_query')
                query.click()
                time.sleep(3)
                flag = find_poor()
            # if isElementExist('/html/body/div[21]/div/div[10]/button[1]'):
            #     click('/html/body/div[21]/div/div[10]/button[1]')
            #     time.sleep(1)
            #     on_save()
            #     time.sleep(1)
            #     click('/html/body/div[21]/div/div[10]/button[1]')
            #     time.sleep(1)
            if flag == False:
                if j == 4:
                    try:
                        selector(2, "AAR006")
                    except Exception:
                        click('/html/body/div[21]/div/div[10]/button[1]')
                        time.sleep(1)
                        on_save()
                        time.sleep(3)
                        click('/html/body/div[21]/div/div[10]/button[1]')
                        time.sleep(1)
                        print(i)
                        iter_fill()
                if j == 5:
                    selector(groups.index(cell.value) + 1, 'AAR007')
                if j == 8:
                    input_text(cell.value, "aab002")
                if j == 11:
                    selector(1, 'aab007')
                if j == 12:
                    selector(4 if cell.value == '群众' else 1, 'aak033')
                if j == 13:
                    input_text(cell.value, 'aac017')
                if j == 14:
                    input_text(cell.value, 'aar012')
                    pyautogui.scroll(-300)
            elif find_poor():
                click('/html/body/div[21]/div/div[10]/button[1]')
                pyautogui.scroll(-300)
            if j == 18:
                selector(2 if cell.value == '是' else 1, 'aac340')
            if j == 19:
                selector(2 if cell.value == '是' else 1, 'aac341')
            if j == 20:
                selector(2 if cell.value == '是' else 1, 'aac342')
            if j == 21:
                selector(2 if cell.value == '是' else 1, 'aac091')
            if j == 22:
                selector(2 if cell.value == '是' else 1, 'aac343')
            if j == 25:
                selector(2 if cell.value == '是' else 1, 'aac318')
                pyautogui.scroll(-300)
            if j == 26:
                selector(2 if cell.value == '是' else 1, 'aac346')
            if j == 27:
                selector(2 if cell.value == '是' else 1, 'aac347')
            if j == 28:
                selector(2 if cell.value == '是' else 1, 'aac319')
            if j == 29:
                selector(1 if cell.value == '水冲卫生厕所' else 2, 'aac348')
            if j == 30:
                selector(2 if cell.value == '是' else 1, 'aac349')
            if j == 31:
                selector(2 if cell.value == '是' else 1, 'aac350')
            if j == 32:
                selector(2 if cell.value == '是' else 1, 'aac351')
            if j == 33:
                selector(2 if cell.value == '是' else 1, 'aac352')
                time.sleep(0.5)
                on_save()
                click('/html/body/div[21]/div/div[10]/button[1]')

try:
    iter_fill()
except Exception:
    click('/html/body/div[21]/div/div[10]/button[1]')
    time.sleep(1)
    on_save()
    time.sleep(3)
    click('/html/body/div[21]/div/div[10]/button[1]')
    time.sleep(1)
    print(i)
    iter_fill()





