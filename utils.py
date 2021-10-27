import numpy as np
from numpy import expand_dims
import pandas as pd
import os
import pickle
import keras
from keras.layers import Dense,Flatten,Input,concatenate,Dropout,GlobalMaxPooling2D
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Model
from keras.optimizers import Adam, SGD
from keras.applications.vgg16 import (
    VGG16, preprocess_input, decode_predictions)
from keras.layers.core import Lambda
#from tensorflow.python.framework import ops
#import tensorflow as tf
import sys
#from keras import Sequential
#from keras import activations
import keras.backend as K
from collections import Counter
from sklearn.model_selection import StratifiedKFold
from keras.models import model_from_json
from keras.models import load_model

num_struct = 6

def own_train_generator_func(train_df, train_generator, num_struct, n_classes):
    count = 0
    while True:
        if count == len(train_df.index):
            train_generator.reset()
            #break
        count += 1
        data = train_generator.next()
        
        imgs = data[0]
        meta = data[1][:,:num_struct]
        targets = data[1][:,-1*n_classes:]
        
        yield [imgs, meta], targets

def own_test_generator_func(test_df, test_generator, num_struct, n_classes):
    count = 0
    test_generator.reset()
    while True:
        if count == len(test_df.index):
            test_generator.reset()
            #break
        count += 1
        data = test_generator.next()
                
        imgs = data[0]
        meta = data[1][:,:num_struct]
        targets = data[1][:,-1*n_classes:]
        
        yield [imgs, meta], targets
        
        
def own_test_generator_func_unknown(unknown_df, unknown_generator, num_struct, n_classes):
    count = 0
    unknown_generator.reset()
    while True:
        if count == len(unknown_df.index):
            unknown_generator.reset()
            #break
        count += 1
        data = unknown_generator.next()
                
        imgs = data[0]
        meta = data[1][:,:num_struct]
        targets = data[1][:,-1*n_classes:]
        
        yield [imgs, meta], targets
        
def create_model(hidden_vgg, learning_rate, reg, n_classes, num_struct):
    # Import pre-trained VGG16 model
    pretrained_model = VGG16(input_shape=(224, 224, 3), include_top=False, weights="imagenet")

    # Freeze all the layers
    for layer in pretrained_model.layers[:]:
        layer.trainable = False

    # Check the trainable status of the individual layers
    for layer in pretrained_model.layers:
        print(layer, layer.trainable)

    # Build additional dense and classification layers
    last_layer = pretrained_model.get_layer('block5_pool')
    last_output = last_layer.output

    x = Flatten()(last_output)
    # Construct input layer for structure
    meta_input = Input(shape = (num_struct,))
    merged = keras.layers.Concatenate(axis=1)([x, meta_input])
    ###############################################à
    x = Dense(hidden_vgg, activation='relu', kernel_regularizer=reg)(merged)
    x = Dropout(0.5)(x) 
    x = Dense(n_classes, activation='softmax', name='predictions')(x)
    #model = Model(inputs = [pretrained_model.input, struct_model.input], outputs = x)
    model = Model(inputs = [pretrained_model.input, meta_input], outputs = x)

    model.summary()
    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr=learning_rate),
                  metrics=['acc'])
    
    return model