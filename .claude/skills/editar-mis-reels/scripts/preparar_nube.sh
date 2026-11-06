#!/usr/bin/env bash
# Prepara una sesión de Claude Code en la nube: compila whisper.cpp y baja el modelo si faltan.
# Uso: bash scripts/preparar_nube.sh   (idempotente: si ya está todo, no hace nada)
set -e
if ! command -v whisper-cli >/dev/null; then
  [ -d ~/whisper.cpp ] || git clone --depth 1 https://github.com/ggml-org/whisper.cpp ~/whisper.cpp
  cmake -S ~/whisper.cpp -B ~/whisper.cpp/build -DCMAKE_BUILD_TYPE=Release -DWHISPER_BUILD_TESTS=OFF >/dev/null
  cmake --build ~/whisper.cpp/build -j"$(nproc)" --target whisper-cli >/dev/null
  ln -sf ~/whisper.cpp/build/bin/whisper-cli /usr/local/bin/whisper-cli
fi
M=~/whisper-modelos/ggml-large-v3-turbo.bin
if [ ! -s "$M" ]; then
  mkdir -p ~/whisper-modelos
  curl -sSL --retry 3 -o "$M" https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin
fi
python3 "$(dirname "$0")/revisar_entorno.py"
