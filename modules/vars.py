import os

API_ID    = os.environ.get("API_ID", "24812063")
API_HASH  = os.environ.get("API_HASH", "e7ee18967768d95aeb7f2f6674e7da4c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
