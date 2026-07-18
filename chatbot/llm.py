import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime

from chatbot.memory_decision import should_save_memory
from chatbot.memory import (
    load_memory,
    save_memory,
    search_memory,
    delete_memory,
    memory
)
from chatbot.memory_filter import should_replace_memory

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"

load_memory()


def get_ai_response(messages):

    # Latest user message
    user_question = messages[-1]["content"]

    # Search memory
    memories = search_memory(user_question)
    memory_text = "\n".join(memories)

    # Current date & time
    now = datetime.now()
    current_date = now.strftime("%d %B %Y")
    current_time = now.strftime("%I:%M %p")

    # System Prompt
    system_prompt = f"""
You are a helpful AI Personal Assistant.

Current Date:
{current_date}

Current Time:
{current_time}

Relevant memories:

{memory_text}

Rules:

1. Use memories only if they are relevant to the user's question.

2. Mention the current date or time ONLY when the user explicitly asks for it.

3. Do NOT mention the current date or time in unrelated answers.

4. Never use old memories as today's date or time.

5. If no memory is relevant, answer normally and naturally.
"""

    final_messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ] + messages

    response = client.chat.completions.create(
        model=MODEL,
        messages=final_messages
    )

    answer = response.choices[0].message.content

    # ----------------------------
    # Save memory intelligently
    # ----------------------------

    if should_save_memory(user_question):

        updated = False

        for old_memory in memory:

            if should_replace_memory(old_memory, user_question):

                delete_memory(old_memory)
                save_memory(user_question)

                updated = True
                break

        if not updated:
            save_memory(user_question)

    return answer