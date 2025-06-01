from django.shortcuts import render
from django.contrib import messages
from .models import Detection
import tensorflow as tf
import numpy as np
from PIL import Image
import io

def load_model():
    try:
        model = tf.keras.models.load_model('my_model.keras')
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def preprocess_image(image):
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Resize to expected input size (adjust dimensions as needed)
    image = image.resize((224, 224))
    
    # Convert to array and preprocess
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    
    return img_array

def home(request):
    return render(request, 'home.html')

def detection(request):
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            # Load the model
            model = load_model()
            if not model:
                messages.error(request, "Error loading the model. Please try again later.")
                return render(request, 'detection.html')
            
            # Process the uploaded image
            image_file = request.FILES['image']
            image = Image.open(image_file)
            processed_image = preprocess_image(image)
            
            # Make prediction
            prediction = model.predict(processed_image)
            confidence = float(prediction[0][0]) * 100
            result = "Malignant" if confidence > 50 else "Benign"
            
            # Save the detection
            detection = Detection.objects.create(
                image=image_file,
                result=result,
                confidence=confidence
            )
            
            context = {
                'result': {
                    'image': detection.image,
                    'result': result,
                    'confidence': confidence,
                    'is_malignant': result == "Malignant"
                }
            }
            
            return render(request, 'detection.html', context)
            
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'detection.html')
    
    return render(request, 'detection.html')

def about(request):
    return render(request, 'about.html') 