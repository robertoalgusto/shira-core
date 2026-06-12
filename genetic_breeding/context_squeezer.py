import torch
import torch.nn as nn
import torch.nn.functional as F

class ContextSqueezer(nn.Module):
    def __init__(self, dim_embedding: int = 4096, dim_estado: int = 512):
        super().__init__()
        self.projetor = nn.Parameter(torch.randn(dim_embedding, dim_estado) / dim_embedding**0.5, requires_grad=False)
        self.decodificador = nn.Parameter(torch.randn(dim_estado, dim_embedding) / dim_estado**0.5, requires_grad=False)
    
    def squeeze(self, sequencia: torch.Tensor) -> torch.Tensor:
        pesos = F.softmax(torch.arange(sequencia.shape[1]), dim=0).to(sequencia.device)
        media_ponderada = (sequencia * pesos.unsqueeze(-1)).sum(dim=1)
        return media_ponderada @ self.projetor
    
    def unsqueeze(self, estado: torch.Tensor) -> torch.Tensor:
        return estado @ self.decodificador

if __name__ == "__main__":
    cs = ContextSqueezer()
    print("✅ ContextSqueezer pronto (compressão 4096→512, 87.5%)")
