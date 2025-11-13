# Classe Loja: Centraliza o gerenciamento do estoque de produtos. Demonstra Agregação, pois agrega a lista de objetos Produto.

from .produto import Produto  # Importa a classe Produto do mesmo pacote

class Loja:
    
    def __init__(self):
        # Lista de produtos disponíveis na loja (Estoque)
        self.estoque_produtos = [
            # Inicializando objetos (Produtos)
            Produto(101, "Camiseta Básica", 49.90, 50),
            Produto(102, "Calça Jeans", 129.90, 25),
            Produto(103, "Tênis Esportivo", 199.99, 10),
            Produto(104, "Meia Pack (3)", 19.50, 100)
        ]
        print("Loja Virtual inicializada com 4 produtos no estoque.")

    def exibir_estoque(self):
        # Exibe todos os produtos disponíveis no estoque
        print("\n=======================================================")
        print("               PRODUTOS DISPONÍVEIS NA LOJA            ")
        print("=======================================================")
        print("| Código | Nome                 | Preço (R$) | Estoque |")
        print("-------------------------------------------------------")
        
        for produto in self.estoque_produtos:
            produto.exibir_detalhes() 
        print("=======================================================")

    def buscar_produto(self, codigo: int) -> Produto | None:
        # Busca um produto pelo código
        for produto in self.estoque_produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def adicionar_produto(self, produto: Produto) -> bool:
        # Adiciona um novo produto ao estoque da loja
        if self.buscar_produto(produto.codigo):
            print(f"❌ Erro: Produto com código {produto.codigo} já existe. Não foi adicionado.")
            return False
        
        self.estoque_produtos.append(produto)
        print(f"✅ Produto '{produto.nome}' (Cód: {produto.codigo}) adicionado ao estoque da Loja!")
        return True