import pyaudio
import wave
import sys
# def play_file(fname):
#     # create an audio object
#     wf = wave.open("/home/demihuman/Documents/project/Tabledrummer/samples/909_snr2.wav", 'rb')
#     p = pyaudio.PyAudio()
#     chunk = 1024
#
#     # open stream based on the wave object which has been input.
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                     channels=wf.getnchannels(),
#                     rate=wf.getframerate(),
#                     output=True)
#
#     # read data (based on the chunk size)
#     data = wf.readframes(chunk)
#
#     # play stream (looping from beginning of file to the end)
#     while data != '':
#         # writing to the stream is what *actually* plays the sound.
#         stream.write(data)
#         data = wf.readframes(chunk)

def play(s):
    CHUNK = 1024
    wf = wave.open(s, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)
    data = wf.readframes(CHUNK)

    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate


