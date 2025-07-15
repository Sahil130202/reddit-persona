# Reddit User Persona Generator

This project is a coding assignment for a part-time AI/LLM Engineer Internship at BeyondChats. The tool takes a Reddit username as input, scrapes the user's posts and comments, and generates a detailed user persona by analyzing the textual content using Google's Gemini API (free-tier compatible). Each inferred trait is supported by citations from the user’s Reddit activity.

## Features

- Scrapes public Reddit posts and comments using the Reddit API (`praw`)
- Cleans and combines user-generated content
- Sends input to Gemini 1.5 LLM (via `google-generativeai`) for persona generation
- Outputs a structured user persona in plain text format
- Includes source links for every characteristic mentioned
- Modular Python codebase with clear separation of logic

## Technologies Used

- Python 3.11+
- `praw` – Reddit API wrapper
- `google-generativeai` – Gemini API for LLM-based analysis
- `python-dotenv` – for API credential management
- `tqdm` – progress bar support (optional)
- Google MakerSuite for Gemini API key

## Folder Structure

reddit-persona/
├── main.py # Entry point
├── .env # API keys (excluded from Git)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── users/ # Output folder for generated persona files
└── src/
├── reddit_scraper.py # Reddit data collection
├── persona_builder.py # Gemini LLM integration and prompt
└── utils.py # File-saving and helper functions


## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/reddit-persona.git
cd reddit-persona
Create and activate a virtual environment (recommended):
python3 -m venv tfenv
source tfenv/bin/activate  # Linux/macOS
# OR
.\tfenv\Scripts\activate   # Windows
Install dependencies:
pip install -r requirements.txt
Create a .env file in the root directory:
REDDIT_CLIENT_ID=your_reddit_app_client_id
REDDIT_CLIENT_SECRET=your_reddit_app_client_secret
REDDIT_USER_AGENT=script:redit-persona:v1.0 (by /u/your_reddit_username)
GOOGLE_API_KEY=your_gemini_api_key
Note: Do not commit your .env file. Ensure it is listed in .gitignore.
Usage

Edit main.py and set the target Reddit username:

username = "kojied"
Run the script:

python main.py
Upon success, a structured persona file will be saved to:

users/kojied_persona.txt
Sample Output

The output file includes sections such as:

Age, Occupation, Location (if inferable)
Interests and Hobbies
Motivations, Frustrations, Goals
Writing Style and Personality Traits
Cited Reddit links used for each inference
Example snippet:

User Persona for u/kojied

Age: Estimated 22–30
Occupation: Likely a software engineer or student
Interests: Privacy tools, Linux, anime
Frustrations: Moderation inconsistencies

Cited from: https://www.reddit.com/r/linux/comments/abc123/example
Gemini API Considerations

The script uses Gemini's free-tier access. If you hit a rate limit or quota error (HTTP 429), wait a few minutes and re-run the script. To avoid this:

Use the gemini-1.5-flash-latest model (configured in persona_builder.py)
Limit the number of posts/comments if needed
Troubleshooting

Empty output file: Gemini may have returned a blank response due to rate limits or malformed input
429 Errors: You’ve exceeded your daily or per-minute quota. Switch to a new API key or use a lighter model
PRAW errors: Check that your Reddit API credentials are correct and the user exists
License

This project is provided as part of a coding assignment. All intellectual property belongs to the author unless the assignment is accepted and ownership is transferred as part of the hiring process.

Contact

For any questions, please reach out via Internshala or the official hiring channel at BeyondChats.


---

Let me know if you'd like:
- A version formatted for PDF or print submission
- A quick deployable `.zip` of the final repo for upload
- Help generating a second persona as an additional test case

You're fully ready to submit.

You said:
Yeah, this is good. Now, give it to me in markdown format for my readme file
ChatGPT said:
Here's the full README.md content in Markdown format, ready to paste into your file:

# Reddit User Persona Generator

This project is a coding assignment for a part-time AI/LLM Engineer Internship at BeyondChats. The tool takes a Reddit username as input, scrapes the user's posts and comments, and generates a detailed user persona by analyzing the textual content using Google's Gemini API (free-tier compatible). Each inferred trait is supported by citations from the user’s Reddit activity.

## Features

- Scrapes public Reddit posts and comments using the Reddit API (`praw`)
- Cleans and combines user-generated content
- Sends input to Gemini 1.5 LLM (via `google-generativeai`) for persona generation
- Outputs a structured user persona in plain text format
- Includes source links for every characteristic mentioned
- Modular Python codebase with clear separation of logic

## Technologies Used

- Python 3.11+
- `praw` – Reddit API wrapper
- `google-generativeai` – Gemini API for LLM-based analysis
- `python-dotenv` – for API credential management
- `tqdm` – progress bar support (optional)
- Google MakerSuite for Gemini API key

## Folder Structure

reddit-persona/
├── main.py # Entry point
├── .env # API keys (excluded from Git)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── users/ # Output folder for generated persona files
└── src/
├── reddit_scraper.py # Reddit data collection
├── persona_builder.py # Gemini LLM integration and prompt
└── utils.py # File-saving and helper functions


## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/reddit-persona.git
cd reddit-persona
Create and activate a virtual environment (recommended):
python3 -m venv tfenv
source tfenv/bin/activate  # Linux/macOS
# OR
.\tfenv\Scripts\activate   # Windows
Install dependencies:
pip install -r requirements.txt
Create a .env file in the root directory:
REDDIT_CLIENT_ID=your_reddit_app_client_id
REDDIT_CLIENT_SECRET=your_reddit_app_client_secret
REDDIT_USER_AGENT=script:redit-persona:v1.0 (by /u/your_reddit_username)
GOOGLE_API_KEY=your_gemini_api_key
Note: Do not commit your .env file. Ensure it is listed in .gitignore.
Usage

Edit main.py and set the target Reddit username:

username = "kojied"
Run the script:

python main.py
Upon success, a structured persona file will be saved to:

users/kojied_persona.txt
Sample Output

The output file includes sections such as:

Age, Occupation, Location (if inferable)
Interests and Hobbies
Motivations, Frustrations, Goals
Writing Style and Personality Traits
Cited Reddit links used for each inference
Example snippet:

User Persona for u/kojied

Age: Estimated 22–30
Occupation: Likely a software engineer or student
Interests: Privacy tools, Linux, anime
Frustrations: Moderation inconsistencies

Cited from: https://www.reddit.com/r/linux/comments/abc123/example
Gemini API Considerations

The script uses Gemini's free-tier access. If you hit a rate limit or quota error (HTTP 429), wait a few minutes and re-run the script. To avoid this:

Use the gemini-1.5-flash-latest model (configured in persona_builder.py)
Limit the number of posts/comments if needed
Troubleshooting

Empty output file: Gemini may have returned a blank response due to rate limits or malformed input
429 Errors: You’ve exceeded your daily or per-minute quota. Switch to a new API key or use a lighter model
PRAW errors: Check that your Reddit API credentials are correct and the user exists
License

This project is provided as part of a coding assignment. All intellectual property belongs to the author unless the assignment is accepted and ownership is transferred as part of the hiring process.

Contact

For any questions, please reach out via Internshala or the official hiring channel at BeyondChats.


---

You can now paste this directly into your `README.md` file in the project root. Let me know if you'd like help converting this into PDF format, or cleaning your repo before pushing to GitHub.
