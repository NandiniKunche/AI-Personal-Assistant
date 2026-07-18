from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"


def should_replace_memory(old_memory, new_memory):

    prompt = f"""
You are deciding whether a user's new memory should REPLACE an old memory.

Old memory:
{old_memory}

New memory:
{new_memory}

Examples:

Old: My name is Sona
New: My name is Nandini
Answer: YES

Old: I live in Hyderabad
New: I live in Bangalore
Answer: YES

Old: I like Python
New: I love Python
Answer: NO

Old: My favorite color is blue
New: My favorite color is red
Answer: YES

Reply ONLY with YES or NO.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # return response.choices[0].message.content.strip().upper() == "YES"
    reply = response.choices[0].message.content.strip().upper()

    print("Memory Decision:", reply)

    return reply.startswith("YES")