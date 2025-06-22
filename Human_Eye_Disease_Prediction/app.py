# app.py
import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
import numpy as np
import tempfile
from PIL import Image, UnidentifiedImageError

# ---- Custom text snippets for each class ------------------------------
from recommendation import cnv, dme, drusen, normal   # make sure this exists

CLASS_NAMES = ['CNV', 'DME', 'DRUSEN', 'NORMAL']
RECOMMENDATIONS = {
    0: cnv,
    1: dme,
    2: drusen,
    3: normal,
}

# ---- Load model once & cache it ---------------------------------------
@st.cache_resource(show_spinner="Loading deep-learning model …")
def load_model():
    return tf.keras.models.load_model("Trained_Model.h5")  # rename if .h5

MODEL = load_model()

# ---- Image utilities --------------------------------------------------
def prepare_image(path: str) -> np.ndarray:
    """Load image and convert to MobileNetV3 input tensor (shape 1×224×224×3)."""
    img = tf.keras.utils.load_img(path, target_size=(224, 224))
    arr = tf.keras.utils.img_to_array(img)
    arr = np.expand_dims(arr, axis=0)
    arr = preprocess_input(arr)
    return arr

def predict(path: str) -> tuple[int, float]:
    """Return predicted class index and softmax confidence (0-1)."""
    tensor = prepare_image(path)
    logits = MODEL.predict(tensor)
    idx = int(np.argmax(logits))
    conf = float(tf.nn.softmax(logits)[0][idx])
    return idx, conf

# ---- Streamlit pages --------------------------------------------------
def page_home():
    st.markdown(
        """
        ## **OCT Retinal Analysis Platform**

        **Optical Coherence Tomography (OCT)** provides high-resolution cross-sectional images of the retina, enabling early detection of vision-threatening diseases.

        ---  
        **Key Features**  
        • Automated classification into **Normal, CNV, DME, Drusen**  
        • Instant treatment recommendations  
        • Easy upload workflow
        """
    )

def page_about():
    st.header("About")
    st.write(
        """
        This app demonstrates an OCT classifier trained on **84 k** images
        (Normal, CNV, DME, Drusen). Images were triple-graded by ophthalmology
        experts to ensure label reliability.
        """
    )

def page_predict():
    st.header("Retinal OCT Disease Identification")

    uploaded = st.file_uploader("Upload an OCT image …", type=["jpg", "jpeg", "png", "bmp", "tiff"])

    if uploaded:
        # Save bytes to a temp file (Streamlit will delete on app restart)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            tmp.write(uploaded.read())
            tmp_path = tmp.name

        # Display the uploaded image
        try:
            st.image(Image.open(tmp_path), caption="Uploaded scan", use_column_width=True)
        except UnidentifiedImageError:
            st.error("Error: uploaded file is not a valid image.")
            return

        if st.button("Predict"):
            with st.spinner("Analyzing …"):
                idx, conf = predict(tmp_path)

            st.success(f"**Prediction:** {CLASS_NAMES[idx]}  \n**Confidence:** {conf:.2%}")

            with st.expander("Explanation & Treatment Recommendation"):
                st.markdown(RECOMMENDATIONS[idx])

# ---- Main -------------------------------------------------------------
def main():
    st.sidebar.title("Dashboard")
    page = st.sidebar.selectbox("Navigation", ["Home", "About", "Disease Identification"])

    if page == "Home":
        page_home()
    elif page == "About":
        page_about()
    else:
        page_predict()

if __name__ == "__main__":
    main()
