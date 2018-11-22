# @Author: nilanjan
# @Date:   2018-11-20T19:34:48+05:30
# @Email:  nilanjandaw@gmail.com
# @Filename: spectronet.py
# @Last modified by:   nilanjan
# @Last modified time: 2018-11-22T15:17:20+05:30
# @Copyright: Nilanjan Daw
from keras import layers, models
from keras import optimizers
import csv


def defineModel():
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu',
                            input_shape=(240, 360, 3)))
    model.add(layers.MaxPool2D(2, 2))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D(2, 2))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D(2, 2))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D(2, 2))
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.1))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    print(model.summary())

    model.compile(loss='binary_crossentropy',
                  optimizer=optimizers.RMSprop(lr=0.04), metrics=['acc'])
    return model


model = defineModel()
