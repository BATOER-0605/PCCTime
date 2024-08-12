from playsound import playsound
import time

#音声ファイルの保存場所
filedir = "sounds/5min/"

#チャイム再生
playsound(f"{filedir}chime.mp3")

#放送内容本文
playsound(f"{filedir}1.wav")
time.sleep(0.5)
playsound(f"{filedir}2.wav")
time.sleep(0.5)
playsound(f"{filedir}3.wav")
time.sleep(0.5)
playsound(f"{filedir}4.wav")
time.sleep(0.5)
playsound(f"{filedir}5.wav")