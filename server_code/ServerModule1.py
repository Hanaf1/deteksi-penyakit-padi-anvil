import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
from PIL import Image
import gdown
import anvil.media


model_path = "rice_disease_weights.h5"
model = tf.keras.models.load_model(model_path)

# Class labels for the disease prediction
class_labels = {0: 'Bacterial leaf blight', 1: 'Brown spot', 2: 'Leaf smut'}

def prediksi(img):
    img = cv2.resize(img, (224, 224))  # Resize the image
    img_array = np.expand_dims(img, axis=0) / 255.0  # Normalize

    # Make predictions
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)

    # Check the predicted class
    if predicted_class in class_labels:
        return class_labels[predicted_class]
    else:
        return 'Unknown class'


@anvil.server.callable
def prediksipenyakitpadi(file):

    with anvil.media.TempFile(file) as f:
        img = np.array(Image.open(f))
    hasil = "hasil prediksi penyakit : " + prediksi(img)
    return hasil