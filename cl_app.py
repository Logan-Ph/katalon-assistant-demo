import chainlit as cl
from app.llm.ai_agent import stream_gemini_response
import asyncio
import random

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Morning routine ideation",
            message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
            icon="/public/idea.svg",
            ),
        cl.Starter(
            label="Explain superconductors",
            message="Explain superconductors like I'm five years old.",
            icon="/public/learn.svg",
            ),
        cl.Starter(
            label="Python script for daily email reports",
            message="Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.",
            icon="/public/terminal.svg",
            ),
        cl.Starter(
            label="Text inviting friend to wedding",
            message="Write a text asking a friend to be my plus-one at a wedding next month. I want to keep it super short and casual, and offer an out.",
            icon="/public/write.svg",
            )
        ]
    
@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )


@cl.on_message
async def handle_message(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")

    async for chunk in stream_gemini_response(message.content):
        if isinstance(chunk, str):
            # Split the chunk into individual characters and stream with delay
            for char in chunk:
                await msg.stream_token(char)
                # Add a small random delay between characters
                await asyncio.sleep(random.uniform(0.001, 0.005))
        else:
            # If not a string, stream as is
            await msg.stream_token(chunk)
            await asyncio.sleep(random.uniform(0.001, 0.003))

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()
    