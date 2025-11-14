#feito

# Classe Vendedor: Simula a entidade responsável por cadastrar produtos. Demonstra Herança (de Usuario) e Associação (com Loja).

from .loja import Loja 
from .produto import Produto
from .usuario import Usuario # NOVO IMPORT

# Vendedor herda de Usuario
class Vendedor(Usuario): 
    
    def __init__(self, loja: Loja, nome: str = "Vendedor Master", email: str = "vendedor@loja.com", senha: str = "1234"):
        # Chama o construtor da classe base (Usuario)
        super().__init__(nome, email, senha) 
        self.loja_gerenciada = loja 

    def acessar_cadastro(self):
        # Método de interface para gerenciar o processo de cadastro.
        print("\n--- ACESSO DE VENDEDOR ---")
        senha_digitada = input("Digite a senha para cadastrar um novo produto: ")
        
        if self.autenticar(senha_digitada): # Usa o método herdado de Usuario
            print("✅ Senha correta! Acesso liberado.")
            self._coletar_dados_e_cadastrar()
        else:
            print("❌ Senha incorreta. Acesso negado.")

    def _coletar_dados_e_cadastrar(self):
        # Lógica para coletar dados do novo produto (CLI).
        print("\n--- CADASTRO DE NOVO PRODUTO ---")
        
        # 1. Coleta o Código
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

        # 6. Adiciona o produto à Loja (que delega ao Repositório)
        self.loja_gerenciada.adicionar_produto(novo_produto)