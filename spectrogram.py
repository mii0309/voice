import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf

#.wavからデータの作成
wav_name = "n10000.wav"
x, fs = sf.read(wav_name)

#スペクトログラム分析の実施
f, t, Sxx = signal.spectrogram(x, fs)

#図の描画
plt.title(wav_name)
plt.pcolormesh(t, f, 10 * np.log(Sxx))  #intensityを修正
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
cbar = plt.colorbar()  #カラーバー表示のため追加
cbar.ax.set_ylabel("Intensity [dB]")  #カラーバーの名称表示のため追加
plt.show()
