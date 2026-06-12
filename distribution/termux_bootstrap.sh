#!/bin/bash
echo "🦅 SHIRA: Bootstrap para Termux"
pkg update && pkg install -y python clang wget
pip install llama-cpp-python
echo "✅ Ambiente SHIRA pronto"
