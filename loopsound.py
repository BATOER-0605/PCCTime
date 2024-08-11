import playsound

#音声ファイル保存場所
dir = "sounds/"

#BGM再生
for i in range(2):
    playsound.playsound(f"{dir}loopsound.mp3")