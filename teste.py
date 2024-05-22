from selenium import webdriver # Importa o webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # Procurar elementos pelo class, id, etc...
from selenium.webdriver.common.keys import Keys # Teclas (ENTER, END, BACKSPACE, etc...)
from selenium.webdriver.support.ui import WebDriverWait # Esperar elemento carregar
from selenium.webdriver.support import expected_conditions as EC # Esperar elemento carregar
import time 

# Configuração do webdriver
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Site desejado
driver.get('https://www.google.com/')

# Espera até a barra carregar, se n carregar dps de 5 seg ele fecha o programa
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
)

# Encontra a barra de pesquisa pela classe dela e pesquisa uwu
input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
input_element.send_keys('uwu' + Keys.ENTER)

time.sleep(10)

driver.quit()