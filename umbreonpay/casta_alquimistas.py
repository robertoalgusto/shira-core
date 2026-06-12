class Alquimistas:
    def __init__(self, n_agentes: int = 300):
        self.agentes = [f"alquimista_{i}" for i in range(n_agentes)]
        self.capital_gerado = 0.0
    
    def arbitrar(self, pool_a: float, pool_b: float) -> float:
        if abs(pool_a - pool_b) > 0.01:
            return (pool_b - pool_a) * 0.95
        return 0.0

if __name__ == "__main__":
    a = Alquimistas()
    print(f"✅ Casta Alquimistas: {len(a.agentes)} agentes")
