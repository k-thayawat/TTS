# -*- coding: utf-8 -*-
import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
# Print available TTS models

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

tts.tts_to_file(text="夢ならばどれほどよかったでしょう、未だにあなたのことを夢にみる、忘れた物を取りに帰るように、古びた思い出の埃を払う、戻らない幸せがあることを最後にあなたが教えてくれた、言えずに隠してた昏い過去も、あなたがいなきゃ永遠に昏いまま", speaker_wav="sources/ahri_1m.mp3", language="ja", file_path="outputs/output.wav")
