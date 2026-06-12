import hashlib
from collections import defaultdict

class KompromatGraph:
    def __init__(self):
        self.entidades = {}
        self.conexoes = defaultdict(list)
    
    def _hash(self, nome: str) -> str:
        return hashlib.md5(nome.lower().encode()).hexdigest()[:16]
    
    def adicionar_conexao(self, origem: str, destino: str, tipo: str, peso: float = 1.0):
        oid, did = self._hash(origem), self._hash(destino)
        self.conexoes[oid].append((did, tipo, peso))
        self.conexoes[did].append((oid, tipo, peso))

if __name__ == "__main__":
    kg = KompromatGraph()
    print("✅ KompromatGraph pronto")
