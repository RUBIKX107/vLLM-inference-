from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="distilgpt2"
)

result = pipe(
    "Explain AI agents",
    max_length=50
)

print(result)