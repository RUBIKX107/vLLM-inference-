import time
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="distilgpt2"
)

prompts = [
    "Explain AI agents",
    "Explain RAG",
    "Explain MCP"
]

start = time.time()

results = pipe(
    prompts,
    max_length=80
)

end = time.time()

execution_time = end - start

total_chars = sum(
    len(r[0]["generated_text"])
    for r in results
)

print(f"Execution Time: {execution_time:.2f}s")
print(f"Total Characters Generated: {total_chars}")
print(f"Characters/sec: {total_chars/execution_time:.2f}")