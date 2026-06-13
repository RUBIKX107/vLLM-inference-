from transformers import pipeline
import time

pipe = pipeline(
    "text-generation",
    model="distilgpt2"
)

prompts = [
    "Explain AI agents",
    "Explain RAG systems",
    "Explain TinyML",
    "Explain MLOps"
]

start = time.time()

results = pipe(
    prompts,
    max_length=60
)

end = time.time()

for i, result in enumerate(results):

    print(f"\nPROMPT {i+1}")
    print(prompts[i])

    print("\nOUTPUT:")
    print(result[0]["generated_text"])

print(f"\nExecution Time: {end - start:.2f} seconds")