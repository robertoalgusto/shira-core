import random
import numpy as np
from typing import List, Tuple

class GhostRouter:
    def __init__(self, num_nos: int = 10):
        self.num_nos = num_nos
        self.nos = [f"node_{i}" for i in range(num_nos)]
    
    def fragmentar_valor(self, valor_total: float) -> List[float]:
        num = max(5, min(20, int(valor_total / 50)))
        fragmentos = []
        restante = valor_total
        for i in range(num - 1):
            proporcao = np.random.pareto(1.5) / 10
            frag = min(restante * proporcao, restante / 2)
            fragmentos.append(round(frag, 2))
            restante -= frag
        fragmentos.append(round(restante, 2))
        random.shuffle(fragmentos)
        return fragmentos
    
    def distribuir(self, fragmentos: List[float]) -> List[Tuple[str, float]]:
        nos_escolhidos = random.choices(self.nos, k=len(fragmentos))
        return list(zip(nos_escolhidos, fragmentos))

if __name__ == "__main__":
    gr = GhostRouter()
    frag = gr.fragmentar_valor(1050.00)
    print(f"✅ GhostRouter: {len(frag)} fragmentos")
