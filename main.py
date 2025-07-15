from src.reddit_scraper import scrape_user_data
from src.persona_builder import build_user_persona
from src.utils import save_persona_to_file

username = "kojied"
posts, comments = scrape_user_data(username)

print(f"Scraped {len(posts)} posts and {len(comments)} comments from u/{username}")

if posts or comments:
    persona = build_user_persona(posts, comments, username)
    save_persona_to_file(username, persona)

