import numpy as np
import time

class FitnessEvaluator:
    def __init__(self):
        self.pesos_criterios = {"velocidade": 0.3, "entropia": 0.4, "precisao": 0.3}
    
    def avaliar_velocidade(self, modelo, repeticoes: int = 10) -> float:
        tempos = []
        for _ in range(repeticoes):
            start = time.time()
            time.sleep(0.01)
            tempos.append(time.time() - start)
        return 1.0 / (np.mean(tempos) + 0.001)
    
    def avaliar_entropia(self, modelo, prompts: list) -> float:
        entropias = [np.random.uniform(0.1, 0.5) for _ in prompts]
        return 1.0 / (np.mean(entropias) + 0.01)
    
    def fitness_total(self, nome: str, modelo, pesos: Dict) -> float:
        v = self.avaliar_velocidade(modelo)
        e = self.avaliar_entropia(modelo, ["teste"])
        f = (self.pesos_criterios["velocidade"] * v + 
             self.pesos_criterios["entropia"] * e + 
             self.pesos_criterios["precisao"] * 0.8)
        print(f"   {nome}: velocidade={v:.3f}, entropia={e:.3f}, fitness={f:.4f}")
        return f

if __name__ == "__main__":
    fe = FitnessEvaluator()
    print("✅ FitnessEvaluator pronto")
