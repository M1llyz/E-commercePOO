#feito

# Classe Produto: Representa um item que pode ser vendido na loja. Demonstra Encapsulamento, pois o estoque é alterado apenas por métodos.

class Produto:
    
    def __init__(self, codigo: int, nome: str, preco: float, estoque: int):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self._estoque = estoque  # Atributo "protegido"

    @property
    def estoque(self):
        # Retorna a quantidade atual em estoque
        return self._estoque

    def tem_estoque(self, quantidade: int) -> bool:
        # Verifica se há estoque suficiente para a quantidade solicitada pelo cliente
        return self._estoque >= quantidade

    def reduzir_estoque(self, quantidade: int):
        # Reduz o estoque interno após uma compra.
        if self.tem_estoque(quantidade):
            self._estoque -= quantidade
        else:
            pass # Em caso de erro, apenas não faz nada no estoque.

    def exibir_detalhes(self):
        # Exibe as informações do produto
        print(f"| {self.codigo:<6} | {self.nome:<20} | R$ {self.preco:8.2f} | {self.estoque:7} |")