from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"


def should_save_memory(user_message):

    prompt = f"""
You are an AI memory manager.

Decide whether the following user message should be stored as a long-term memory.

Store ONLY information that will help in future conversations.

Examples to STORE:
- My name is Nandini.
- I like Python.
- I work as a software engineer.
- I live in Hyderabad.
- Remember that I am learning AI.
- My favorite color is blue.
- I have a dog named Bruno.

Examples to IGNORE:
- Hi
- Hello
- Thanks
- What time is it?
- Tell me a joke.
- What is Python?
- Bye

Reply with ONLY:

YES

or

NO

User message:

"{user_message}"
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

    decision = response.choices[0].message.content.strip().upper()

    return decision == "YES"