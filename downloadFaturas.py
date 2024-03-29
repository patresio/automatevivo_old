import os
import shutil
import time

import undetected_chromedriver as uc
from decouple import config
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager

from alterDados import ano_atual, mes_data, mes_texto, mes_txt


class AutomateVivo:

    ''' Definições de variaveis para execução do sistema '''

    def __init__(self):
        self.PASTA_LOCAL = os.getcwd()
        self.PASTA_DOWNLOAD = os.path.join(self.PASTA_LOCAL, 'Download')
        self.SITE_LINK = "https://mve.vivo.com.br/login/cpf"
        self.DADOS_USUARIO = {
            "cpf": config('CPF'),
            "email": config('EMAIL'),
            "senha": config('PASSWORD'),
        }
        self.SITE_MAP = {
            "inboxes": {
                "cpfInbox": {
                    "xpath": "/html/body/div[1]/div/div/div/div[2]/div/form/div/input"
                },

                "emailInbox": {
                    "xpath": "/html/body/main/div/div/div/div[2]/form/div[2]/span/div/div/input"
                },

                "senhaInbox": {
                    "xpath": "/html/body/main/div[2]/form/div[2]/div/div/input"
                }
            },

            "buttons": {
                "cpfButton": {
                    "xpath": "/html/body/div[1]/div/div/div/div[2]/div/form/button"
                },

                "emailButton": {
                    "xpath": "/html/body/main/div/div/div/div[2]/form/div[4]/button"
                },

                "senhaButton": {
                    "xpath": "/html/body/main/div[2]/form/div[4]/button"
                }
            },

            "forms": {
                "listaTelefone": {
                    "xpath": "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[3]/div/div/form/ul/li"
                },
                "combo-box": {
                    "class_name": "combo_family"
                }
            },

            "hyperlink": {
                "linkFixaCorporativa": {
                    "xpath": "/html/body/div[1]/header/div/div/div[1]/div[1]/div/div[2]/ul/li[2]"
                },

                "downloadPDF": {
                    "id": "downloadFatura0"
                }

            },

            "lista": {
                "ulliTelefones": {
                    "xpath": "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[3]/div/div/form/ul/li[$$NUMEROUP$$]/a/span[1]"
                    #         /html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[3]/div/div/form/ul/li[$$NUMEROUP$$]/a/span[1]
                }
            },

            "img": {
                "download": {
                    "xpath": "/html/body/div[2]/div/div/div/div/div/div/div[3]/div/div[1]/div[3]/div/div/div[1]/form/table/tbody/tr[1]/td[5]/div[3]/img"
                }
            },

            "tabela": {
                "tdmesVigencia": {
                    "xpath": "/html/body/div[2]/div/div/div/div/div/div/div[3]/div/div[1]/div[3]/div/div/div[1]/form/table/tbody/tr[1]/td[1]"
                },

                "tdstatusPagamento": {
                    "xpath": "/html/body/div[2]/div/div/div/div/div/div/div[3]/div/div[1]/div[3]/div/div/div[1]/form/table/tbody/tr[1]/td[3]"
                }
            }

        }

        self.chrome_options = uc.ChromeOptions()
        self.chrome_options.add_argument("--disable-infobars")
        self.chrome_options.headless = False
        self.chrome_options.add_argument("--disable-logging")
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_argument("--disable-notifications")
        self.chrome_options.add_argument("--disable-default-apps")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--window-size=1920,1080")
        prefs = {"download.default_directory": self.PASTA_DOWNLOAD,
                 "safebrowsing.enabled": "false"}
        self.chrome_options.add_experimental_option("prefs", prefs)
        self.driver = uc.Chrome(headless=False,
                                options=self.chrome_options, service=ChromeService(ChromeDriverManager().install()), use_subprocess=True)

        self.driver.implicitly_wait(20)

    ''' Funções para Criação das Pastas locais '''

    def criaPastaFaturas(self):
        self.namePathFatura = f'Faturas-{mes_txt}'
        if os.path.isdir(self.namePathFatura):
            print(f'Pasta do mês: {mes_data} já existe')
        else:
            os.mkdir(self.namePathFatura)
            print(f'A pasta do mês: {mes_data} foi criada')

    def criarPastaDownload(self):
        if os.path.isdir(self.PASTA_DOWNLOAD):
            print('A Pasta Download existe!')
        else:
            os.mkdir(self.PASTA_DOWNLOAD)

    '''
        Termino da criação das pastas

        Inicio da Automação abrindo o navegador e o site
    '''

    def abrirSite(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(5)
        self.criaPastaFaturas()
        self.criarPastaDownload()
        time.sleep(2)

    def logarSite(self):
        self.abrirSite()
        # Parte do CPF
        # """ self.driver.find_element(
        #     By.XPATH, self.SITE_MAP['inboxes']['cpfInbox']['xpath']).send_keys(
        #         self.DADOS_USUARIO['cpf'], Keys.ENTER)
        # time.sleep(15) """

        # Parte do EMAIL
        self.driver.find_element(
            By.XPATH, self.SITE_MAP['inboxes']['emailInbox']['xpath']).send_keys(
                self.DADOS_USUARIO['email'], Keys.ENTER)
        time.sleep(15)

        # Parte do Senha
        self.driver.find_element(
            By.XPATH, self.SITE_MAP['inboxes']['senhaInbox']['xpath']).send_keys(
                self.DADOS_USUARIO['senha'], Keys.ENTER)
        time.sleep(15)

    def clicaLinkFaturas(self):
        self.driver.find_element(
            By.XPATH, self.SITE_MAP['hyperlink']['linkFixaCorporativa']['xpath']).click()
        time.sleep(30)

    def trocaPagina(self):
        self.aba_pai = self.driver.current_window_handle
        self.nova_aba = self.driver.window_handles[1]
        self.driver.switch_to.window(self.nova_aba)

    def listaTelefones(self):
        # Gambiarra
        self.driver.find_element(
            By.CLASS_NAME, self.SITE_MAP['forms']['combo-box']['class_name']).click()

        # Agora lista os telefones
        numeroTelefones = self.driver.find_element(
            By.XPATH, '//*[@id="formSelectedItem"]/ul')
        self.telefoneListados = numeroTelefones.find_elements(
            By.XPATH, self.SITE_MAP['forms']['listaTelefone']['xpath'])

    def downloadFaturas(self):
        self.trocaPagina()
        time.sleep(2)
        self.listaTelefones()
        total = len(self.telefoneListados)
        pbar = tqdm(total=total,
                    position=0, leave=True)

        for i, numTelefone in enumerate(self.telefoneListados):
            pbar.update()
            print(i)
            # Gambiarra no código
            if i != 0:
                self.driver.find_element(By.CLASS_NAME, 'combo_family').click()
                print('Primeiro click!')
            # Gambiarra 2 para quando o codigo der errado !!!! entou problemas
            if i < 0:
                if i == 0:
                    telefoneLista = self.SITE_MAP["lista"]["ulliTelefones"]["xpath"].replace(
                        "$$NUMEROUP$$", str(numeroUP))
                    print(telefoneLista)
                    telefonetexto = self.driver.find_element(
                        By.XPATH, telefoneLista).text()
                    print(telefonetexto)
                    self.driver.find_element(By.XPATH, telefoneLista).click()
                else:
                    print('Vou só pular!')

            else:
                print('tentando entrar no loop!')
                numeroUP = i + 1
                telefoneLista = self.SITE_MAP["lista"]["ulliTelefones"]["xpath"].replace(
                    "$$NUMEROUP$$", str(numeroUP))
                print(telefoneLista)
                self.driver.find_element(By.XPATH, telefoneLista).click()

                telefoneAtual = self.driver.find_element(
                    By.XPATH, telefoneLista).get_attribute("data-value")

                try:
                    mesVigencia = self.driver.find_element(By.XPATH,
                                                           self.SITE_MAP['tabela']['tdmesVigencia']['xpath'])
                    statusPagamento = self.driver.find_element(By.XPATH,
                                                               self.SITE_MAP['tabela']['tdstatusPagamento']['xpath'])
                    textoPronto = f'O sistema abriu com êxito a linha: {telefoneAtual}. Sendo a fatura em vigor {mesVigencia.text}. Com status {statusPagamento.text}'
                    print(textoPronto)

                    if statusPagamento.text == "Pendente":
                        self.driver.find_element(
                            By.XPATH, self.SITE_MAP['img']['download']['xpath']
                        ).click()
                        time.sleep(3)
                        self.driver.find_element(
                            By.ID, self.SITE_MAP['hyperlink']['downloadPDF']['id']
                        ).click()

                        time.sleep(20)

                        '''
                            Tratamento do arquivo da fatura baixado
                            e variaveis utilizadas
                        '''

                        faturaDownload = f'{self.PASTA_DOWNLOAD}/fatura_{mes_texto}{ano_atual}.pdf'
                        faturaDownloadrename = f'{self.PASTA_DOWNLOAD}/{telefoneAtual}.pdf'
                        faturaPastaLocal = f'{self.PASTA_LOCAL}/Faturas-{mes_txt}/{telefoneAtual}.pdf'

                        os.rename(faturaDownload, faturaDownloadrename)

                        '''
                            Movendo para a pasta do sistema
                        '''

                        shutil.move(faturaDownloadrename, faturaPastaLocal)
                        print(
                            f'O sistema renomeou e moveu a fatura da linha {telefoneAtual} com sucesso')

                        print('refaz o processo todo')

                except NoSuchElementException:
                    print(
                        f'A fatura do telefone: {telefoneAtual} apresentou problemas')

                    # return None

                time.sleep(10)

        self.driver.quit()

    def FuncionaBiribinha(self):
        self.logarSite()
        self.clicaLinkFaturas()
        self.downloadFaturas()


fatura = AutomateVivo()
fatura.FuncionaBiribinha()
