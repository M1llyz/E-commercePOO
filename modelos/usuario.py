#feito

# Classe Base para Vendedor e Cliente: Centraliza atributos e comportamentos comuns (Herança).

class Usuario:
    # Classe base para Cliente e Vendedor.
    
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self._senha = senha # Atributo protegido
        
    def autenticar(self, senha_digitada: str) -> bool:
        # Verifica se a senha digitada corresponde à senha do usuário.
        return self._senha == senha_digitada