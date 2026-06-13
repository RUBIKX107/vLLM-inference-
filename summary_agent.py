from transformers import pipeline
from agents.base_agent import BaseAgent


class SummaryAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            name="SummaryAgent",
            role="Summarizes research"
        )

        self.pipe = pipeline(
            "text-generation",
            model="distilgpt2"
        )

    def process(self, search_results):

        combined_text = "\n".join(
            [r["body"] for r in search_results]
        )

        prompt = f"""
Summarize this research clearly:

{combined_text}
"""

        result = self.pipe(
            prompt,
            max_length=200
        )

        return result[0]["generated_text"]