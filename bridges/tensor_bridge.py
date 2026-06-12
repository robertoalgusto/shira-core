import torch

class TensorBridge:
    def __init__(self):
        self.mapeamentos = {}
    
    def aprender(self, X: torch.Tensor, Y: torch.Tensor, nome: str = "bridge") -> torch.Tensor:
        X_flat = X.view(-1, X.shape[-1]).float()
        Y_flat = Y.view(-1, Y.shape[-1]).float()
        W = torch.linalg.pinv(X_flat) @ Y_flat
        self.mapeamentos[nome] = {"W": W, "shape_out": Y.shape}
        return W
    
    def aplicar(self, X: torch.Tensor, nome: str) -> torch.Tensor:
        W = self.mapeamentos[nome]["W"]
        return (X.view(-1, X.shape[-1]).float() @ W).view(self.mapeamentos[nome]["shape_out"])

if __name__ == "__main__":
    tb = TensorBridge()
    print("✅ TensorBridge pronto")
