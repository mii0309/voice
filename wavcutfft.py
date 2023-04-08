import soundfile as sf                      
import numpy as np                          
from matplotlib import pyplot as plt       
N=48000
a=395000

path1 = 'i1000.wav'                      
data1, samplerate = sf.read(path1) 
print(data1[:,1].shape)
result1= data1[a:a+65536,1]
t1 = np.arange(0, len(result1)) / samplerate    # グラフ表示のための横軸を設定

dt = 1/samplerate              #dt:時間刻み幅

result1_fft = np.fft.fft(result1) # 離散フーリエ変換
freq1 = np.fft.fftfreq(N, d=dt) # 周波数を割り当てる
Amp1 = abs(result1_fft/(N/2)) # 音の大きさ（振幅の大きさ）

fig = plt.figure(figsize = (14,7), facecolor='lightblue')
# グラフ表示
ax1 = fig.add_subplot(2, 1,1)
ax2 = fig.add_subplot(2, 1,2)

ax1.set_title(path1)
ax2.set_title('cut')
#ax1.set_xlim(0,14000)
#ax1.set_ylim(0,3*1e-5)

#各subplot領域にデータを渡す
ax1.plot(freq1[1:int(N/2)], Amp1[1:int(N/2)])
ax2.plot(t1, result1)

plt.show()
plt.close()