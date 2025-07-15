# src/persona_builder.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MAX_CONTENT_TOKENS = 14000

def build_user_persona(posts, comments, username):
    # Build combined content
    combined_chunks = []
    total_length = 0

    def safe_add(text):
        nonlocal total_length
        if total_length + len(text) < MAX_CONTENT_TOKENS:
            combined_chunks.append(text)
            total_length += len(text)

    for p in posts:
        entry = f"[POST] Title: {p['title']}\nText: {p['body']}\nSubreddit: {p['subreddit']}\nURL: {p['url']}\n\n"
        safe_add(entry)

    for c in comments:
        entry = f"[COMMENT] Text: {c['body']}\nSubreddit: {c['subreddit']}\nURL: {c['url']}\n\n"
        safe_add(entry)

    combined_text = "".join(combined_chunks)

    prompt = f"""
You are a behavioral analyst AI. Based on this Reddit user’s content, build a detailed user persona including:

- Age (if guessable), Occupation, Location
- Archetype (e.g., Creator, Analyst), Online Behavior
- Interests, Hobbies, Motivations, Frustrations, Goals
- Personality traits (Introvert/Extrovert etc.), Writing Style
- Cite Reddit posts/comments (include URLs) for every key insight

Here is content for Reddit user u/{username}:

{combined_text}
    """

    model = genai.GenerativeModel("gemini-1.5-flash-latest")


    chat = model.start_chat()
    response = chat.send_message(prompt)

    return response.text
