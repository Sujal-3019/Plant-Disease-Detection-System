import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="wide"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
.main{
    background-color:#f5f7fa;
}
.title{
    text-align:center;
    color:#2E7D32;
    font-size:42px;
    font-weight:bold;
}
.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}
.result{
    background-color:#E8F5E9;
    padding:20px;
    border-radius:10px;
    border-left:8px solid green;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("new_crop_disease_predictior_model.keras")

model = load_model()

# ----------------------------
# Classes
# ----------------------------
class_names = [
'Apple___Apple_scab',
'Apple___Black_rot',
'Apple___Cedar_apple_rust',
'Apple___healthy',
'Blueberry___healthy',
'Cherry_(including_sour)___Powdery_mildew',
'Cherry_(including_sour)___healthy',
'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
'Corn_(maize)___Common_rust_',
'Corn_(maize)___Northern_Leaf_Blight',
'Corn_(maize)___healthy',
'Grape___Black_rot',
'Grape___Esca_(Black_Measles)',
'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
'Grape___healthy',
'Orange___Haunglongbing_(Citrus_greening)',
'Peach___Bacterial_spot',
'Peach___healthy',
'Pepper,_bell___Bacterial_spot',
'Pepper,_bell___healthy',
'Potato___Early_blight',
'Potato___Late_blight',
'Potato___healthy',
'Raspberry___healthy',
'Soybean___healthy',
'Squash___Powdery_mildew',
'Strawberry___Leaf_scorch',
'Strawberry___healthy',
'Tomato___Bacterial_spot',
'Tomato___Early_blight',
'Tomato___Late_blight',
'Tomato___Leaf_Mold',
'Tomato___Septoria_leaf_spot',
'Tomato___Spider_mites Two-spotted_spider_mite',
'Tomato___Target_Spot',
'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
'Tomato___Tomato_mosaic_virus',
'Tomato___healthy'
]

# ----------------------------
# Header
# ----------------------------
st.markdown("<h1 class='title'>🌿 Plant Disease Detection System</h1>", unsafe_allow_html=True)

st.markdown(
    "<p class='subtitle'>Upload a plant leaf image and let AI identify the disease.</p>",
    unsafe_allow_html=True
)

st.divider()

# ----------------------------
# Layout
# ----------------------------
left, right = st.columns([1,1])

with left:

    uploaded_file = st.file_uploader(
        "Upload Leaf Image",
        type=["jpg","jpeg","png"]
    )

    predict_btn = st.button("🔍 Predict Disease", use_container_width=True)

with right:

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if predict_btn:

            img = image.resize((128,128))

            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)

            index = np.argmax(prediction)

            confidence = float(np.max(prediction))*100

            disease = class_names[index]

            st.markdown("## Prediction")

            st.success(disease.replace("___"," : "))

            st.progress(confidence/100)

            st.metric(
                label="Confidence",
                value=f"{confidence:.2f}%"
            )

            st.write("### Top 5 Predictions")

            top5 = np.argsort(prediction[0])[::-1][:5]

            for i in top5:
                st.write(
                    f"**{class_names[i].replace('___',' : ')}**"
                )
                st.progress(float(prediction[0][i]))
                st.write(f"{prediction[0][i]*100:.2f}%")

st.divider()

st.markdown(
"""
### About

This AI model detects diseases in plant leaves using a Convolutional Neural Network (CNN).

Supported Crops:

- 🍎 Apple
- 🍅 Tomato
- 🥔 Potato
- 🍇 Grape
- 🌽 Corn
- 🍑 Peach
- 🍓 Strawberry
- 🫑 Pepper
- 🍊 Orange
- 🫐 Blueberry
- 🌱 Soybean
- 🌿 Squash
"""
)