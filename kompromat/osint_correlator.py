import re
import json

class OSINTCorrelator:
    def __init__(self):
        self.bases = {}
    
    def carregar_dados(self, fonte: str, dados: list):
        self.bases[fonte] = dados
    
    def extrair_entidades(self, texto: str) -> list:
        padrao = r"[A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+ (?:Ltd|Inc|S\.A\.)"
        return re.findall(padrao, texto)

if __name__ == "__main__":
    oc = OSINTCorrelator()
    print("✅ OSINTCorrelator pronto")
