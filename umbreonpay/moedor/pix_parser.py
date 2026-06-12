import re

class PixParser:
    def __init__(self):
        self.padroes = {"txid": r"txid[:\s]*([a-f0-9]{32})", "valor": r"R?\$\s*([\d.,]+)"}
    
    def extrair_dados(self, texto: str) -> dict:
        dados = {}
        for campo, padrao in self.padroes.items():
            match = re.search(padrao, texto, re.IGNORECASE)
            if match:
                dados[campo] = next((g for g in match.groups() if g), None)
        return dados

if __name__ == "__main__":
    p = PixParser()
    print("✅ PixParser pronto")
