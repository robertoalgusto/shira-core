import torch
import numpy as np
from typing import Dict, List

class TensorBreeder:
    def __init__(self):
        self.geracao = 0
        self.linhagens = {}
    
    def slerp(self, tensor_a: torch.Tensor, tensor_b: torch.Tensor, t: float = 0.5) -> torch.Tensor:
        a_norm = tensor_a / tensor_a.norm()
        b_norm = tensor_b / tensor_b.norm()
        omega = torch.acos(torch.clamp(torch.dot(a_norm.flatten(), b_norm.flatten()), -1, 1))
        if omega < 1e-6:
            return tensor_a
        sin_omega = torch.sin(omega)
        weight_a = torch.sin((1 - t) * omega) / sin_omega
        weight_b = torch.sin(t * omega) / sin_omega
        return (weight_a * tensor_a + weight_b * tensor_b)
    
    def cruzar_camadas(self, pai: Dict, mae: Dict, taxa_mutacao: float = 0.05) -> Dict:
        filho = {}
        for nome, tensor_pai in pai.items():
            tensor_mae = mae.get(nome)
            if tensor_mae is None:
                filho[nome] = tensor_pai.clone()
            elif "attention" in nome.lower():
                filho[nome] = tensor_pai.clone()
            elif "mlp" in nome.lower() or "ffn" in nome.lower():
                filho[nome] = tensor_mae.clone()
            else:
                filho[nome] = self.slerp(tensor_pai, tensor_mae, t=0.5)
            if np.random.random() < taxa_mutacao:
                filho[nome] += torch.randn_like(filho[nome]) * 0.01
        return filho

if __name__ == "__main__":
    breeder = TensorBreeder()
    print("✅ TensorBreeder pronto")
