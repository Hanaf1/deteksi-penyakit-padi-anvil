import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model 

# Load model once when the server module is loaded
model = load_model('rice_disease_weights.h5')
class_labels = {0: 'Bacterial leaf blight', 1: 'Brown spot', 2: 'Leaf smut'}

@anvil.server.callable
def predict_disease(img):
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0) / 255.0  # Normalize
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions)
    return class_labels.get(predicted_class, 'Unknown class')
