# feito

# Main: Arquivo principal que executa a lógica do programa da Loja Virtual.

# Importa as classes dos módulos (pacote 'modelos')
from modelos.loja import Loja
from modelos.carrinho import Carrinho
from modelos.vendedor import Vendedor 
from modelos.cliente import Cliente 
from modelos.pagamento import PagamentoPix, PagamentoDebito, PagamentoCredito


def menu_pagamento(carrinho: Carrinho, minha_loja: Loja): # Adiciona minha_loja
    # Gerencia o Sub-Menu de Pagamentos, usa as classes polimórficas
    while True:
        print("\n=================================")
        print("        PROCESSO DE PAGAMENTO    ")
        print("=================================")
        carrinho.exibir_carrinho() 
        print("1. Escolher Forma de Pagamento")
        print("2. Voltar ao Menu Principal")
        escolha_pagamento = input("Escolha uma opção (1-2): ")

        if escolha_pagamento == "1":
            # Sub-Menu de Formas de Pagamento
            print("\n--- ESCOLHA A FORMA DE PAGAMENTO ---")
            print("1. PIX")
            print("2. Débito")
            print("3. Crédito")
            forma_pagamento_opcao = input("Escolha uma opção (1-3): ")

            objeto_pagamento = None
            if forma_pagamento_opcao == "1":
                objeto_pagamento = PagamentoPix(carrinho.valor_total)
            elif forma_pagamento_opcao == "2":
                objeto_pagamento = PagamentoDebito(carrinho.valor_total)
            elif forma_pagamento_opcao == "3":
                objeto_pagamento = PagamentoCredito(carrinho.valor_total)
            else:
                print("❌ Opção de pagamento inválida. Voltando ao menu de pagamento.")
                continue 

            # Processa a compra: Passa o objeto Pagamento (Polimorfismo) e a Loja (SRP)
            carrinho.processar_compra(objeto_pagamento, minha_loja) 
            
            # Opções após a compra
            print("\n=================================")
            print("1. Voltar para o Menu Inicial")
            print("2. Sair")
            escolha_final = input("Escolha uma opção (1-2): ")

            if escolha_final == "2":
                exit() 

            return 

        elif escolha_pagamento == "2":
            return 

        else:
            print("❌ Opção inválida. Por favor, escolha 1 ou 2.")

def main():
    # Instancia as classes (os objetos) que serão utilizados
    minha_loja = Loja()
    meu_carrinho = Carrinho()
    
    # Instanciação com Herança
    meu_vendedor = Vendedor(minha_loja, nome="Maria", email="maria@loja.com") 
    meu_cliente = Cliente(nome="João", email="joao@cliente.com") 

    meu_cliente.exibir_boas_vindas() 
    
    while True:
        # O Menu Principal
        print("\n=================================")
        print("    BEM-VINDO À LOJA VIRTUAL     ")
        print("=================================")
        print("O que você deseja fazer?")
        print("1. Ver Produtos Disponíveis (Cliente/Vendedor)")
        print("2. Adicionar Produto ao Carrinho (Cliente)")
        print("3. Ver Carrinho e Total (Cliente)")
        print("4. Finalizar Compra (Cliente)")
        print("5. CADASTRAR NOVO PRODUTO (Vendedor - Requer Senha)")
        print("6. Sair")
        escolha = input("Escolha uma opção (1-6): ")

        if escolha == "1":
            minha_loja.exibir_estoque()

        elif escolha == "2":
            try:
                codigo = int(input("Digite o CÓDIGO do produto que deseja adicionar: "))
                produto_selecionado = minha_loja.buscar_produto(codigo)

                if produto_selecionado:
                    # Busca o produto novamente para garantir que ele é um objeto que o Carrinho pode rastrear
                    produto_para_carrinho = minha_loja.buscar_produto(codigo) 
                    
                    quantidade = int(input(f"Quantas unidades de {produto_para_carrinho.nome} você deseja? "))
                    meu_carrinho.adicionar_ao_carrinho(produto_para_carrinho, quantidade)
                else:
                    print("❌ Erro: Produto não encontrado.")
            except ValueError:
                print("❌ Erro: Entrada inválida (código ou quantidade devem ser números inteiros).")

        elif escolha == "3":
            meu_carrinho.exibir_carrinho()

        elif escolha == "4":
            if meu_carrinho.esta_vazio():
                print("❌ Não é possível finalizar a compra. O carrinho está vazio.")
            else:
                # Passa a Loja para o menu de pagamento
                menu_pagamento(meu_carrinho, minha_loja)

        elif escolha == "5":
            meu_vendedor.acessar_cadastro()

        elif escolha == "6":
            print("Obrigado por usar a Loja Virtual. Até mais!")
            break

        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 6.")

if __name__ == "__main__":
    main()