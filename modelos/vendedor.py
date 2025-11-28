# Classe Vendedor: Representa o administrador da loja. Herda de Usuario e possui permissão para cadastrar produtos.

from loja import Loja
from produto import Produto
from usuario import Usuario

class Vendedor(Usuario):
    
    def __init__(self, loja: Loja, nome: str = "Vendedor Master", email: str = "vendedor@loja.com", senha: str = "1234"):
        # Inicializa o vendedor chamando o construtor da classe pai e associando à loja
        super().__init__(nome, email, senha) 
        self.loja_gerenciada = loja 

    def cadastrar_produto(self, produto: Produto) -> bool:
        # Encaminha a solicitação de cadastro do produto para a loja gerenciada (Retorna True se o cadastro for bem-sucedido, False caso contrário)
        return self.loja_gerenciada.adicionar_produto(produto)