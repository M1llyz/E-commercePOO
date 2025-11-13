# Classe Carrinho: Gerencia os produtos que o cliente deseja comprar. Demonstra Composição, pois o carrinho é composto por instâncias de Produto.

from datetime import datetime
from .produto import Produto  # Importa a classe Produto do mesmo pacote

class Carrinho:
    
    def __init__(self):
        # Dicionário para armazenar {Produto: Quantidade}
        self.itens_comprados = {}

    @property
    def valor_total(self) -> float:
        # Calcula o valor total dos itens no carrinho
        total = 0.0
        for produto, quantidade in self.itens_comprados.items():
            total += produto.preco * quantidade
        return total

    def esta_vazio(self) -> bool:
        # Verifica se o carrinho está vazio
        return len(self.itens_comprados) == 0

    def adicionar_ao_carrinho(self, produto: Produto, quantidade: int):
        # Adiciona um produto ao carrinho verificando o estoque
        if quantidade <= 0:
            print("❌ Erro: A quantidade deve ser maior que zero.")
            return

        if produto.tem_estoque(quantidade):
            if produto in self.itens_comprados:
                self.itens_comprados[produto] += quantidade
            else:
                self.itens_comprados[produto] = quantidade
            print(f"✅ {quantidade}x {produto.nome} adicionado(s) ao carrinho.")
        else:
            print(f"❌ Erro: Estoque insuficiente para {produto.nome}. Disponível: {produto.estoque}.")

    def exibir_carrinho(self):
        # Exibe os itens do carrinho
        print("\n--- RESUMO DO CARRINHO ---")
        if self.esta_vazio():
            print("O carrinho está vazio.")
            return

        for produto, quantidade in self.itens_comprados.items():
            subtotal = produto.preco * quantidade
            print(f"- {quantidade}x {produto.nome} (R$ {produto.preco:.2f} cada) = R$ {subtotal:.2f}")
        print("--------------------------")
        print(f"VALOR TOTAL: R$ {self.valor_total:.2f}")
        print("--------------------------")

    def processar_compra(self, forma_pagamento: str):
        # Simula o processamento final da compra, atualiza estoque e emitindo nota fiscal
        print("\n=================================")
        print("      REALIZANDO PAGAMENTO...    ")
        print("=================================")
        print(f"Pagamento via {forma_pagamento} de R$ {self.valor_total:.2f} APROVADO!")

        # 1. Atualiza o estoque para cada produto no carrinho
        print("\n--- ATUALIZANDO ESTOQUE ---")
        for produto, quantidade in self.itens_comprados.items():
            produto.reduzir_estoque(quantidade)

        # 2. Emite a Nota Fiscal simulada
        self._emitir_nota_fiscal(forma_pagamento)

        # 3. Limpa o carrinho
        self.itens_comprados.clear()
        print("\nCompra realizada com sucesso!")

    def _emitir_nota_fiscal(self, forma_pagamento: str):
        # Simula a emissão de uma Nota Fiscal
        print("\n=================================")
        print("         NOTA FISCAL SIMPLES     ")
        print("=================================")
        print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print("---------------------------------")
        print("| Cód. | Produto         | Valor (R$) | Qtd | Subtotal (R$) |")
        print("-------------------------------------------------------------")
        
        for produto, quantidade in self.itens_comprados.items():
            subtotal = produto.preco * quantidade
            print(f"| {produto.codigo:<4} | {produto.nome:<15} | {produto.preco:10.2f} | {quantidade:3} | {subtotal:13.2f} |")
        
        print("-------------------------------------------------------------")
        print(f"| VALOR TOTAL:                                | {self.valor_total:13.2f} |")
        print(f"| FORMA DE PAGAMENTO:                         | {forma_pagamento:<13} |")
        print("=============================================================")