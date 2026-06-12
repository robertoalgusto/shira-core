import hashlib
from typing import List, Dict

class P2PSyncer:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.shards = {}
    
    def fragmentar(self, dados: bytes, num: int = 10) -> List[Dict]:
        size = len(dados) // num
        shards = []
        for i in range(num):
            start, end = i * size, (i + 1) * size if i < num - 1 else len(dados)
            shard_data = dados[start:end]
            shards.append({"id": f"{self.node_id}_shard_{i}", "hash": hashlib.sha3_256(shard_data).hexdigest(), "dados": shard_data})
        return shards

if __name__ == "__main__":
    ps = P2PSyncer("node_main")
    print("✅ P2PSyncer pronto")
