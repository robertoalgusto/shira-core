from collections import deque
import numpy as np

class WhaleTracker:
    def __init__(self, janela: int = 100, limiar: float = 3.0):
        self.janela = janela
        self.limiar = limiar
        self.historico = deque(maxlen=janela)
        self.alertas = []
    
    def detectar_anomalia(self, valor: float) -> dict:
        if len(self.historico) < 10:
            self.historico.append(valor)
            return {"anomalia": False}
        valores = list(self.historico)
        media, desvio = np.mean(valores), np.std(valores)
        zscore = abs(valor - media) / (desvio + 1e-6)
        is_anomalia = zscore > self.limiar
        self.historico.append(valor)
        if is_anomalia:
            self.alertas.append({"valor": valor, "zscore": zscore})
        return {"anomalia": is_anomalia, "zscore": zscore}

if __name__ == "__main__":
    wt = WhaleTracker()
    print("✅ WhaleTracker pronto")
