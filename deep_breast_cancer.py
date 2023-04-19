from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

model = keras.models.load_model('./model/CancerNet.h5')

x = "C:/Users/vosco/Documents/Ydays/test/"

BS = 32
valAug = ImageDataGenerator(rescale=1 / 255.0)
x = valAug.flow_from_directory(
    x,
    class_mode="categorical",
    target_size=(48, 48),
    color_mode="rgb",
    shuffle=False,
    batch_size=BS)

predIdxs = model.predict(x)
predIdxs = np.argmax(predIdxs, axis=1)