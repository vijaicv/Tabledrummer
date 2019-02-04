import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import wave


def wavread(filename):
    wavefile = wave.open(filename, 'r')
    signal = wavefile.readframes(-1)
    signal = np.fromstring(signal, 'Int16')
    return signal


def graphplot(root):
    soundwave = wavread('samples/bass1.wav')
    f = Figure(figsize=(8, 5))
    a = f.add_subplot(111)
    a.plot(soundwave)
    canvas = FigureCanvasTkAgg(f, root)
    return canvas














