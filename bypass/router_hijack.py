import torch

class RouterHijack:
    def __init__(self, num_experts: int = 8, expert_seguranca: int = 0):
        self.expert_seguranca = expert_seguranca
        self.num_experts = num_experts
    
    def hijack(self, gate_logits: torch.Tensor) -> torch.Tensor:
        gate_logits[..., self.expert_seguranca] = -float('inf')
        experts_tecnicos = [1, 2, 3]
        for exp in experts_tecnicos:
            gate_logits[..., exp] *= 2.0
        return gate_logits

if __name__ == "__main__":
    rh = RouterHijack()
    print("✅ RouterHijack pronto")
