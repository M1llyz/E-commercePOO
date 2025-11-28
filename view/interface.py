# Arquivo principal da Interface Gráfica (Tkinter). Atua como a camada de visualização (Front-end).

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Adiciona o diretório 'modelos' (localizado um nível acima) ao sys.path para permitir a importação dos módulos de negócio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modelos')))

from loja import Loja
from carrinho import Carrinho
from produto import Produto
from vendedor import Vendedor
from cliente import Cliente
from pagamento import PagamentoPix, PagamentoCredito, PagamentoDebito

class LojaApp(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Sistema de Loja Virtual POO")
        self.geometry("1000x700")
        
        # Configuração de Estilo Visual
        style = ttk.Style()
        style.theme_use('clam') 
        
        # Inicialização das classes de negócio
        self.loja = Loja()
        self.carrinho = Carrinho()
        self.cliente = Cliente("Cliente Interface", "cliente@email.com")
        self.vendedor = Vendedor(self.loja)

        # Configuração do Container de Abas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        self.criar_aba_cliente()
        self.criar_aba_vendedor()
        
    def criar_aba_cliente(self):
        # Configura a aba destinada às operações do cliente (compra)
        tab_cliente = ttk.Frame(self.notebook)
        self.notebook.add(tab_cliente, text="🛒 Área do Cliente (Comprar)")

        # Layout dividido: Esquerda (Produtos) e Direita (Carrinho)
        frame_esq = ttk.Frame(tab_cliente)
        frame_esq.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        frame_dir = ttk.Frame(tab_cliente)
        frame_dir.pack(side='right', fill='both', expand=True, padx=10, pady=10)

        # Tabela de Produtos (Treeview)
        ttk.Label(frame_esq, text="Produtos Disponíveis", font=('Arial', 12, 'bold')).pack(pady=5)
        
        colunas = ('cod', 'nome', 'preco', 'estoque')
        self.tree_produtos = ttk.Treeview(frame_esq, columns=colunas, show='headings', height=15)
        self.tree_produtos.heading('cod', text='Cód')
        self.tree_produtos.heading('nome', text='Nome')
        self.tree_produtos.heading('preco', text='Preço (R$)')
        self.tree_produtos.heading('estoque', text='Estoque')
        
        self.tree_produtos.column('cod', width=50, anchor='center')
        self.tree_produtos.column('preco', width=80, anchor='e')
        self.tree_produtos.column('estoque', width=60, anchor='center')
        
        self.tree_produtos.pack(fill='both', expand=True)
        
        # Controles de Adição ao Carrinho
        frame_botoes = ttk.Frame(frame_esq)
        frame_botoes.pack(pady=10, fill='x')
        
        ttk.Label(frame_botoes, text="Quantidade:").pack(side='left', padx=5)
        self.qtd_var = tk.StringVar(value="1")
        ttk.Entry(frame_botoes, textvariable=self.qtd_var, width=5).pack(side='left')
        ttk.Button(frame_botoes, text="Adicionar ao Carrinho (+)", command=self.adicionar_ao_carrinho).pack(side='left', padx=10)
        
        # Resumo do Carrinho
        ttk.Label(frame_dir, text="Seu Carrinho", font=('Arial', 12, 'bold')).pack(pady=5)
        
        self.lista_carrinho = tk.Listbox(frame_dir, width=40, height=15)
        self.lista_carrinho.pack(fill='both', expand=True)
        
        self.lbl_total = ttk.Label(frame_dir, text="Total: R$ 0.00", font=('Arial', 11, 'bold'))
        self.lbl_total.pack(pady=10)
        
        ttk.Button(frame_dir, text="FINALIZAR COMPRA (Checkout)", command=self.abrir_checkout).pack(pady=5, fill='x')
        ttk.Button(frame_dir, text="Limpar Carrinho", command=self.limpar_carrinho).pack(pady=5)

        self.atualizar_tabela_produtos()

    def criar_aba_vendedor(self):
        # Configura a aba destinada ao cadastro de produtos pelo vendedor
        tab_vendedor = ttk.Frame(self.notebook)
        self.notebook.add(tab_vendedor, text="📦 Área do Vendedor (Cadastrar)")

        frame_form = ttk.LabelFrame(tab_vendedor, text=" Cadastrar Novo Produto ", padding=20)
        frame_form.pack(pady=20, padx=20)

        grid_opts = {'padx': 5, 'pady': 5, 'sticky': 'w'}
        
        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, **grid_opts)
        self.ent_cod = ttk.Entry(frame_form)
        self.ent_cod.grid(row=0, column=1, **grid_opts)

        ttk.Label(frame_form, text="Nome:").grid(row=1, column=0, **grid_opts)
        self.ent_nome = ttk.Entry(frame_form)
        self.ent_nome.grid(row=1, column=1, **grid_opts)

        ttk.Label(frame_form, text="Preço:").grid(row=2, column=0, **grid_opts)
        self.ent_preco = ttk.Entry(frame_form)
        self.ent_preco.grid(row=2, column=1, **grid_opts)

        ttk.Label(frame_form, text="Estoque Inicial:").grid(row=3, column=0, **grid_opts)
        self.ent_estoque = ttk.Entry(frame_form)
        self.ent_estoque.grid(row=3, column=1, **grid_opts)

        ttk.Button(frame_form, text="Salvar Produto", command=self.cadastrar_produto).grid(row=4, column=0, columnspan=2, pady=15)

    def atualizar_tabela_produtos(self):
        # Busca os dados atualizados do repositório e recarrega a Treeview
        for item in self.tree_produtos.get_children():
            self.tree_produtos.delete(item)
            
        produtos = self.loja.repositorio_produto.buscar_todos()
        
        for p in produtos:
            self.tree_produtos.insert('', 'end', values=(p.codigo, p.nome, f"{p.preco:.2f}", p.estoque))

    def adicionar_ao_carrinho(self):
        # Lógica de interação entre a tabela de produtos e a entidade Carrinho
        selected = self.tree_produtos.selection()
        if not selected:
            messagebox.showwarning("Atenção", "Selecione um produto na tabela primeiro.")
            return

        item_values = self.tree_produtos.item(selected[0])['values']
        cod_produto = item_values[0]
        
        produto_obj = self.loja.buscar_produto(int(cod_produto))
        
        try:
            qtd = int(self.qtd_var.get())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida.")
            return

        sucesso, mensagem = self.carrinho.adicionar_ao_carrinho(produto_obj, qtd)
        
        if sucesso:
            self.atualizar_lista_carrinho()
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showerror("Erro de Estoque", mensagem)

    def atualizar_lista_carrinho(self):
        # Atualiza a Listbox e o label de total com base no estado atual do carrinho
        self.lista_carrinho.delete(0, tk.END)
        for prod, qtd in self.carrinho.itens_comprados.items():
            subtotal = prod.preco * qtd
            self.lista_carrinho.insert(tk.END, f"{qtd}x {prod.nome} - R$ {subtotal:.2f}")
        
        self.lbl_total.config(text=f"Total: R$ {self.carrinho.valor_total:.2f}")

    def limpar_carrinho(self):
        # Limpa os itens do carrinho e atualiza a interface
        self.carrinho.itens_comprados.clear()
        self.atualizar_lista_carrinho()

    def cadastrar_produto(self):
        # Coleta dados do formulário e invoca o método de cadastro do Vendedor
        try:
            cod = int(self.ent_cod.get())
            nome = self.ent_nome.get()
            preco = float(self.ent_preco.get())
            estoque = int(self.ent_estoque.get())
            
            novo_prod = Produto(cod, nome, preco, estoque)
            
            if self.vendedor.cadastrar_produto(novo_prod):
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
                self.ent_cod.delete(0, tk.END)
                self.ent_nome.delete(0, tk.END)
                self.ent_preco.delete(0, tk.END)
                self.ent_estoque.delete(0, tk.END)
                self.atualizar_tabela_produtos()
            else:
                messagebox.showerror("Erro", "Produto com este código já existe.")
                
        except ValueError:
            messagebox.showerror("Erro", "Verifique se os campos numéricos estão corretos.")

    def abrir_checkout(self):
        # Abre janela secundária (Toplevel) para seleção de pagamento
        if self.carrinho.esta_vazio():
            messagebox.showwarning("Vazio", "O carrinho está vazio.")
            return

        checkout_win = tk.Toplevel(self)
        checkout_win.title("Finalizar Compra - Pagamento")
        checkout_win.geometry("400x450")
        
        ttk.Label(checkout_win, text="Forma de Pagamento", font=('Arial', 11, 'bold')).pack(pady=10)
        
        self.metodo_pagamento = tk.StringVar(value="pix")
        
        frame_opts = ttk.Frame(checkout_win)
        frame_opts.pack(pady=5, padx=20, fill='x')
        
        ttk.Radiobutton(frame_opts, text="PIX", variable=self.metodo_pagamento, value="pix", command=lambda: self.toggle_opcoes_pagamento(frame_detalhes)).pack(anchor='w')
        ttk.Radiobutton(frame_opts, text="Cartão de Crédito", variable=self.metodo_pagamento, value="credito", command=lambda: self.toggle_opcoes_pagamento(frame_detalhes)).pack(anchor='w')
        ttk.Radiobutton(frame_opts, text="Cartão de Débito", variable=self.metodo_pagamento, value="debito", command=lambda: self.toggle_opcoes_pagamento(frame_detalhes)).pack(anchor='w')
        
        frame_detalhes = ttk.LabelFrame(checkout_win, text="Detalhes do Pagamento", padding=10)
        frame_detalhes.pack(pady=10, padx=20, fill='x')
        
        self.frame_conteudo_dinamico = ttk.Frame(frame_detalhes)
        self.frame_conteudo_dinamico.pack(fill='both', expand=True)
        
        self.toggle_opcoes_pagamento(frame_detalhes)
        
        ttk.Button(checkout_win, text="Confirmar Pagamento", command=lambda: self.confirmar_compra(checkout_win)).pack(pady=20)

    def toggle_opcoes_pagamento(self, parent_frame):
        # Atualiza dinamicamente os campos de detalhe conforme a forma de pagamento
        for widget in self.frame_conteudo_dinamico.winfo_children():
            widget.destroy()
            
        metodo = self.metodo_pagamento.get()
        
        if metodo == "pix":
            ttk.Label(self.frame_conteudo_dinamico, text="Tipo de Chave:").pack(anchor='w')
            self.pix_tipo = tk.StringVar(value="qr_code")
            ttk.Radiobutton(self.frame_conteudo_dinamico, text="QR Code", variable=self.pix_tipo, value="qr_code").pack(anchor='w')
            ttk.Radiobutton(self.frame_conteudo_dinamico, text="Copia e Cola", variable=self.pix_tipo, value="copia_cola").pack(anchor='w')
            
        elif metodo == "credito":
            ttk.Label(self.frame_conteudo_dinamico, text="Número de Parcelas:").pack(anchor='w')
            self.parcelas_var = tk.StringVar(value="1")
            spin = ttk.Spinbox(self.frame_conteudo_dinamico, from_=1, to=12, textvariable=self.parcelas_var, width=5)
            spin.pack(anchor='w', pady=5)
            
        elif metodo == "debito":
            ttk.Label(self.frame_conteudo_dinamico, text="Pagamento à vista via Débito.").pack(anchor='w')

    def confirmar_compra(self, window):
        # Instancia a classe de pagamento correta e processa a transação
        metodo = self.metodo_pagamento.get()
        total = self.carrinho.valor_total
        pagamento_obj = None
        
        if metodo == "pix":
            pagamento_obj = PagamentoPix(total, self.pix_tipo.get())
        elif metodo == "credito":
            try:
                p = int(self.parcelas_var.get())
                pagamento_obj = PagamentoCredito(total, p)
            except ValueError:
                messagebox.showerror("Erro", "Parcelas inválidas")
                return
        elif metodo == "debito":
            pagamento_obj = PagamentoDebito(total)
            
        resultado = self.carrinho.processar_compra(pagamento_obj, self.loja)
        
        if resultado['sucesso']:
            messagebox.showinfo("Compra Aprovada", "Transação realizada com sucesso!")
            
            nf_win = tk.Toplevel(self)
            nf_win.title("Nota Fiscal")
            nf_win.geometry("400x500")
            
            txt = tk.Text(nf_win, wrap='word', font=('Consolas', 10))
            txt.pack(fill='both', expand=True, padx=10, pady=10)
            txt.insert('1.0', resultado['nota_fiscal'])
            txt.config(state='disabled')
            
            self.atualizar_tabela_produtos()
            self.atualizar_lista_carrinho()
            window.destroy()
        else:
            messagebox.showwarning("Atenção", resultado['nota_fiscal'])

if __name__ == "__main__":
    app = LojaApp()
    app.mainloop()