# @Author: nilanjan
# @Date:   2018-11-20T19:23:59+05:30
# @Email:  nilanjandaw@gmail.com
# @Filename: file_conversion.py
# @Last modified by:   nilanjan
# @Last modified time: 2018-11-22T16:12:44+05:30
# @Copyright: Nilanjan Daw



import os
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np

def spectrogram(filename,dLength):

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
    # spectrogram = spectrogram * 100000modelsmodelsmodelsmmodelsodels
    fig = plt.figure(figsize=(3.60, 3.60), dpi=100)
    ax = fig.add_subplot(1,1,1)
    plt.axis('off')
    plt.pcolormesh(times, frequencies, spectrogram)
    plt.imshow(spectrogram)
    # plt.ylabel('Frequency [Hz]')
    # plt.xlabel('Time [sec]')
    plt.ylim(30, 0)
    path="validation/"+filename[dLength+1:-4]+".png"
    print("pathName ",path)
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    plt.savefig(path,dpi=100,bbox_inches=extent,pad_inches=0)
    plt.close('all')


directory = 'validation_raw'
dlength = len(directory)
for filename in os.listdir(directory):
    # print("filename"+str(filename))
    if filename.endswith(".wav"):
        # print("dir: "+str(directory))
        path = directory+"/"+filename
        # print("path "+str(path))
        spectrogram(path,dlength)
    else:
        pass
