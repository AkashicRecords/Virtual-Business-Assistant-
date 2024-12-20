"""Gmail OAuth credentials configuration."""
import json
import os

# Get the directory of the current file
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(CURRENT_DIR, '../resources/credentials.json')

# Load credentials from the JSON file
with open(CREDENTIALS_PATH) as f:
    credentials = json.load(f)

# Gmail OAuth2 credentials
GMAIL_CLIENT_ID = credentials['installed']['client_id']
GMAIL_CLIENT_SECRET = credentials['installed']['client_secret']
GMAIL_REDIRECT_URI = credentials['installed']['redirect_uris'][0]

# Additional configuration
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify'
]

# Token storage path
TOKEN_PATH = os.path.join(CURRENT_DIR, '../resources/token.json')

# Add this to your existing secrets.py
OPENAI_API_KEY = "your-openai-api-key-here"  # Replace with your actual OpenAI API key
 