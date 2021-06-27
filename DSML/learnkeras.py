import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten
from keras.datasets import mnist
from keras.optimizers import SGD
from keras.utils.np_utils import to_categorical
from keras.preprocessing.image import load_img, img_to_array

from sklearn.model_selection import KFold
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

# https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-from-scratch-for-mnist-handwritten-digit-classification/

########################################################################
print("Load Dataset")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
num_classes = 10

def prepare_data():
    print("Prepare Data")
    global x_train, y_train, x_test, y_test 
    # Scale images to the [0, 1] range , just for fload to calculate
    x_train = x_train.astype("float32") / 255 
    x_test = x_test.astype("float32") / 255
    # Make sure images have shape (28, 28, 1)
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)
    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)


##### define model
def define_model():
    print("Define Model")
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(10, activation='softmax'))
    # compile model
    opt = SGD(learning_rate=0.01, momentum=0.9)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    return model

##### train model
def train_model(model, fileName):
    print("Train Model")
    global x_train, y_train
    x_val = x_train[300:,]
    y_val = y_train[300:,]
    history = model.fit(x_train, y_train, epochs=12, batch_size=32, validation_data=(x_val,y_val), verbose=0)
    plt.plot(history.history['accuracy'])
    #plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()
    model.save(fileName)

##### evaluate model
def evaluate_model():
    global x_test, y_test 
    model = load_model("testconvnet.h5")
    results = model.evaluate(x_test, y_test)
    for i in range(len(model.metrics_names)):
        print(model.metrics_names[i]," : ", results[i])
    
##### test model
def test_model():
    img = load_image("sample_image.png")
    model = load_model("testconvnet.h5")
    digit =model.predict_classes(img)
    print(digit[0])

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, color_mode = "grayscale", target_size=(28, 28))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 1 channel
	img = img.reshape(1, 28, 28, 1)
	# prepare pixel data
	img = img.astype('float32')
	img = img / 255.0
	return img

def main():
    prepare_data()
    model = define_model()
    train_model(model, "testconvnet.h5")
    evaluate_model()
    test_model()
    print("Done")

main()
