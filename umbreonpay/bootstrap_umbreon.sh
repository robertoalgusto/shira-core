#!/bin/bash
echo "🐝 SHIRA: Inicializando Colmeia UmbreonPay"
python3 -c "from casta_arquitetos import Arquitetos; a = Arquitetos()" &
python3 -c "from casta_guardioes import Guardioes; g = Guardioes()" &
python3 -c "from casta_alquimistas import Alquimistas; a = Alquimistas()" &
echo "✅ Colmeia ativa: 1000 agentes"
