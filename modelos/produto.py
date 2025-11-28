# Classe Produto: Representa um item do estoque. Demonstra Encapsulamento através de atributos protegidos.

class Produto:
    
    def __init__(self, codigo: int, nome: str, preco: float, estoque: int):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self._estoque = estoque  # Atributo protegido

    @property
    def estoque(self):
        # Retorna a quantidade atual em estoque
        return self._estoque

    def tem_estoque(self, quantidade: int) -> bool:
        # Verifica se há estoque suficiente para a quantidade solicitada
        return self._estoque >= quantidade

    def reduzir_estoque(self, quantidade: int):
        # Reduz o estoque interno após uma compra confirmada
        if self.tem_estoque(quantidade):
            self._estoque -= quantidade