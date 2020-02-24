import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
import utils  # Our own utility functions 
from blinkFilter import filt
from scipy import signal
import pyautogui # for spacebar

from fakeCollectedData import collectedData


# matchFilt = signal.hilbert(filt)

# matches = signal.correlate(matchFilt, collectedData)

# matchesAbs = np.abs(matches[:])

# maxMatch = np.max(matchesAbs)/1e5
# print(maxMatch)

# if maxMatch > 4.5:
#     print('blink') 

timeAboveThreshold = 0
threshold = 3.5
numBlinks = 0

for element in collectedData:
    if (element > threshold):
        timeAboveThreshold += 1
    if (timeAboveThreshold > 5):
        numBlinks += 1
        timeAboveThreshold = 0
print("finished")
print(numBlinks)