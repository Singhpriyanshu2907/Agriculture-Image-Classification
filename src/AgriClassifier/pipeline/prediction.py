import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # Load the trained model
        #model = load_model(os.path.join("artifacts","training", "model.h5"))
        model = load_model(os.path.join("model", "model.h5"))

        # List of 30 class names (update this list with your actual class labels)
        class_names = [
            "Banana", "Cardamom", "Cherry", "Chilli", "Clove",
            "Coconut", "Coffee", "Cotton", "Cucumber", "Fox Nut",
            "Gram", "Jowar", "Jute", "Lemon", "Almond",
            "Maize", "Mustard", "Olive", "Pineapple", "Papaya",
            "Pearl", "Rice", "Soyabean", "Sugarcane", "Sunflower",
            "Tea", "Tobacco", "Tomato", "Mung", "Wheat"
        ]

        # Load and preprocess the input image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Get predictions and determine the class
        predictions = model.predict(test_image)
        predicted_class_index = np.argmax(predictions, axis=1)[0]
        predicted_class_name = class_names[predicted_class_index]

        # Print and return the prediction
        print(f"Predicted class: {predicted_class_name}")
        return [{"image": predicted_class_name}]