# pip install tensorflow
# pip install keras


import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.datasets import boston_housing

(x_train, y_train), (x_test, y_test) = boston_housing.load_data()
#print(x_train.shape, y_train.shape) #(404,13), (404,)
#print(x_test.shape, y_test.shape) #(102, 13), (102,)

#print(x_train[:3,:].shape) # row 3, all columns

# Extract the last 100 rows from the training data to create the validation datasets.
x_val = x_train[300:,]
y_val = y_train[300:,]

# Define the model architecture
model = Sequential()
model.add(Dense(13, input_dim=13, kernel_initializer='normal',activation='relu'))
model.add(Dense(6, kernel_initializer='normal',activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))

# Compile model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_absolute_percentage_error'])
# Train the model
model.fit(x_train, y_train, batch_size=32, epochs=99, validation_data=(x_val,y_val))
# Evaluate model
results = model.evaluate(x_test, y_test)
for i in range(len(model.metrics_names)):
    print(model.metrics_names[i]," : ", results[i])












########################################################

# # Generate dummy training dataset
# np.random.seed(2018)
# x_train = np.random.random((6000,10))
# y_train = np.random.randint(2, size=(6000, 1))

# # Generate dummy validation dataset
# x_val = np.random.random((2000,10))
# y_val = np.random.randint(2, size=(2000, 1))
# # Generate dummy test dataset
# x_test = np.random.random((2000,10))
# y_test = np.random.randint(2, size=(2000, 1))
# #Define the model architecture
# model = Sequential()
# model.add(Dense(64, input_dim=10,activation = "relu")) #Layer 1
# model.add(Dense(32,activation = "relu")) #Layer 2
# model.add(Dense(16,activation = "relu")) #Layer 3
# model.add(Dense(8,activation = "relu")) #Layer 4
# model.add(Dense(4,activation = "relu")) #Layer 5
# model.add(Dense(1,activation = "sigmoid")) #Output Layer
# #Configure the model
# model.compile(optimizer='Adam',loss='binary_crossentropy',metrics=['accuracy'])
# #Train the model
# model.fit(x_train, y_train, batch_size=64, epochs=3, validation_data=(x_val,y_val))
# #Evaluate
# print(model.evaluate(x_test,y_test))
# #Make predictions on the test dataset and print the first 10 predictions
# pred = model.predict(x_test)
# print(pred[:10])














