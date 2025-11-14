#feito

# Classe Loja: Centraliza a lógica de gerenciamento do estoque de produtos. Demonstra Associação com o Repositório para acessar os dados.

from .produto import Produto  
from .repositorio import RepositorioProduto # NOVO IMPORT

class Loja:
    
    def __init__(self):
        # Associa a Loja ao Repositório para gerenciar os dados
        self.repositorio_produto = RepositorioProduto() 
        print("Loja Virtual inicializada. Estoque gerenciado por Repositório CSV.")

    def exibir_estoque(self):
        # Lê os produtos disponíveis, delegando ao Repositório
        produtos = self.repositorio_produto.buscar_todos() 
        
        print("\n=======================================================")
        print("               PRODUTOS DISPONÍVEIS NA LOJA            ")
        print("=======================================================")
        print("| Código | Nome                 | Preço (R$) | Estoque |")
        print("-------------------------------------------------------")
        
        for produto in produtos: 
            produto.exibir_detalhes() 
        print("=======================================================")

    def buscar_produto(self, codigo: int) -> Produto | None:
        # Busca um produto pelo código, delegando ao Repositório
        return self.repositorio_produto.buscar_por_codigo(codigo)

    def adicionar_produto(self, produto: Produto) -> bool:
        # Adiciona um novo produto, delegando ao Repositório
        return self.repositorio_produto.adicionar_produto(produto)