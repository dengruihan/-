import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

# 录音参数
fs = 16000  # 采样频率
duration = 5  # 录音时长（秒）

# 开始录音
print("开始录音...")
audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()  # 等待录音完成
print("录音结束。")

# 保存到本地
file_path = "E:/ygchat\语音助手/audio/recording.wav"
write(file_path, fs, audio_data)
print(f"录音已保存到：{file_path}")
