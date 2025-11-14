# feito

# Classe Cliente: Herda a estrutura básica de Usuario para identficação do cliente na loja.

from .usuario import Usuario

class Cliente(Usuario):
    # Representa o cliente, herdando atributos de Usuario.
    
    def __init__(self, nome: str, email: str, senha: str = ""):
        # Chama o construtor da classe base (Usuario)
        super().__init__(nome, email, senha) 
        
    def exibir_boas_vindas(self):
        # Método de interface (CLI) que demonstra a instância.
        print(f"\nSeja bem-vindo(a), {self.nome}! Pronto(a) para comprar.")