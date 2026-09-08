import tensorflow as tf
import numpy as np

IMG_SIZE = (128, 128)
BATCH_SIZE = 32

model = tf.keras.models.load_model("gender_classification_model.keras")

test_data = tf.keras.utils.image_dataset_from_directory(
    "dataset",
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

loss, accuracy = model.evaluate(test_data)

print("\nModel Evaluation")
print("Loss:", loss)
print("Accuracy:", accuracy * 100, "%")