# Classe Loja: Centraliza a lógica de gerenciamento do estoque de produtos e acesso ao repositório.

from produto import Produto
from repositorio import RepositorioProduto

class Loja:
    
    def __init__(self):
        # Associa a Loja ao Repositório para gerenciar os dados
        self.repositorio_produto = RepositorioProduto() 

    def buscar_produto(self, codigo: int) -> Produto | None:
        # Busca um produto pelo código, delegando ao Repositório
        return self.repositorio_produto.buscar_por_codigo(codigo)

    def adicionar_produto(self, produto: Produto) -> bool:
        # Adiciona um novo produto, delegando ao Repositório
        return self.repositorio_produto.adicionar_produto(produto)