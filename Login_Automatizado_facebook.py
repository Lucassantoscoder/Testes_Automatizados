from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import pyautogui
import os


#LOGIN FACEBOOK

USERNAME  =  'seu login aqui'
PASSWORD  =  'sua senha aqui'


##Feito com chromedriver para funcionar tem que adicionar instalador na pasta#


driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

driver.get("https://pt-br.facebook.com/login/")


name_textbox = driver.find_element_by_id("email")
name_textbox.send_keys("digite seu email")


password_textbox = driver.find_element_by_id("pass")
password_textbox.send_keys("digite sua senha")


btn_more = driver.find_element_by_id("loginbutton")
btn_more.click()

btn_more = driver.find_elements_by_id("Ações de notificação")
btn_more.click()





######Este codigo abaixo abre arquivo para upload########
#print(pyautogui.position())
#pyautogui.click(280,74), (400,85)
#pyautogui.typewrite("seu arquivo")
#pyautogui.typewrite(['enter'])
