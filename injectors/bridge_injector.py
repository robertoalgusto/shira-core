import torch

class BridgeInjector:
    def __init__(self):
        self.bridges = {}
    
    def aprender(self, ativ_origem: torch.Tensor, ativ_destino: torch.Tensor, nome: str = "bridge"):
        X = ativ_origem.view(-1, ativ_origem.shape[-1]).cpu().float()
        Y = ativ_destino.view(-1, ativ_destino.shape[-1]).cpu().float()
        W = torch.linalg.pinv(X) @ Y.T
        self.bridges[nome] = {"W": W, "shape": ativ_destino.shape}
        return W

if __name__ == "__main__":
    bi = BridgeInjector()
    print("✅ BridgeInjector pronto")
