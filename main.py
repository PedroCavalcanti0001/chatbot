import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep} Olá {nome}, Resposta aqui 1{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep} Olá {nome}, Resposta aqui 2{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep} Olá {nome}, Resposta aqui 3{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep} Olá {nome}, Resposta aqui 4{os.linesep}')
    else:
        print(f'Escolha uma opção válida! {os.linesep}')


def start():
    print("Olá! Bem-vindo!")
    nome = input(f'Digite seu nome:{os.linesep}')
    email = input(f'Digite seu e-mail:{os.linesep}')
    while (True):
        resposta = input(f'O que gostaria de saber hoje? {os.linesep}'
                         f'[1] - Vale a pena aprender python? {os.linesep}'
                         f'[2] - Quanto tempo leva para conseguir um emprego com python? {os.linesep}'
                         f'[3] - Quando vou saber que sou bom o suficiente? {os.linesep}'
                         f'[4] - O que me recomenda aprender? {os.linesep}')
        processar_resposta(resposta, nome)


if __name__ == "__main__":
    start()
