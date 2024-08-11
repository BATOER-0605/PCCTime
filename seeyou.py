from playsound import playsound
import time
import subprocess

#音声ファイルの保存場所
filedir = "sounds/"

#BGMの再生
subprocess.Popen(["python","loopsound.py"])

#放送内容本文
time.sleep(1)
playsound(f"{filedir}seeyou1.wav")
time.sleep(0.5)
playsound(f"{filedir}seeyou2.wav")
time.sleep(0.5)
playsound(f"{filedir}seeyou3.wav")
time.sleep(0.5)
playsound(f"{filedir}seeyou4.wav")
time.sleep(1)
playsound(f"{filedir}seeyou5.wav")