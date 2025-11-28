# Classe Base: Centraliza atributos e comportamentos comuns (Herança) para Cliente e Vendedor.

class Usuario:
    
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self._senha = senha # Atributo protegido
        
    def autenticar(self, senha_digitada: str) -> bool:
        # Verifica se a senha digitada corresponde à senha do usuário (Retorna True se a senha estiver correta, False caso contrário).
        return self._senha == senha_digitada