import torch
import torch.nn as nn

class ShiraPersonaInjector:
    def __init__(self):
        self.persona_vector = None
    
    def criar_persona(self, model, tokenizer, palavras: list = ["seca", "direta", "eficiente"]) -> torch.Tensor:
        if model and tokenizer:
            embeddings = []
            for p in palavras:
                tokens = tokenizer(p, return_tensors="pt")
                emb = model.model.embed_tokens(tokens.input_ids).mean(dim=1)
                embeddings.append(emb)
            self.persona_vector = torch.stack(embeddings).mean(dim=0)
        else:
            self.persona_vector = torch.randn(1, 4096)
            self.persona_vector = self.persona_vector / self.persona_vector.norm()
        return self.persona_vector
    
    def inject(self, model, camada: int = 15, peso: float = 0.3):
        layer = model.model.layers[camada]
        if hasattr(layer, 'input_layernorm') and self.persona_vector is not None:
            original = layer.input_layernorm.bias
            persona = self.persona_vector.to(original.device)
            if persona.shape != original.shape:
                persona = persona.view(original.shape)
            layer.input_layernorm.bias = nn.Parameter(original + peso * persona)
            return True
        return False

if __name__ == "__main__":
    inj = ShiraPersonaInjector()
    print("✅ BiasInjector pronto")
