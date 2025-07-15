# src/utils.py

import os

def save_persona_to_file(username, persona_text):
    """
    Saves persona text to a .txt file in the users/ folder.
    
    Args:
        username (str): Reddit username
        persona_text (str): Full generated persona
    """
    folder = "users"
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = f"{folder}/{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)

    print(f"✅ Persona saved to: {filename}")
