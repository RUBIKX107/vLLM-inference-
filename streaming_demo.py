import time

text = """
AI agents are autonomous systems capable
of reasoning, planning, and tool usage.
"""

words = text.split()

for word in words:

    print(word, end=" ", flush=True)

    time.sleep(0.15)