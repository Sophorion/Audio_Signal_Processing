import os
import numpy as np
from scipy.io.wavfile import write #Import libraries
import matplotlib.pyplot as plt
# ================================================================== #
fs = 16000
duration = 2 
Time = np.arange(0, duration, 1/fs)      # time vector
Frecuency_1 = 440                        # frecuency
Frecuency_2 = 620                        # angular frecuency

S_1 = 0.8*np.sin(2*np.pi*Frecuency_1*Time)
S_2 = 0.8*np.sin(2*np.pi*Frecuency_2*Time)

S_3 = S_1 + S_2                          # The two signals are added

# Create 'data' folder if it does not exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save the file in the 'data' folder
filename = os.path.join('data', 'point_two_440_620.wav')
write(filename, fs, S_3)                 # save

# Plot the tone signal
plt.title("Tone")
plt.ylabel("Amplitud")
plt.xlabel("Time")
plt.plot(Time, S_3)

image_filename = os.path.join('data', 'tone_S3.png')
plt.savefig(image_filename)  # Save the plot as a PNG image

plt.show()