#feito

# Classes de Pagamento: Implementam o Polimorfismo através de uma classe abstrata.

from abc import ABC, abstractmethod

class Pagamento(ABC):
    # Classe Abstrata/Interface para Polimorfismo.
    
    def __init__(self, valor: float):
        self.valor = valor
        
    @abstractmethod
    def processar(self) -> str:
        # Método polimórfico: cada forma de pagamento implementa sua lógica.
        pass

class PagamentoPix(Pagamento):
    def processar(self) -> str:
        # Simula a lógica de pagamento via PIX.
        return "PIX"

class PagamentoDebito(Pagamento):
    def processar(self) -> str:
        # Simula a lógica de pagamento via Débito.
        return "Débito"
        
class PagamentoCredito(Pagamento):
    def processar(self) -> str:
        # Simula a lógica de pagamento via Crédito.
        return "Crédito"