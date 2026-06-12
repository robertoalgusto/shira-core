import torch
import numpy as np

class WeightMutator:
    def __init__(self, taxa: float = 0.01):
        self.taxa = taxa
        self.historico = []
    
    def mutar(self, peso: torch.Tensor, feedback: float = 0.5) -> torch.Tensor:
        intensidade = self.taxa * (1 + feedback)
        if feedback > 0.7:
            ruido = torch.randn_like(peso) * intensidade
            return peso + ruido * torch.sigmoid(peso)
        elif feedback < 0.3:
            limiar = torch.quantile(peso.abs(), 0.3)
            return peso * (peso.abs() > limiar)
        else:
            ruido = torch.randn_like(peso) * (intensidade / 2)
            return peso + ruido

if __name__ == "__main__":
    wm = WeightMutator()
    print("✅ WeightMutator pronto")
