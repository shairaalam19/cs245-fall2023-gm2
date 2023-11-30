import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics import pairwise_distances

# Function to calculate FID
def calculate_fid(real_images, generated_images):
    # Load InceptionV3 model pre-trained on ImageNet data
    model = InceptionV3(include_top=False, pooling='avg')

    # Preprocess images
    real_images = preprocess_input(real_images)
    generated_images = preprocess_input(generated_images)

    # Get InceptionV3 features
    real_features = model.predict(real_images)
    generated_features = model.predict(generated_images)

    # Calculate FID
    mu_real, sigma_real = np.mean(real_features, axis=0), np.cov(real_features, rowvar=False)
    mu_generated, sigma_generated = np.mean(generated_features, axis=0), np.cov(generated_features, rowvar=False)

    # Calculate FID using the formula
    fid = np.sum((mu_real - mu_generated)**2) + np.trace(sigma_real + sigma_generated - 2.0 * np.sqrt(sigma_real.dot(sigma_generated)))

    return fid

# Example usage
# Assuming you have real_images and generated_images as your datasets
# real_images and generated_images should be NumPy arrays of shape (num_samples, height, width, channels)

# Generate FID
fid_value = calculate_fid(real_images, generated_images)

# Print FID value
print(f"FID: {fid_value}")
