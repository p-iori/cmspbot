'''
================
CRIADO POR IORI
================
'''


from selenium import webdriver  # Importa o webdriver
from selenium.webdriver.chrome.service import Service
# Procurar elementos pelo class, id, etc...
from selenium.webdriver.common.by import By
# Teclas (ENTER, END, BACKSPACE, etc...)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  # Esperar elemento carregar
# Esperar elemento carregar
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

botao_acesso_id = 'access-student'
campo_ra_id = 'ra-student'
campo_digito_id = 'digit-student'
campo_senha_id = 'password-student'
botao_entrar_id = 'btn-login-student'

botao_tarefa_class = 'material-icons.room-list-menu-tasks.tdg'

# Abre o cmsp
driver.get('https://cmspweb.ip.tv/')

'''
=========== LOGIN ===========
'''

# Localiza o botao de login e clica
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, botao_acesso_id))
)

botao_acesso = driver.find_element(By.ID, botao_acesso_id)
botao_acesso.click()

# Localiza o RA e escreve
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, campo_ra_id))
)

campo_ra = driver.find_element(By.ID, campo_ra_id)
campo_ra.send_keys(ESCREVA O RA ENTRE ASPAS AQUI)

# Localiza o dígito e escreve
campo_digito = driver.find_element(By.ID, campo_digito_id)
campo_digito.send_keys(ESCREVA O DIGITO ENTRE ASPAS AQUI)

# Localiza a senha e escreve
campo_senha = driver.find_element(By.ID, campo_senha_id)
campo_senha.send_keys(ESCREVA A SENHA ENTRE ASPAS AQUI)

# Localiza o entrar e clica
botao_entrar = driver.find_element(By.ID, botao_entrar_id)
botao_entrar.click()

'''
=========== ENTRAR NA TAREFA ===========
'''

# Localiza a sala e clica no icone de tarefas
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, botao_tarefa_class))
)

botao_sala = driver.find_elements(By.CLASS_NAME, botao_tarefa_class)
botao_sala[2].click()


time.sleep(10)
