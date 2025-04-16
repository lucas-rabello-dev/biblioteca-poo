import re
import json
import datetime
import openpyxl as xl
import os 
import pandas as pd




class biblioteca:
    def __init__(self, nome, idade, email, cpf):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf

    @classmethod
    def cadastro(cls):
        vnome = input("Digite seu nome para o cadastro: ").strip().capitalize()

        while True:
            try:
                vidade = int(input("Digite sua idade: "))
                break
            except ValueError:
                print("Por favor insira um numero válido! ")
                print("\n")

        #varificação do email para ver se ele é valido
        while True:
            vemail = input("Digite um email válido: ").strip()
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', vemail):
                break
            print("Email inválido, tente novamente!\n")

        # verificar o CPF
        while True:
            vcpf = input("Digite um CPF válido (somente números): ").strip()
            if re.match(r'^\d{11}$', vcpf):  
                break
            print("CPF inválido, tente novamente!\n")


        try:
            with open("cadastro_biblioteca.json", "r") as file:
                dados = json.load(file)                   
        
        except (FileNotFoundError, json.JSONDecodeError):
            dados = []

        dados.append({
            "nome":vnome,
            "idade":vidade,
            "email":vemail,
            "CPF":vcpf})

        with open("cadastro_biblioteca.json", "w") as file:
            json.dump(dados, file, indent=4)

        print("Cliente cadastrado com sucesso!")
    
    @classmethod
    def user_existe(cls):
        email = input("Digite o seu email exato sem erros para que possa verificar sua existência: ").strip()
        try:
            with open("cadastro_biblioteca.json", "r") as file:
                usuarios = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Nenhum usuário registrado no sistema!")
            return

        for usuario in usuarios:
            if usuario["email"] == email:
                print(f"Esse email {email} está registrado!")
                return True
        print(f"O email {email} não está registrado!")
        return False


    @classmethod
    def emprestar_book2(cls, email):
        emprestimos = {}
        
        try:
            with open("emprestimos.json", "r") as f:
                emprestimos = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        if email in emprestimos:
            print("Este usuário já tem um livro emprestado!")
            return

        livro = input("Digite o nome do livro: ").strip().capitalize()
        dias_prazo = 7  # Prazo de 7 dias para devolução
        data_emprestimo = datetime.datetime.now()
        data_devolucao = data_emprestimo + datetime.timedelta(days=dias_prazo)

        arquivo = "db_livros.xlsx"

        if os.path.exists(arquivo):
            dados = pd.read_excel(arquivo)
        else:
            print("Não existe nanhum livro cadastrado!")
            return

        

        lista = dados["Nome"].tolist()


        if livro in lista:

            emprestimos[email] = {
                "livro": livro,
                "data_emprestimo": data_emprestimo.strftime("%Y-%m-%d"),
                "data_devolucao": data_devolucao.strftime("%Y-%m-%d"),
                "status": "Emprestado"
            }

            with open("emprestimos.json", "w") as f:
                json.dump(emprestimos, f, indent=4)

            print(f"Livro '{livro}' emprestado para {email}. Deve ser devolvido até {data_devolucao.strftime('%d/%m/%Y')}.")
        else:
            print(f"Oops o livro {livro} não existe em nosso estoque!")

    # Verificação para ver se o email está registrado
    @classmethod
    def emprestar_book(cls):
        while True:
            vemail = input("Digite o seu email: ")
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', vemail):
                break
            print("formato de email inválido, tente novamente!\n")
        
        if cls.user_existe():
            print("Usuário cadastrado!")
            cls.emprestar_book2(vemail)
        else:
            print(f"O email {vemail} não está cadastrado no sistema!")


    @classmethod
    def devolver_book(cls):
        email = input("Digite o seu email exato sem erros: ").strip()
        try:
            with open("emprestimos.json", "r") as f:
                emprestimos = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Nenhum empréstimo encontrado.")
            return

        if email not in emprestimos:
            print("Nenhum livro emprestado para este usuário.")
            return

        data_devolucao_real = datetime.datetime.now()
        data_devolucao_prevista = datetime.datetime.strptime(
            emprestimos[email]["data_devolucao"], "%Y-%m-%d"
        )

        if data_devolucao_real > data_devolucao_prevista:
            emprestimos[email]["status"] = "Atrasado"
            print("Livro devolvido com atraso!")
        else:
            emprestimos[email]["status"] = "Devolvido"
            print("Livro devolvido no prazo.")

        emprestimos[email]["data_devolucao_real"] = data_devolucao_real.strftime("%Y-%m-%d")

        with open("emprestimos.json", "w") as f:
            json.dump(emprestimos, f, indent=4)

        print("Registro atualizado com sucesso!")
    

















