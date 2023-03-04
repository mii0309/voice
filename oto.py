import matplotlib.pyplot as plt     #合成波の確認　
import pygame       #音の再生
import numpy as np      #合成派の作成

#モジュール初期化
pygame.mixer.init(frequency=44100, size=-16, channels=1)

#再生時間を指定
time=2

#周波数を指定
Hz1=2500

#再生時間を設定/グラフ化
arr_size = 44100*time*2
x=np.linspace(0,arr_size,arr_size)
y=np.sin(2*np.pi*Hz1/44100*x)*10000
y=y.astype(np.int16)
xtime=x/44100
plt.plot(xtime,y)
plt.xlim(0,0.002)
sound_arr = y.reshape(int(y.shape[0]/2), 2)
plt.show()
#音を再生
sound = pygame.sndarray.make_sound(sound_arr)
sound.play()