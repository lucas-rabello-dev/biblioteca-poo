import json
import openpyxl as xl
import os
import pandas as pd

arquivo_json = "registro_de_livros.json"

class Livro:
    def __init__(self, nome, autor, n_paginas, editora):
        self.nome = nome
        self.autor = autor
        self.n_paginas = n_paginas
        self.editora = editora

    @classmethod
    def cadas_livro(cls):
        nome = input("Digite o nome do livro: ").strip().capitalize()
        autor = input("Digite o nome do autor: ").strip().capitalize()

        while True:
            try:
                n_paginas = int(input("Digite o numero exato de paginas: "))
                break
            except ValueError:
                print("Digite o numero exato de paginas: ")
        
        editora = input("Digite a editora do livro: ").strip().capitalize()


        try:
            with open(arquivo_json, "r") as file:
                livros = json.load(file)
        except FileNotFoundError:
            livros = []


        livros.append({"nome": nome,
                       "autor": autor,
                       "número de páginas": n_paginas,
                       "aditora": editora})


        with open(arquivo_json, "w") as file:
            json.dump(livros, file, indent=4)

        arquivo = "db_livros.xlsx"

        # carregar se o arquivo já existir
        if os.path.exists(arquivo):
            book = xl.load_workbook(arquivo)        
            pagina = book.active
        else:
            # cria o arquivo se não existir
            book = xl.Workbook()
            pagina = book.active
            pagina.title = "db_livros"
            # adiciona cabeçalhos se o arquivo for novo
            pagina.append(["Nome", "Autor", "Número de páginas", "Editora"])
        # adicionar o arquivo
        pagina.append([nome, autor, n_paginas, editora])

        # salva o arquivo
        book.save(arquivo)

        print("Livro cadastrado com sucesso!")


    @classmethod
    def procurar_book(cls):
        dados = pd.read_excel("db_livros.xlsx")  # Carregar o arquivo

        nome = input("Digite o nome do livro: ").strip().capitalize()
        autor = input("Digite o nome do autor: ").strip().capitalize()

        while True:
            try:
                n_paginas = int(input("Digite o número de páginas: ")).strip()
                break
            except ValueError:
                print("Digite um número válido para páginas.")

        editora = input("Digite a editora: ").strip().capitalize()

        # Filtrando os livros que correspondem aos critérios inseridos
        filtro = (
            (dados['Nome'].str.contains(nome, case=False, na=False)) &
            (dados['Autor'].str.contains(autor, case=False, na=False)) &
            (dados['Número de páginas'] == n_paginas) &
            (dados['Editora'].str.contains(editora, case=False, na=False))
        )

        resultados = dados[filtro]

        if not resultados.empty:
            print("\nLivros encontrados:")
            print(resultados)
        else:
            print("\nNenhum livro encontrado com esses critérios.")

    @classmethod
    def look_book(cls):
        dados = pd.read_excel("db_livros.xlsx")
        print(dados)

