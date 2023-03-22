import pyaudio
import numpy as np
from time import sleep

# サンプリングレートを定義 --- (*1)
RATE = 48000

# BPMや音長を定義 --- (*2)
BPM = 100
L1 = (60 / BPM)
#L2,L4,L8 = (L1/2,L1/4,L1/8)

# 周波数を定義 --- (*3)
f = 6000

# サイン波を生成 --- (*4)
def tone(freq, length, gain):
    slen = int(length * RATE)
    t = float(freq) * np.pi * 2 / RATE
    return np.sin(np.arange(slen) * t) * gain

# 再生 --- (*5)
def play_wave(stream, samples):
    stream.write(samples.astype(np.float32).tostring())


# 出力用のストリームを開く --- (*6)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=RATE,
                frames_per_buffer=1024,
                output=True)

# ドレミを再生 --- (*7)
replay=3
print("play")
for i in range(replay):
    play_wave(stream, tone(f, L1, 1.0)) 
    sleep(1)


stream.close()
