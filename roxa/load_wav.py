from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import IPython.display
import librosa
import librosa.display

audio_path = ../../espnet/egs/yesno/asr1/waves_yesno/0_0_0_0_1_1_1_1.wav
y, sr = librosa.load(audio_path)
