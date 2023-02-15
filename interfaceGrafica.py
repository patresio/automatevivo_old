import PySimpleGUI as sg
from downloadFaturas import AutomateVivo


def telaPrincipal(theme='Reddit'):
    sg.theme(theme)

    layout_l = [
        [sg.Image(filename='imgs/automateLogo.png')],
    ]

    layout_r = [
        [
            sg.Push(),
            sg.Button('Download Faturas!', key='-FATURA-'),
            sg.Push(),
            sg.Button('Junta o PDF!', key='-PDFUNICO-'),
            sg.Push(),
        ],
        [
            sg.Push(),
            sg.Button('Enviar E-mail!', key='-EMAIL-'),
            sg.Push(),
            sg.Button('Sobre o Sistema!', key='-SOBRE-'),
            sg.Push(),
        ],
        [
            sg.Multiline('', key='-RESULT-')
        ]
    ]

    layout = [
        [
            sg.Column(layout_l),
            sg.VSeparator(),
            sg.Column(layout_r)
        ]
    ]

    window = sg.Window(
        'Tela do Sistema',
        layout=layout,
        size=(750, 400)
    )
    return window
