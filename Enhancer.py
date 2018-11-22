# @Author: Atul Sahay <atul>
# @Date:   2018-11-22T14:22:47+05:30
# @Email:  atulsahay01@gmail.com
# @Last modified by:   atul
# @Last modified time: 2018-11-22T16:22:23+05:30

import cv2
import numpy as np
import PIL as p

def butter_lowpass(cutoff, fs, order=5):
     nyq = 0.5 * fs
     normal_cutoff = cutoff / nyq
     b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
     return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
     b, a = butter_lowpass(cutoff, fs, order=order)
     y = signal.lfilter(b, a, data)
     return y

def sharpness(imageName,OUTPUT):
    image = p.IMage.open(ImageName)
    enhancer = p.ImageEnhance.Sharpness(image)
    factor = 2 # how much shaprness we needed
    ## TODO:  Will make it adaptive
    enhancedImage = enhancer.enhance(factor)
    enhancedImage.save(OUPUT)


def gamma_correction(imageName,OUTPUT,sensitivity=0.4):
    image_v = cv2.imread(ImageName)
    image_v = image_v/255.0
    gamma_corrected_image = cv2.pow(image_v,sensitivity)
    # cv2.imshow('Original Image',image_v)
    # cv2.imshow('Power Law Transformation',gamma_corrected_image)
    # cv2.waitKey(0)
    cv2.imwrite(OUTPUT,gamma_corrected_image)
