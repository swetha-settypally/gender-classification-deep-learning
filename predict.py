import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array

model = tf.keras.models.load_model("gender_classification_model.keras")

image_path = input("Enter image path: ").strip().strip('"')

image = load_img(image_path, target_size=(128, 128))
image_array = img_to_array(image)
image_array = image_array / 255.0
image_array = tf.expand_dims(image_array, 0)

prediction = model.predict(image_array)[0][0]

if prediction >= 0.5:
    print("Prediction: Female")
else:
    print("Prediction: Male")