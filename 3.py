import os
from scipy.io.wavfile import read
from scipy.fftpack import fft
import math
import numpy as np
import matplotlib.pyplot as plt

fs_1, S_1 = read("data/point_one_480.wav")     # The signal from point 1 is loaded
fs_2, S_2 = read("data/point_two_440_620.wav") # The signal from point 2 is loaded

# ================================================================================
# ------------------ Apply the fast Fourier transform to S_1 ---------------------
# ================================================================================
X_1 = fft(S_1)                    # Fourier transform is calculated
absS_1 = np.abs(X_1)/(X_1.size)   # The magnitude of X_1 is calculated
pX_1 = np.unwrap(np.angle(X_1))   # The angle is adjusted between 0 and 2π

# -------------------------- Frequency 1 is created ------------------------------
Frecuencia_1 = np.linspace(-fs_1/2, fs_1/2, absS_1.size)

# ------------------- Negative frequency is adjusted to the left ----------------- 
hN=int(math.floor((X_1.size+1)/2))
absS_1=np.hstack((absS_1[hN:],absS_1[:hN]))# The magnitudes come together
pX_1=np.hstack((pX_1[hN:],pX_1[:hN]))      # The phases come together

# ================================================================================
# ---------------- Apply the fast Fourier transform to S_1 -----------------------
# ================================================================================
X_2 = fft(S_2)                    # Fourier transform is calculated
absS_2 = np.abs(X_2)/(X_2.size)   # The magnitude of X_1 is calculated
pX_2 = np.unwrap(np.angle(X_2))   # The angle is adjusted between 0 and 2π
                      
# -------------------------- Frequency 2 is created ------------------------------
Frecuencia_2 = np.linspace(-fs_2/2, fs_2/2, absS_2.size)

# ------------------- Negative frequency is adjusted to the left -----------------
hN=int(math.floor((X_2.size+1)/2))
absS_2=np.hstack((absS_2[hN:],absS_2[:hN]))# The magnitudes come together
pX_2=np.hstack((pX_2[hN:],pX_2[:hN]))      # The phases come together

# Create 'data' folder if it does not exist
if not os.path.exists('data'):
    os.makedirs('data')

# ================================================================================
# ---------------------------------- It is graphed -------------------------------
# ================================================================================
Fig, Ax = plt.subplots(2, 1, sharex=True)
Ax[0].plot(Frecuencia_1, absS_1)  # S_1 is graphed
Ax[1].plot(Frecuencia_2, absS_2)  # S_2 is graphed
Ax[0].set_title("Graph of S_1") 
Ax[1].set_title("Graph of S_2") 
Ax[1].set_xlabel("Frecuency")    
Ax[0].set_ylabel("Magnitude")      
Ax[1].set_ylabel("Magnitude")      

image_filename = os.path.join('data', 'Image.png')
plt.savefig(image_filename)  # Save the plot as a PNG image

plt.show()