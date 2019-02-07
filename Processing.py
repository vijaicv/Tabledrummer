import wave
import numpy as np



class processor:
    # TODO: remove this part and replace with realtime frames
    def wavread(self,filename):
        wavefile = wave.open(filename, 'r')
        signal = wavefile.readframes(-1)
        signal = np.fromstring(signal, 'Int16')
        return signal

    def correlate(self,s1, s2):
        s1 = s1[1:10000]
        s2 = s2[1:10000]
        corr_matt = np.corrcoef(s1, s2)
        corr_coef = corr_matt[0, 1]
        print(abs(corr_coef))













