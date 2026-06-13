from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

pipe = pipeline(
    "text-generation",
    model="distilgpt2"
)


@app.post("/generate")
def generate(prompt: str):

    result = pipe(
        prompt,
        max_length=80
    )

    return {
        "response": result[0]["generated_text"]
    }