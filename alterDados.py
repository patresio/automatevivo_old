''' Arquivo para configurações padrões '''

from datetime import date

data_atual = date.today()
ano_atual = data_atual.year

if data_atual.month == 1:
    mes_texto = 'Jan'
if data_atual.month == 2:
    mes_texto = 'Fev'
if data_atual.month == 3:
    mes_texto = 'Mar'
if data_atual.month == 4:
    mes_texto = 'Abr'
if data_atual.month == 5:
    mes_texto = 'Mai'
if data_atual.month == 6:
    mes_texto = 'Jun'
if data_atual.month == 7:
    mes_texto = 'Jul'
if data_atual.month == 8:
    mes_texto = 'Ago'
if data_atual.month == 9:
    mes_texto = 'Set'
if data_atual.month == 10:
    mes_texto = 'Out'
if data_atual.month == 11:
    mes_texto = 'Nov'
if data_atual.month == 12:
    mes_texto = 'Dez'

mes_data = '{}/{}'.format(mes_texto, ano_atual)
mes_txt = '{}{}'.format(mes_texto, ano_atual)