# -*- coding: utf-8 -*-
import torch
from TTS.api import TTS
from pydub import AudioSegment

    return altered_sound.set_frame_rate(sound.frame_rate)
# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
# Print available TTS models

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

source = "sources/{file_name}"
inputs = [
    [1,'en', ""],
    [2,'ja', ""],
]

for input in inputs:
    tts.tts_to_file(text=input[2], speaker_wav=source, language=input[1], file_path=f"outputs/output_{input[0]}.wav")

final_audio = AudioSegment.silent()

for count in range(len(inputs)):

    count +=1
    cur_clip = AudioSegment.from_wav(f'outputs/output_{count}.wav')

    final_audio = final_audio + cur_clip  

final_audio.export(f'outputs/output_final.wav', format="wav")
