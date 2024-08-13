#pip install gtts


from gtts import gTTS

texto = "wújí"
lingua = "zh"
tts = gTTS(texto, lang=lingua)
tts.save("wuji.mp3")