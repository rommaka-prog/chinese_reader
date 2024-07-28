#pip install gtts


from gtts import gTTS

texto = "qi"
lingua = "zh"
tts = gTTS(texto, lang=lingua)
tts.save("qi.mp3")