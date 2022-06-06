######### BIBLIOTECAS

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

#################
BASE_PIPEFY = "BASE_PIPEFY.xlsx"
df = pd.read_excel(BASE_PIPEFY)

for index,row in df.iterrows():
    chrome = webdriver.Chrome(executable_path= 'chromedriver.exe')
    chrome.get("https://app.pipefy.com/public/form/9s5JH4_J")
    time.sleep(2)
    ###################################     COLABORADOR NOME       ########################################
    COLABORADOR = chrome.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[1]/div[2]/div/form/div[1]/div/div[1]/span[1]/div/a/span')
    COLABORADOR.click()
    COLABORADORNOME= chrome.find_element(By.XPATH,'/html/body/div[3]/div/div/header/label/input')
    COLABORADORNOME.click()
    COLABORADORNOME.send_keys('Luiz Henrique Reis')
    time.sleep(2)
    CONFIRMACOLABORADOR= chrome.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div')
    CONFIRMACOLABORADOR.click()
    
    ############################################### FORNECEDOR ##################################################33
    CLICARDATABASEFORNECEDOR = chrome.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[1]/div[2]/div/form/div[1]/div/div[1]/span[2]/div/a')
    CLICARDATABASEFORNECEDOR.click()
    ESCREVERFORNECEDOR = chrome.find_element(By.XPATH,'/html/body/div[3]/div/div/header/label/input')
    ESCREVERFORNECEDOR.send_keys(row["FORNECEDOR"])
    time.sleep(2)
    CLICARFORNECEDOR = chrome.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div/a' )
    CLICARFORNECEDOR.click()

    ########################################     DATAS              ###################################
    
    DATADEEMISSAO= chrome.find_element(By.XPATH,'//*[@id="fake-pipe-field-publicForm-customFields_data_de_emiss_o-input"]')
    DATADEPAGAMENTO=chrome.find_element(By.XPATH,'//*[@id="fake-pipe-field-publicForm-customFields_copy_of_data_de_emiss_o-input"]')
    DATADEEMISSAO.send_keys(row["DATA DE EMISSAO"])
    DATADEPAGAMENTO.send_keys(row["PREVISÃO DE PAGAMENTO"])
    

    #########################################      QUANTIDADE CENTRO DE CUSTO #######################################################
    QUANTIDADECENTRODECUSTO = chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[2]/div/form/div[1]/div/div[1]/div[2]/div[' + str(row["QUANTIDADE CENTRO DE CUSTO"]) + ']/label')
    QUANTIDADECENTRODECUSTO.click()
    time.sleep(2)
    
    ############################################### VALOR ##################################################
    VALORTOTAL = chrome.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[1]/div[2]/div/form/div[1]/div/div[1]/label[1]/input')
    VALORTOTAL.send_keys(str(row["VALOR TOTAL"]))



    ################################################# FORMA DE PAGAMENTO ############################

    FORMADEPAGAMENTO = chrome.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[1]/div[2]/div/form/div[1]/div/div[1]/div[6]/div['+ str(row["FORMA DE PAGAMENTO"])+']/label')
    FORMADEPAGAMENTO.click()
    

    #################  NÚMERO OE #############################
    CLICARNUMEROOE = chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[2]/div/form/div[1]/div/div[1]/span[3]/div/a')
    CLICARNUMEROOE.click()
    COLOCARNUMEROOE = chrome.find_element(By.XPATH,'/html/body/div[3]/div/div/header/label/input')
    COLOCARNUMEROOE.click()
    COLOCARNUMEROOE.send_keys(str(row["Oes"]))
    time.sleep(2)
    NUMEROOE = chrome.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/a')
    NUMEROOE.click()


    ############################################## ANEXAR DOCUMENTO ######################################
    CLICARANEXO = chrome.find_element(By.XPATH,'//*[@id="dropzone-fake-pipe-field-publicForm-customFields_anexo_1-input"]/div[2]/div/a')
    CLICARANEXO.click()
    time.sleep(16)
    chrome.quit
    

    

