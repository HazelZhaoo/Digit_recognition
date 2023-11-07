from keras.models import load_model
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab , Image
import numpy as np

model = load_model('mnist.h5')

def predict_digit(img):
    img = img.resize((28 , 28)) #resize to 28 , 28
    img = img.convert('L')
    img = np.array(img)

    #reshape to support the model input and normal
    img = img.reshape(1 , 28 , 28 , 1)
    img = img/255.0

    #predict the calss of the image
    output = model.predict([img])[0]
    return np.argmax(output) ,max(output)

class App(tk.Tk):
    def __init__(self):