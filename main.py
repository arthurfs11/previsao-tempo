from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pyg

# PASSO 0 - CONFIGS

driver = webdriver.Chrome() # SETANDO QUE O NAVEGADOR UTILIZADO SERÁ O CHROME

# PASSO 1 - PERGUNTAR AO USUÁRIO SEU NOME E A CIDADE QUE DESEJA BUSCAR
usuario = pyg.prompt(text='Olá! Qual é o seu nome?', title='Assistente de Previsão do Tempo', default='') # AQUI MONTAMOS UMA MESSAGE BOX QUE ARMAZENA DADOS
cidade = pyg.prompt(text=f'Certo, {usuario}, qual cidade você quer consultar o tempo?', title='Assistente de Previsão do Tempo', default='') # USANDO O MESMO CONCEITO ANTERIOR, ARMAZENAMOS A CIDADE

# PASSO 2 - ABRIR NAVEGADOR 
driver.get('https://www.google.com.br/') # ABRINDO NAVEGADOR NO SITE GOOGLE
time.sleep(3) # AGUARDAR 3 SEGUNDOS

# PASSO 3 - BUSCAR PREVISÃO DO TEMPO PARA A CIDADE INFORMADA
driver.find_element(By.XPATH, "//textarea[contains(@aria-label, 'Pesquisar')]").send_keys(f'previsão do tempo em {cidade}') # PESQUISA A CIDADE NO GOOGLE
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click() # CLICAR NO BOTÃO PESQUISAR
time.sleep(60)

# PASSO 4 - APLICAR REGRA NA TEMPERATURA 

# PASSO 5 - SUGERIR CASACO OU SHORTS CONFORME TEMPERATURA. 