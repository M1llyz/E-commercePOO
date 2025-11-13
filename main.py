# Main: Arquivo principal que executa a lógica do programa da Loja Virtual.

# Importa as classes dos módulos (pacote 'modelos')
from modelos.loja import Loja
from modelos.carrinho import Carrinho
from modelos.vendedor import Vendedor 


def menu_pagamento(carrinho: Carrinho):
    #Gerencia o Sub-Menu de Pagamentos
    while True:
        print("\n=================================")
        print("        PROCESSO DE PAGAMENTO    ")
        print("=================================")
        carrinho.exibir_carrinho() # Exibe o resumo do carrinho
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

            nome_forma_pagamento = ""
            if forma_pagamento_opcao == "1":
                nome_forma_pagamento = "PIX"
            elif forma_pagamento_opcao == "2":
                nome_forma_pagamento = "Débito"
            elif forma_pagamento_opcao == "3":
                nome_forma_pagamento = "Crédito"
            else:
                print("❌ Opção de pagamento inválida. Voltando ao menu de pagamento.")
                continue 

            # Processa a compra (atualiza o estoque e emite nota fiscal)
            carrinho.processar_compra(nome_forma_pagamento)
            
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
    # Função principal que executa a lógica do programa. Instancia as classes (os objetos) que serão utilizados
    minha_loja = Loja()
    meu_carrinho = Carrinho()
    meu_vendedor = Vendedor(minha_loja) # Vendedor é instanciado com a Loja associada

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
                    quantidade = int(input(f"Quantas unidades de {produto_selecionado.nome} você deseja? "))
                    meu_carrinho.adicionar_ao_carrinho(produto_selecionado, quantidade)
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
                menu_pagamento(meu_carrinho)

        elif escolha == "5":
            meu_vendedor.acessar_cadastro()

        elif escolha == "6":
            print("Obrigado por usar a Loja Virtual. Até mais!")
            break

        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 6.")

if __name__ == "__main__":
    main()