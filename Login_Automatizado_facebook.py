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






#driver.find_element_by_css_selector ('<div class="bp9cbjyn j83agx80 taijpn5t dfwzkoeu ni8dbmo4 stjgntxs"><span class="pq6dq46d kb5gq1qc pfnyh3mw oi9244e8"><i class="sp_ihSnwNsMqao sx_b4d710" role="img"></i></span><span class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain" dir="auto"><span class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5">Foto/vídeo</span></span></div>')
#btn_more.click()