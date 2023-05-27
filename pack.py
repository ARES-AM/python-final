import gtts
import os
import playsound
names=['elina','alina','doremon']
for name in names:
    speech=gtts.gTTS(f"shoutout to {name}",lang='en')
    file='shit.mp3'
    speech.save(file)
    # os.system(f"start {file}")
    # os.system("mpg321 shit.mp3")
    playsound.playsound(file)
for i in range(len(names)):
    speech=gtts.gTTS(f"shoutout to {names[i]}",lang='en')
    file='shit.mp3'
    speech.save(file)
    # os.system(f"start {file}")
    # os.system("mpg321 shit.mp3")
    playsound.playsound(file)