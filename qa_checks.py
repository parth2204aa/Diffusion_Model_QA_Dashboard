# ------------------- backend/qa_checks.py -------------------
from PIL import Image
import numpy as np
import cv2

def blur_detector(image: Image.Image) -> float:
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var

def nsfw_check(image: Image.Image) -> float:
    # Dummy NSFW checker. Replace with real logic or model.
    return 0.1

def run_qa_checks(image):
    return {
        "blur_score": blur_detector(image),
        "nsfw_score": nsfw_check(image)
    }
