import numpy as np

class ConceptExtractor:
    def __init__(self):
        self.conceitos = {}
    
    def extrair_por_contraste(self, ativ_pos: np.ndarray, ativ_neg: np.ndarray, nome: str) -> np.ndarray:
        vetor = (ativ_pos - ativ_neg).flatten()
        vetor = vetor / (np.linalg.norm(vetor) + 1e-6)
        self.conceitos[nome] = vetor
        return vetor
    
    def aplicar(self, ativacao: np.ndarray, conceito: str, direcao: float = 1.0) -> np.ndarray:
        vetor = self.conceitos[conceito]
        projecao = np.dot(ativacao.flatten(), vetor)
        return ativacao + direcao * projecao * vetor.reshape(ativacao.shape)

if __name__ == "__main__":
    ce = ConceptExtractor()
    print("✅ ConceptExtractor pronto")
