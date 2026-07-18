import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf


# =====================================================
# LOAD CSS
# =====================================================

def load_css(css_file):
    """
    Load external CSS file.
    """

    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# =====================================================
# RESIZE IMAGE
# =====================================================

def resize_image(image, max_width=550):
    """
    Resize image while maintaining aspect ratio.
    """

    width, height = image.size

    if width <= max_width:
        return image

    ratio = max_width / width

    new_height = int(height * ratio)

    image = image.resize(
        (max_width, new_height),
        Image.LANCZOS
    )

    return image


# =====================================================
# PREPROCESS IMAGE
# =====================================================

def preprocess_image(image):
    """
    Convert uploaded image into model input.
    """

    image = image.resize((128, 128))

    img_array = tf.keras.preprocessing.image.img_to_array(image)

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    return img_array


# =====================================================
# PREDICT IMAGE
# =====================================================

def predict_image(model, image):
    """
    Perform prediction using trained model.
    """

    processed = preprocess_image(image)

    prediction = model.predict(
        processed,
        verbose=0
    )

    probabilities = prediction[0]

    index = np.argmax(probabilities)

    confidence = float(
        probabilities[index] * 100
    )

    from disease_info import CLASS_NAMES

    predicted_class = CLASS_NAMES[index]

    return {

        "class": predicted_class,

        "confidence": confidence,

        "probabilities": probabilities,

        "index": index

    }


# =====================================================
# TOP PREDICTIONS
# =====================================================

def top_predictions(probabilities, class_names, top=5):
    """
    Return top N predictions.
    """

    indices = np.argsort(
        probabilities
    )[::-1][:top]

    predictions = []

    for idx in indices:

        predictions.append(

            {

                "class": class_names[idx],

                "confidence": float(
                    probabilities[idx] * 100
                )

            }

        )

    return predictions


# =====================================================
# FORMAT CLASS NAME
# =====================================================

def format_class_name(name):
    """
    Convert class label into readable text.
    """

    return (

        name

        .replace("___", " : ")

        .replace("_", " ")

    )


# =====================================================
# CONFIDENCE COLOR
# =====================================================

def confidence_color(score):

    if score >= 90:
        return "#2E7D32"

    elif score >= 70:
        return "#43A047"

    elif score >= 50:
        return "#FB8C00"

    else:
        return "#D32F2F"


# =====================================================
# SEVERITY COLOR
# =====================================================

def severity_color(level):

    level = level.lower()

    if level == "none":
        return "#2E7D32"

    if level == "low":
        return "#66BB6A"

    if level == "medium":
        return "#FB8C00"

    return "#D32F2F"