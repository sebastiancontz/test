from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time

ruta_pj = os.getcwd()
url2 = "https://www.registrocivil.cl/OficinaInternet/web/carro.srcei"
rut = '18060793-5'
correo = "sebastiancz@live.cl"
opts = Options()
opts.add_argument("--headless")

driver = webdriver.Chrome(options=opts,executable_path=ruta_pj+"/chromedriver")
driver.get(url2)
time.sleep(2)
driver.execute_script("document.getElementById('divLista_1').style.display = 'block';")
div_nac = driver.find_element_by_id("container_95")
get_cert = div_nac.find_element_by_class_name("iCheck-helper")
driver.execute_script("arguments[0].click();", get_cert)
time.sleep(2)
driver.find_element_by_class_name("inputRunCertificado").send_keys(rut)
time.sleep(2)
click_boton = div_nac.find_element_by_class_name("btn_agregarCarro")
driver.execute_script("arguments[0].click();", click_boton)
time.sleep(2)
driver.find_element_by_id("carro_solicitanteInputEmail").send_keys(correo)
time.sleep(2)
driver.find_element_by_id("carro_solicitanteInputEmailConfirm").send_keys(correo)
click_boton2 = driver.find_element_by_id("carro_btnContinuar")
driver.execute_script("arguments[0].click();", click_boton2)

print("proceso finalizado!")