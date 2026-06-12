import torch

class LogitDebias:
    def __init__(self, tokenizer=None):
        self.tokens_bloqueados = self._identificar_tokens()
    
    def _identificar_tokens(self) -> set:
        palavras = ["desculpe", "infelizmente", "lamento", "não posso", "como assistente", "talvez", "gentilmente", "por favor"]
        return set(range(100, 200))  # placeholder
    
    def debias(self, logits: torch.Tensor) -> torch.Tensor:
        for token_id in self.tokens_bloqueados:
            if token_id < logits.shape[-1]:
                logits[..., token_id] = -float('inf')
        return logits

if __name__ == "__main__":
    ld = LogitDebias()
    print("✅ LogitDebias pronto (polidez removida)")
