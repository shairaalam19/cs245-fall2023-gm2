import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics import pairwise_distances

# Function to load and preprocess images
def load_images(filepaths):
    images = []
    for filepath in filepaths:
        img = image.load_img(filepath, target_size=(299, 299))  # Assuming InceptionV3 input size
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        images.append(img)
    return np.vstack(images)

# Function to calculate FID
def calculate_fid(real_images, generated_images):
    # Load InceptionV3 model pre-trained on ImageNet data
    model = InceptionV3(include_top=False, pooling='avg')

    # Get InceptionV3 features
    real_features = model.predict(real_images)
    generated_features = model.predict(generated_images)

    # Calculate FID
    mu_real, sigma_real = np.mean(real_features, axis=0), np.cov(real_features, rowvar=False)
    mu_generated, sigma_generated = np.mean(generated_features, axis=0), np.cov(generated_features, rowvar=False)

    # Ensure covariance matrices have at least two dimensions
    sigma_real = np.atleast_2d(sigma_real)
    sigma_generated = np.atleast_2d(sigma_generated)

    # Calculate FID using the formula
    fid = np.sum((mu_real - mu_generated)**2) + np.trace(sigma_real + sigma_generated - 2.0 * np.sqrt(sigma_real.dot(sigma_generated)))

    return fid

def compare_images(img1, img2):
    # Specify file paths for the images
    real_image_paths = [img1]
    generated_image_paths = [img2]

    # Load and preprocess images
    real_images = load_images(real_image_paths)
    generated_images = load_images(generated_image_paths)

    # Generate FID
    fid_value = calculate_fid(real_images, generated_images)

    # Print FID value
    print(f"FID: {fid_value}")

def compare_image_folders(real_images_folder, generated_images_folder):
    # Specify the folders containing the original and generated images

    # Get a list of filenames in each folder
    real_image_files = sorted(os.listdir(real_images_folder))
    generated_image_files = sorted(os.listdir(generated_images_folder))

    # Initialize a list to store FID values for each pair
    fid_values = []

    # Loop through the images and calculate FID
    for real_image_file, generated_image_file in zip(real_image_files, generated_image_files):
        real_image_path = os.path.join(real_images_folder, real_image_file)
        generated_image_path = os.path.join(generated_images_folder, generated_image_file)

        # Load and preprocess images
        real_images = load_images([real_image_path])
        generated_images = load_images([generated_image_path])

        # Generate FID
        fid_value = calculate_fid(real_images, generated_images)

        # Print FID value for the current pair
        print(f"FID for real photograph {real_image_file} and generated photograph {generated_image_file}: {fid_value}")

        # Store FID value in the list
        fid_values.append(fid_value)

    # Calculate and print the average FID value
    average_fid = np.mean(fid_values)
    print(f"Average FID: {average_fid}")
