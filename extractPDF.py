# Imports Python
import PyPDF2
import os
# My imports
from alterDados import mes_txt

pasta_local = os.getcwd()
nome_pasta_fatura = f'Faturas-{mes_txt}'

pasta_fatura = os.path.join(pasta_local, nome_pasta_fatura)

for filename in os.listdir(pasta_fatura):
    print(filename)
