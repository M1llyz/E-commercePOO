# Classe Cliente: Representa o consumidor da loja. Herda atributos e métodos da classe base Usuario.

from usuario import Usuario

class Cliente(Usuario):
    
    def __init__(self, nome: str, email: str, senha: str = ""):
        # Inicializa o cliente chamando o construtor da classe pai (Usuario)
        super().__init__(nome, email, senha) 
        
    def get_mensagem_boas_vindas(self) -> str:
        # Retorna a mensagem de boas-vindas para ser exibida na interface
        return f"Seja bem-vindo(a), {self.nome}! Pronto(a) para comprar."