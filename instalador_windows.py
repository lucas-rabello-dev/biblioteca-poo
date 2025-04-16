from os import system
from time import sleep

# tempo de espera para eviatar erros dos comandos
tempo = 1.0

print("Esse é o instalador das bibliotecas usadas do projeto 'biblioteca-poo' ")


while True:
    p2 = input("Digite (s) para iniciar a instalação das libs usando pip no seu windows ou (n) para sair: ")

    if p2 == "s":
        system("pip install pandas ")
        sleep(tempo)
        system("pip install openpyxl ")
        sleep(tempo)
        system("pip install rich ")
        sleep(1.0)
        print("Todas as bibliotecas instaladas! \n ")
        break
    elif p2 == "n":
        print("Saindo do instalador! \n")
        break
    else:
        print("Digite apenas (s) ou (n)! \n")