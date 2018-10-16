import os
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np

def spectrogram(filename):

    sample_rate, samples = wavfile.read(filename)
    np.set_printoptions(threshold=np.inf)
    # print(samples)
    upper = np.mean(samples) + np.std(samples)
    lower = np.mean(samples) - np.std(samples)
    samples = np.clip(samples, lower, upper)
    # def butter_lowpass(cutoff, fs, order=5):
    #     nyq = 0.5 * fs
    #     normal_cutoff = cutoff / nyq
    #     b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    #     return b, a
    #
    # def butter_lowpass_filter(data, cutoff, fs, order=5):
    #     b, a = butter_lowpass(cutoff, fs, order=order)
    #     y = signal.lfilter(b, a, data)
    #     return y


    # Filter requirements.
    # order = 6
    # fs = 30.0       # sample rate, Hz
    # cutoff = 3.667  # desired cutoff frequency of the filter, Hz

    # Get the filter coefficients so we can check its frequency response.
    # b, a = butter_lowpass(cutoff, fs, order)
    # y = butter_lowpass_filter(samples, cutoff, fs, order)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
    # print(np.mean(frequencies))
    for i in range(len(frequencies)):
        if frequencies[i] > np.mean(frequencies):
            frequencies[i] = 0
    # print(frequencies)
    # spectrogram = spectrogram * 100000
    fig = plt.figure(figsize=(3.60, 3.60), dpi=100)
    ax = fig.add_subplot(1,1,1)
    plt.axis('off')
    plt.pcolormesh(times, frequencies, spectrogram)
    plt.imshow(spectrogram)
    # plt.ylabel('Frequency [Hz]')
    # plt.xlabel('Time [sec]')
    plt.ylim(30, 0)
    path="spectrogram/"+filename[6:-4]+".png"
    print(path)
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    plt.savefig(path,dpi=100,bbox_inches=extent,pad_inches=0)


directory = 'train'

for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        path = directory+"/"+filename
        spectrogram(path)
    else:
        pass
