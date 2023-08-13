import gtts
import playsound
text = input("Enter Your Text : ")
sound = gtts.gTTS(text, lang = "hi")
sound.save("TextSound.mp3")
playsound.playsound("TextSound.mp3")