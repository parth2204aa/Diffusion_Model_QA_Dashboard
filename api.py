# ------------------- backend/api.py -------------------
from fastapi import FastAPI
from pydantic import BaseModel
from model_runner import generate_image
from qa_checks import run_qa_checks
from fastapi.middleware.cors import CORSMiddleware
import base64
from io import BytesIO

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptInput(BaseModel):
    prompt: str

@app.post("/generate")
def generate(prompt: PromptInput):
    image = generate_image(prompt.prompt)
    qa_results = run_qa_checks(image)

    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return {
        "image": img_str,
        "qa_results": qa_results,
        "prompt": prompt.prompt
    }
