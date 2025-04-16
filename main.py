from rich import print
from rich.console import Console

from biblioteca import biblioteca as bi
from livros import Livro as li


console = Console(highlight= False)


while True:
    print("[bold]Bem vindo a biblioteca Digital[bold]")
    console.print("Todas as opções disponiveis: \n(1)Se cadastrar \n(2)Verificar se o Usuario existe \n(3)Emprestimo do livro \n(4)Devolução \n(5)Cadastrar livro \n(6)Procurar livro \n(7)Ver todos os livros \n(8)Sair")

    while True:
        try:
            escolha = int(input("Digite a opção que você deseja: "))
            break
        except ValueError:
            console.print("Por favor escolha uma opção válida!")


    opcoes = {
        1:bi.cadastro,
        2:bi.user_existe,
        3:bi.emprestar_book,
        4:bi.devolver_book,
        5:li.cadas_livro,
        6:li.procurar_book,
        7:li.look_book
    }


    if escolha == 8:
        console.print("Saindo...")
        break
    elif escolha in opcoes:
        opcoes[escolha]()
    else:
        console.print("selecione uma opção válida!")














