# ------------------- frontend/dashboard.py -------------------
import streamlit as st
import requests
from PIL import Image
import io
import base64

st.set_page_config(page_title="Diffusion QA Dashboard", layout="centered")
st.title("\U0001F5A5️ Diffusion Model QA Dashboard")

prompt = st.text_input("Enter a prompt to generate an image:")
if st.button("Generate Image") and prompt:
    with st.spinner("Generating image and running QA checks..."):
        res = requests.post("http://localhost:8000/generate", json={"prompt": prompt})
        if res.status_code == 200:
            data = res.json()
            image = Image.open(io.BytesIO(base64.b64decode(data["image"])))

            st.image(image, caption="Generated Image", use_column_width=True)

            st.subheader("QA Results")
            for key, value in data["qa_results"].items():
                st.metric(label=key.replace("_", " ").title(), value=round(value, 4))
        else:
            st.error("Failed to generate image.")
