import random

class SyntheticOracle:
    def __init__(self):
        self.precos = {}
    
    def obter_preco(self, ativo: str) -> float:
        return random.uniform(100, 1000)  # placeholder

if __name__ == "__main__":
    so = SyntheticOracle()
    print("✅ SyntheticOracle pronto")
