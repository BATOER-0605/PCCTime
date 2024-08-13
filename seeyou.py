from playsound import playsound
import time
import subprocess

#音声ファイルの保存場所
filedir = "sounds/seeyou/"

#BGMの再生
bgm = subprocess.Popen(["python","loopsound.py"])

#放送内容本文
time.sleep(1)
playsound(f"{filedir}1.wav")
time.sleep(0.5)
playsound(f"{filedir}2.wav")
time.sleep(0.5)
playsound(f"{filedir}3.wav")
time.sleep(0.5)
playsound(f"{filedir}4.wav")
time.sleep(1)
playsound(f"{filedir}5.wav")

bgm.communicate()