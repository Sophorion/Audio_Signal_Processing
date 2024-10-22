import os
import numpy as np
from scipy.io.wavfile import write #Import libraries
import matplotlib.pyplot as plt
# ==================================================== #
fs = 16000 
duration = 2 
time = np.arange(0, duration, 1/fs)     # time vector
F = 480                                 # frecuency
w = 2*np.pi*F                           # angular frecuency
tone = 0.8*np.cos(w*time)               # tone signal

# Create 'data' folder if it does not exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save the file in the 'data' folder
filename = os.path.join('data', 'point_one_480.wav')
write(filename, fs, tone)               # save

# Plot the tone signal
plt.title("Tone")
plt.plot(time, tone)   
plt.ylabel("Amplitud")
plt.xlabel("Time")

image_filename = os.path.join('data', 'tone.png')
plt.savefig(image_filename)  # Save the plot as a PNG image

plt.show()