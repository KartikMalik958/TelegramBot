import os

# MongoDB URI (replace with your actual MongoDB Atlas URI)
MONGO_URI =os.getenv('MONGO_URI',"mongodb+srv://myuser:myuser@cluster0.rk9fa.mongodb.net/lkartiko?retryWrites=true&w=majority&ssl=true")

# Telegram Bot Token (replace with your actual Telegram bot token)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '7692737561:AAGuHSxBRwoj6NRzPhE6gb6r4nHaG0hwY5E')

# Gemini API Key (if you're using Gemini for AI-powered responses)
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
