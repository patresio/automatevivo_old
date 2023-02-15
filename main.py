from interfaceGrafica import *
from downloadFaturas import *

window = telaPrincipal()

while True:
    event, values = window.read()
    match(event):
        case '-FATURA-':
            fatura = AutomateVivo()
            fatura.FuncionaBiribinha()
        case None:
            break
        case '-SOBRE-':
            sg.popup_ok('Melhor que o estagiario!')
        case _:
            print(event, values)

window.close()
