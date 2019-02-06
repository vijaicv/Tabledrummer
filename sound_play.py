##import pyaudio
##import wave
##import sys
##CHUNK = 1024
##wf= wave.open("D:\jazz\snare",'rb')
##p= pyaudio.PyAudio()
##stream= p.open(format=p.get_format_from_width(wf.getsampwidth()),
##               channels=wf.getnchannels(),
##               rate=wf.getframerate(),
##               output=True)
##data=wf.readframes(CHUNK)
##
##while len(data)>0:
##    stream.write(data)
##    data=wf.readframes(CHUNK)
##
##stream.stop_stream()
##stream.close()
##
##p.terminate

def play(s):
    if(s=="snare"):
        print("snare")
    elif(s=="kick"):
        print("kick")
    elif(s=="hat"):
        print("haaat")


play("mat")
