from os import system
from time import sleep

# tempo de espera para eviatar erros dos comandos
tempo = 1.0

print("Esse é o instalador das bibliotecas usadas do projeto 'biblioteca-poo' ")

break_linux = "--break-system-packages"

while True:
    p = input("Deseja usar o parâmetro: '--break-system-packages' em suas instalações (s) ou (n)? ")

    if p == "s":
        print("OK! \n")
        break
    elif p == "n":
        break_linux = ""
        break
    else:
        print("Por favor digite apenas (s) ou (n) \n")


while True:
    p2 = input("Digite (s) para iniciar a instalação das libs usando pip no seu linux ou (n) para sair: ")

    if p2 == "s":
        system("pip install pandas " + break_linux)
        sleep(tempo)
        system("pip install openpyxl " + break_linux)
        sleep(tempo)
        system("pip install rich " + break_linux)
        sleep(1.0)
        print("Todas as bibliotecas instaladas! \n ")
        break
    elif p2 == "n":
        print("Saindo do instalador! \n")
        break
    else:
        print("Digite apenas (s) ou (n)! \n")

