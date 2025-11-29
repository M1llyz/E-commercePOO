# 🛒 LOJA VIRTUAL - SISTEMA DE E-COMMERCE POO

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)
![Tecnologias](https://img.shields.io/badge/Tecnologias-Python%20%7C%20Tkinter%20%7C%20CSV-blue?style=for-the-badge)
![Tipo de Projeto](https://img.shields.io/badge/Tipo-Projeto%20POO-red?style=for-the-badge)

Este projeto é uma aplicação desktop desenvolvida como Trabalho Prático para a disciplina de **Programação Orientada a Objetos (POO)**. O objetivo principal foi criar um **Sistema de Gerenciamento de Loja Virtual** que aplicasse, na prática, os pilares fundamentais da orientação a objetos e princípios sólidos de arquitetura de software.

A aplicação se destaca por separar completamente a **Lógica de Negócios (Back-end)** da **Interface Gráfica (Front-end)**, garantindo um código limpo, modular e fácil de manter. O sistema atende dois perfis de usuário: o **Vendedor** (focado em gestão de estoque) e o **Cliente** (focado na experiência de compra).

## ⚙️ Funcionalidades Principais

* **Gestão de Estoque (CRUD):** O sistema permite cadastrar novos produtos, garantindo a persistência dos dados em arquivo CSV.
* **Interface Gráfica Amigável:** Desenvolvida com **Tkinter (ttk)**, oferecendo abas separadas para "Área do Cliente" e "Área do Vendedor", facilitando a navegação.
* **Carrinho de Compras:** Lógica completa de adição de itens, cálculo de subtotal e total em tempo real.
* **Polimorfismo nos Pagamentos:** O checkout suporta múltiplas formas de pagamento com comportamentos distintos:
    * **Pix:** Simulação de escolha entre QR Code ou Copia e Cola.
    * **Crédito:** Simulação com opção de parcelamento (cálculo de parcelas).
    * **Débito:** Processamento imediato.
* **Nota Fiscal:** Geração automática e visualização do comprovante de compra detalhado.

## 🧠 Arquitetura e Pilares de POO

O desenvolvimento seguiu rigorosamente os conceitos de POO para garantir a qualidade do software:

1.  **Encapsulamento:** As classes de modelo (ex: `Produto`) protegem seus atributos internos, permitindo acesso apenas por métodos seguros.
2.  **Herança:** Utilização de uma classe base `Usuario` para centralizar atributos comuns, herdada pelas entidades `Vendedor` e `Cliente`.
3.  **Polimorfismo:** Implementação de uma classe abstrata `Pagamento` que obriga as classes filhas (`PagamentoPix`, `PagamentoCredito`, etc.) a implementarem suas próprias regras de negócio.
4.  **Responsabilidade Única (SRP):** A classe `RepositorioProduto` é a única responsável por lidar com o arquivo CSV, isolando a lógica de persistência do restante do sistema.

## 🛠️ Tecnologias Utilizadas

O projeto é uma aplicação *desktop* construída com tecnologias nativas e robustas:

* **Python 3.12+:** Linguagem principal.
* **Tkinter (ttk):** Biblioteca nativa para construção da Interface Gráfica (GUI).
* **CSV:** Biblioteca para manipulação de arquivos de texto e persistência de dados.
* **Git:** Controle de versão.

## 🚀 Como Executar Localmente

Para rodar o projeto em sua máquina, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/M1llyz/E-commercePOO.git](https://github.com/M1llyz/E-commercePOO.git)
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd E-commercePOO
    ```
3.  **Execute a interface gráfica:**
    ```bash
    python view/interface.py
    ```
    *Obs: Na primeira execução, o sistema criará automaticamente a pasta `dados/` e o arquivo `produtos.csv`.*

## 📂 Estrutura do Projeto

```
LOJAVIRTUALPOO/
├── .gitignore                      # Configura o que o Git deve ignorar (cache, logs).
├── README.md                       # Documentação/Descrição do projeto.
├── dados/                          # Contém produtos.csv (Arquivo de Persistência).
│   └── produtos.csv                # Arquivo de dados (mantido na raiz por convenção)
├── main.py                         # Front-end de Console (CLI)
├── view/                           # Componentes da Interface Gráfica.
│   ├── assets/                     # Imagens e recursos visuais
│   └── interface.py                # Arquivo principal da Interface Gráfica (Tkinter).
└── modelos/                        # Núcleo de Negócios (Back-end) e Lógica de POO.
    ├── carrinho.py                 # Gerencia o pedido e checkout (Composição).
    ├── cliente.py                  # Perfil do Cliente (Herança).
    ├── loja.py                     # Centraliza a lógica de estoque.
    ├── pagamento.py                # Classes para Polimorfismo.
    ├── produto.py                  # Modelo de dados do item (Encapsulamento).
    ├── repositorio.py              # Gerencia o acesso aos dados (SRP).
    ├── usuario.py                  # Classe base para Herança.
    └── vendedor.py                 # Perfil do Vendedor (Herança).
```

## 🤝 Contribuições

Este é um projeto acadêmico, mas sugestões são bem-vindas! Sinta-se à vontade para abrir uma *issue* para discutir melhorias na arquitetura ou na interface.

## 👨‍💻 Desenvolvedores

* **JAMILLY VERTUOZA DE ARAUJO (jamillya@unisantos.br)**
* **ALI IHSEN KHATIB (alikhatib@unisantos.br)**
* **RAYDA OMAR ANKA (raydaanka@unisantos.br)**

