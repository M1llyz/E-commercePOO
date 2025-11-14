# feito

# Implementando o SRP: Única classe responsável pela persistência (CRUD) de objetos Produto em um arquivo CSV, isolando a lógica de dados.

import csv
import os
from .produto import Produto

class RepositorioProduto:
    
    ARQUIVO_CSV = 'dados/produtos.csv'
    COLUNAS = ['codigo', 'nome', 'preco', 'estoque']

    def __init__(self):
        # Garante que a pasta "dados" exista
        os.makedirs(os.path.dirname(self.ARQUIVO_CSV), exist_ok=True)
        # Verifica se o arquivo precisa ser inicializado (não existe ou está vazio)
        if not os.path.exists(self.ARQUIVO_CSV) or os.stat(self.ARQUIVO_CSV).st_size == 0:
            self._criar_arquivo_base()
            self._popular_estoque_inicial()
            
    def _criar_arquivo_base(self):
        # Cria o arquivo CSV com o cabeçalho.
        with open(self.ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.COLUNAS)
            writer.writeheader()
            
    def _popular_estoque_inicial(self):
        # Adiciona os produtos iniciais da Loja ao CSV.
        produtos_iniciais = [
            Produto(101, "Camiseta Básica", 49.90, 50),
            Produto(102, "Calça Jeans", 129.90, 25),
            Produto(103, "Tênis Esportivo", 199.99, 10),
            Produto(104, "Meia Pack (3)", 19.50, 100)
        ]
        
        # Abre o arquivo no modo append
        with open(self.ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.COLUNAS)
            for produto in produtos_iniciais:
                 writer.writerow({
                    'codigo': produto.codigo,
                    'nome': produto.nome,
                    'preco': produto.preco,
                    'estoque': produto.estoque
                })
        print("Repositório inicializado e populado com dados base no CSV.")

    
    def buscar_todos(self) -> list[Produto]:
        # Lê todos os registros do CSV e retorna como lista de objetos Produto.
        produtos = []
        try:
            # Força a reabertura no modo 'r' (leitura)
            with open(self.ARQUIVO_CSV, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for linha in reader:
                    produto = Produto(
                        codigo=int(linha['codigo']),
                        nome=linha['nome'],
                        preco=float(linha['preco']),
                        estoque=int(linha['estoque'])
                    )
                    produtos.append(produto)
        except FileNotFoundError:
            pass 
        except Exception as e:
            print(f"Erro ao ler o repositório: {e}")
            
        return produtos

    def buscar_por_codigo(self, codigo: int) -> Produto | None:
        # Busca um único produto pelo código, lendo o CSV.
        for produto in self.buscar_todos():
            if produto.codigo == codigo:
                return produto
        return None
    
    def salvar_todos(self, produtos: list[Produto]):
        # Sobrescreve o CSV com a lista completa de produtos (usado para o UPDATE de estoque).
        # Abre no modo 'w' (write), o que apaga o conteúdo anterior
        with open(self.ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as f: 
            writer = csv.DictWriter(f, fieldnames=self.COLUNAS)
            writer.writeheader()
            for produto in produtos:
                writer.writerow({
                    'codigo': produto.codigo,
                    'nome': produto.nome,
                    'preco': produto.preco,
                    'estoque': produto.estoque
                })

    def adicionar_produto(self, produto: Produto) -> bool:
        # Adiciona um novo produto ao CSV.
        
        # 1. Verifica duplicidade lendo o arquivo atualizado
        if self.buscar_por_codigo(produto.codigo): 
             print(f"Erro: Produto com código {produto.codigo} já existe. Não foi adicionado.")
             return False
        
        # 2. Adiciona o novo produto ao final do arquivo
        with open(self.ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.COLUNAS)
            writer.writerow({
                'codigo': produto.codigo,
                'nome': produto.nome,
                'preco': produto.preco,
                'estoque': produto.estoque
            })
        print(f"Produto '{produto.nome}' (Cód: {produto.codigo}) adicionado ao estoque da Loja!")
        return True