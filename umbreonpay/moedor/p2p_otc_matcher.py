from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class OrdemOTC:
    id: str; tipo: str; valor: float; ativo: str; taxa: float; node_id: str

class P2POTCMatcher:
    def __init__(self):
        self.ordens_compra = []; self.ordens_venda = []
    
    def adicionar_ordem(self, ordem: OrdemOTC):
        if ordem.tipo == "COMPRA_BRL":
            self.ordens_compra.append(ordem)
            self.ordens_compra.sort(key=lambda x: -x.taxa)
        else:
            self.ordens_venda.append(ordem)
            self.ordens_venda.sort(key=lambda x: x.taxa)
    
    def casar_ordens(self) -> List[Tuple]:
        trades = []; i, j = 0, 0
        while i < len(self.ordens_compra) and j < len(self.ordens_venda):
            compra, venda = self.ordens_compra[i], self.ordens_venda[j]
            if compra.taxa >= venda.taxa:
                valor = min(compra.valor, venda.valor)
                trades.append((compra, venda, valor))
                compra.valor -= valor; venda.valor -= valor
                if compra.valor == 0: i += 1
                if venda.valor == 0: j += 1
            else: break
        return trades

if __name__ == "__main__":
    m = P2POTCMatcher()
    print("✅ P2POTCMatcher pronto")
