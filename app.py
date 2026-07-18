import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from pathlib import Path

# Import helper files
from utils import (
    predict_image,
    load_css,
    resize_image,
    top_predictions,
    format_class_name,
    confidence_color
)

from disease_info import (
    DISEASE_INFO,
    CLASS_NAMES,
)

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Plant Disease AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# LOAD CUSTOM CSS
# ---------------------------------------------------

load_css("style.css")

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

@st.cache_resource(show_spinner=False)
def load_model():
    return tf.keras.models.load_model(
        "model/new_crop_disease_predictior_model.keras"
    )

model = load_model()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.markdown("# 🌿 Plant Disease AI")

    st.markdown(
        """
Detect diseases from plant leaves using a
Convolutional Neural Network trained on
the PlantVillage Dataset.
"""
    )

    st.divider()

    st.markdown("### 🧠 Model")

    st.success("TensorFlow / Keras")

    st.markdown("### 📊 Dataset")

    st.info("PlantVillage")

    st.markdown("### 🎯 Classes")

    st.metric(
        "Supported Diseases",
        len(CLASS_NAMES)
    )

    st.divider()

    st.markdown("### 🌱 Supported Crops")

    crops = [
        "🍅 Tomato",
        "🍎 Apple",
        "🥔 Potato",
        "🍇 Grape",
        "🌽 Corn",
        "🍊 Orange",
        "🍓 Strawberry",
        "🍑 Peach",
        "🫐 Blueberry",
        "🫑 Pepper",
        "🌱 Soybean",
        "🌿 Squash",
        "🍒 Cherry"
    ]

    for crop in crops:
        st.write(crop)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

st.markdown(
"""
<div class="hero">

<h1>
🌿 Plant Disease Detection System
</h1>

<p>

Identify plant diseases instantly using
Artificial Intelligence.

Upload a leaf image and receive
accurate disease predictions powered by
your custom-trained TensorFlow model.

</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------

left, right = st.columns(
    [1,1],
    gap="large"
)

# ---------------------------------------------------
# LEFT COLUMN
# ---------------------------------------------------

with left:

    st.markdown(
        """
<div class="glass-card">

<h3>📤 Upload Leaf Image</h3>

Upload a clear image of a plant leaf
for disease analysis.

</div>
""",
unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "",
        type=["jpg","jpeg","png"]
    )

    predict_btn = st.button(
        "🔍 Analyze Leaf",
        use_container_width=True,
        type="primary"
    )

# ---------------------------------------------------
# RIGHT COLUMN
# ---------------------------------------------------

with right:

    st.markdown(
        """
<div class="glass-card">

<h3>🖼️ Preview</h3>

</div>
""",
unsafe_allow_html=True
    )

    image = None

    if uploaded_file:

        image = Image.open(
            uploaded_file
        ).convert("RGB")

        image = resize_image(
            image,
            max_width=550
        )

        st.image(
            image,
            use_container_width=False
        )

    else:

        st.info(
            "Upload an image to preview it here."
        )

# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------

if uploaded_file and predict_btn:

    with st.spinner(
        "🧠 AI is analyzing the leaf..."
    ):

        prediction = predict_image(
            model,
            image
        )

        predicted_class = prediction["class"]

        confidence = prediction["confidence"]

        probabilities = prediction["probabilities"]

    st.divider()

    st.markdown(
"""
<h2 style="text-align:center;">
🩺 Prediction Result
</h2>
""",
unsafe_allow_html=True
    )

    disease = DISEASE_INFO.get(
        predicted_class,
        {}
    )

# =================================================
# PREMIUM PREDICTION DASHBOARD
# =================================================


display_name = format_class_name(
    predicted_class
)


confidence_color_code = confidence_color(
    confidence
)


st.markdown(
f"""

<div class="prediction-card">

<h2>
🦠 Disease Detected
</h2>


<h1>
{display_name}
</h1>


<div style="
background:#eeeeee;
border-radius:20px;
height:18px;
overflow:hidden;
margin:20px 0;
">


<div style="
width:{confidence}%;
background:{confidence_color_code};
height:100%;
border-radius:20px;
">
</div>


</div>


<h2 style="
color:{confidence_color_code};
">

{confidence:.2f}% Confidence

</h2>


</div>

""",
unsafe_allow_html=True
)
# =================================================
# TOP 5 PREDICTIONS
# =================================================


st.markdown(
"""
## 📊 Top 5 AI Predictions
"""
)


top5 = top_predictions(
    probabilities,
    CLASS_NAMES,
    top=5
)


rank_icons = [
    "🥇",
    "🥈",
    "🥉",
    "4️⃣",
    "5️⃣"
]


for index, item in enumerate(top5):


    name = format_class_name(
        item["class"]
    )


    score = item["confidence"]


    st.markdown(
    f"""
    
    <div class="glass-card">


    <h3>
    {rank_icons[index]} {name}
    </h3>


    <div style="
    background:#eeeeee;
    border-radius:15px;
    height:12px;
    ">


    <div style="
    width:{score}%;
    background:#43A047;
    height:100%;
    border-radius:15px;
    ">
    </div>


    </div>


    <p>
    Confidence:
    <b>
    {score:.2f}%
    </b>
    </p>


    </div>

    """,
    unsafe_allow_html=True
    )
    # =================================================
# DISEASE INFORMATION
# =================================================


st.divider()


st.markdown(
"""
## 🌿 Disease Information
"""
)


info = DISEASE_INFO.get(
    predicted_class
)


if info:


    col1, col2 = st.columns(2)


    with col1:

        st.markdown(
        f"""
        <div class="glass-card">

        <h3>
        🌱 Crop
        </h3>

        <h2>
        {info['crop']}
        </h2>


        <h3>
        ⚠ Severity
        </h3>

        <h2>
        {info['severity']}
        </h2>

        </div>

        """,
        unsafe_allow_html=True
        )


    with col2:

        st.markdown(
        f"""
        <div class="glass-card">

        <h3>
        📝 Description
        </h3>

        <p>
        {info['description']}
        </p>

        </div>

        """,
        unsafe_allow_html=True
        )
        # =================================================
# DISEASE DETAILS
# =================================================


if info:

    st.divider()


    # ---------------------------------------------
    # Symptoms + Causes
    # ---------------------------------------------


    col1, col2 = st.columns(2, gap="large")


    with col1:

        st.markdown(
        """
        <div class="glass-card">

        <h2>
        ⚠️ Symptoms
        </h2>

        """,
        unsafe_allow_html=True
        )


        for symptom in info["symptoms"]:

            st.write(
                f"🔸 {symptom}"
            )


        st.markdown(
        "</div>",
        unsafe_allow_html=True
        )



    with col2:


        st.markdown(
        """
        <div class="glass-card">

        <h2>
        🦠 Causes
        </h2>

        """,
        unsafe_allow_html=True
        )


        for cause in info["causes"]:

            st.write(
                f"🔸 {cause}"
            )


        st.markdown(
        "</div>",
        unsafe_allow_html=True
        )



    # ---------------------------------------------
    # Prevention + Treatment
    # ---------------------------------------------


    st.write("")


    col3, col4 = st.columns(2, gap="large")



    with col3:


        st.markdown(
        """
        <div class="glass-card">

        <h2>
        🛡 Prevention
        </h2>

        """,
        unsafe_allow_html=True
        )


        for item in info["prevention"]:

            st.write(
                f"✅ {item}"
            )


        st.markdown(
        "</div>",
        unsafe_allow_html=True
        )



    with col4:


        st.markdown(
        """
        <div class="glass-card">

        <h2>
        💊 Recommended Treatment
        </h2>

        """,
        unsafe_allow_html=True
        )


        for item in info["treatment"]:

            st.write(
                f"💡 {item}"
            )


        st.markdown(
        "</div>",
        unsafe_allow_html=True
        )
        # =================================================
# AI MODEL INFORMATION
# =================================================


st.divider()


st.markdown(
"""
<h2 style="text-align:center;">
🤖 About The AI Model
</h2>
""",
unsafe_allow_html=True
)



model_col1, model_col2, model_col3, model_col4 = st.columns(4)



model_col1.metric(
    "Framework",
    "TensorFlow"
)


model_col2.metric(
    "Architecture",
    "CNN"
)


model_col3.metric(
    "Input Size",
    "128×128"
)


model_col4.metric(
    "Classes",
    "38"
)



st.markdown(
"""

<div class="glass-card">

<h3>
🌿 Project Information
</h3>


<p>

This AI system uses a custom-trained
Convolutional Neural Network (CNN)
model to identify plant diseases from
leaf images.

The model was trained using the
PlantVillage dataset and integrated
with Streamlit to provide real-time
disease detection.

</p>


</div>


""",
unsafe_allow_html=True
)
# =================================================
# FOOTER
# =================================================


st.markdown(
"""

<br>

<div style="
text-align:center;
color:#666;
padding:20px;
">


🌿 Plant Disease AI Assistant

<br>

Built using:
TensorFlow • Streamlit • Python


<br>

AI-powered crop health detection system


</div>

""",
unsafe_allow_html=True
)