# Classe Vendedor: Simula a entidade responsável por cadastrar produtos. Demonstra Associação, pois o Vendedor usa a Loja para gerenciar o estoque.

from .loja import Loja # Associação: Vendedor está associado à Loja 
from .produto import Produto 

class Vendedor:

    SENHA_VENDEDOR = "1234" 

    def __init__(self, loja: Loja):
        self.loja_gerenciada = loja # Guarda a instância da Loja associada 

    def autenticar(self, senha: str) -> bool:
        # Verifica a senha do vendedor
        return senha == self.SENHA_VENDEDOR

    def acessar_cadastro(self):
        # Método de acesso onde solicita a senha do vendedor para iniciar o cadastro
        print("\n--- ACESSO DE VENDEDOR ---")
        senha_digitada = input("Digite a senha para cadastrar um novo produto: ")
        
        if self.autenticar(senha_digitada):
            print("✅ Senha correta! Acesso liberado.")
            self._cadastrar_produto()
        else:
            print("❌ Senha incorreta. Acesso negado.")

    def _cadastrar_produto(self):
        # Lógica para o Vendedor cadastrar um novo produto na Loja
        print("\n--- CADASTRO DE NOVO PRODUTO ---")
        
        # 1. Coleta o Código (omiti loops para brevidade, mas devem ser mantidos)
        while True:
            try:
                codigo = int(input("Digite o Código (número inteiro): "))
                if codigo > 0:
                    break
                print("Código inválido. Digite um número inteiro positivo.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

        # 2. Coleta o Nome
        nome = input("Digite o Nome do Produto: ")
        
        # 3. Coleta o Preço
        while True:
            try:
                preco = float(input("Digite o Preço (ex: 49.90): "))
                if preco > 0:
                    break
                print("Preço inválido. Digite um valor positivo.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

        # 4. Coleta o Estoque
        while True:
            try:
                estoque = int(input("Digite a Quantidade em Estoque: "))
                if estoque >= 0:
                    break
                print("Estoque inválido. Digite um número inteiro não negativo.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

        # 5. Cria o novo objeto Produto
        novo_produto = Produto(codigo, nome, preco, estoque)

        # 6. Adiciona o produto à Loja
        self.loja_gerenciada.adicionar_produto(novo_produto)