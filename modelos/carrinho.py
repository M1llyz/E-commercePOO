# Classe Carrinho: Gerencia os produtos que o cliente deseja comprar. Demonstra Composição (itens_comprados) e orquestra o Polimorfismo.

from datetime import datetime
from produto import Produto
from loja import Loja
from pagamento import Pagamento

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

    def adicionar_ao_carrinho(self, produto: Produto, quantidade: int) -> tuple[bool, str]:
        # Adiciona um produto ao carrinho verificando o estoque e retorna status
        if quantidade <= 0:
            return False, "A quantidade deve ser maior que zero."

        if produto.tem_estoque(quantidade):
            if produto in self.itens_comprados:
                self.itens_comprados[produto] += quantidade
            else:
                self.itens_comprados[produto] = quantidade
            return True, f"{quantidade}x {produto.nome} adicionado(s) ao carrinho."
        else:
            return False, f"Estoque insuficiente para {produto.nome}. Disponível: {produto.estoque}."

    def processar_compra(self, objeto_pagamento: Pagamento, minha_loja: Loja) -> dict:
        # Processa o pagamento, atualiza o estoque e retorna o resultado da operação
        resultado_pagamento = objeto_pagamento.processar()
        status_transacao = resultado_pagamento["status"]

        nota_fiscal = ""
        sucesso = False

        if status_transacao == "APROVADO":
            # Atualiza o estoque e persiste no CSV
            estoque_atualizado = minha_loja.repositorio_produto.buscar_todos()

            for produto_no_carrinho, quantidade_comprada in self.itens_comprados.items():
                for produto_no_estoque in estoque_atualizado:
                    if produto_no_carrinho.codigo == produto_no_estoque.codigo:
                        produto_no_estoque.reduzir_estoque(quantidade_comprada)
                        break

            minha_loja.repositorio_produto.salvar_todos(estoque_atualizado)
            
            # Gera o texto da nota fiscal antes de limpar o carrinho
            nota_fiscal = self._gerar_texto_nota_fiscal(resultado_pagamento)
            
            self.itens_comprados.clear()
            sucesso = True
        else:
            # Caso seja PENDENTE (PIX) ou RECUSADO
            nota_fiscal = f"Transação {status_transacao}. {resultado_pagamento['detalhe']}"

        return {
            "sucesso": sucesso,
            "status": status_transacao,
            "nota_fiscal": nota_fiscal,
            "dados_pagamento": resultado_pagamento
        }

    def _gerar_texto_nota_fiscal(self, resultado_pagamento: dict) -> str:
        # Gera a string da Nota Fiscal para exibição na interface
        forma_pagamento = resultado_pagamento["forma"]
        status_transacao = resultado_pagamento["status"]
        detalhe_transacao = resultado_pagamento["detalhe"]
        
        texto = "=================================\n"
        texto += "         NOTA FISCAL SIMPLES     \n"
        texto += "=================================\n"
        texto += f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        texto += "---------------------------------\n"
        
        for produto, quantidade in self.itens_comprados.items():
            subtotal = produto.preco * quantidade
            texto += f"{produto.nome} (x{quantidade}): R$ {subtotal:.2f}\n"
        
        texto += "---------------------------------\n"
        texto += f"TOTAL: R$ {self.valor_total:.2f}\n"
        texto += f"PAGAMENTO: {forma_pagamento}\n"
        
        if forma_pagamento == "Crédito":
            parcelas = resultado_pagamento.get("parcelas", 1)
            valor_parcela = resultado_pagamento.get("valor_parcela", self.valor_total)
            texto += f"PARCELAMENTO: {parcelas}x de R$ {valor_parcela:.2f}\n"

        texto += f"STATUS: {status_transacao}\n"
        texto += "================================="
        return texto