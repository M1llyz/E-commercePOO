# Classes de Pagamento: Implementam o Polimorfismo através de uma classe abstrata com regras de negócio distintas.

from abc import ABC, abstractmethod
import random

class Pagamento(ABC):
    
    def __init__(self, valor: float):
        self.valor = valor
        
    @abstractmethod
    def processar(self) -> dict:
        # Método abstrato que deve ser implementado pelas classes filhas retornando um dicionário de dados
        pass

class PagamentoPix(Pagamento):
    
    def __init__(self, valor: float, tipo_chave: str):
        # Inicializa com o valor e o tipo de chave (qr_code ou copia_cola)
        super().__init__(valor)
        self.tipo_chave = tipo_chave
        
    def processar(self) -> dict:
        # Simula a geração de um código PIX e retorna status pendente
        codigo_aleatorio = f"00020126580014BR.GOV.BCB.PIX0136{random.randint(100000, 999999)}"
        
        detalhe = f"Chave ({self.tipo_chave}) gerada. Aguardando pagamento."
        
        if self.tipo_chave == "qr_code":
            # Simulação visual de um QR Code em texto
            detalhe = f"QR Code gerado: [QR_DATA:{codigo_aleatorio}]"
        else:
            detalhe = f"Código Copia e Cola: {codigo_aleatorio}"

        return {
            "forma": "PIX",
            "status": "PENDENTE",
            "detalhe": detalhe,
            "codigo_pix": codigo_aleatorio
        }

class PagamentoDebito(Pagamento):
    
    def processar(self) -> dict:
        # Simula uma transação de débito com aprovação imediata
        return {
            "forma": "Débito",
            "status": "APROVADO",
            "detalhe": "Transação de débito autorizada pelo banco.",
            "codigo_pix": None
        }
        
class PagamentoCredito(Pagamento):
    
    def __init__(self, valor: float, num_parcelas: int):
        # Inicializa com o valor e a quantidade de parcelas desejada
        super().__init__(valor)
        self.num_parcelas = num_parcelas
        
    def processar(self) -> dict:
        # Simula transação de crédito e calcula o valor das parcelas
        valor_parcela = self.valor / self.num_parcelas
        
        return {
            "forma": "Crédito",
            "status": "APROVADO",
            "detalhe": f"Compra parcelada em {self.num_parcelas}x.",
            "parcelas": self.num_parcelas,
            "valor_parcela": valor_parcela,
            "codigo_pix": None
        }