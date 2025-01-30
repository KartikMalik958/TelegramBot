# Telegram AI Chatbot with MongoDB and Gemini API  

This is a Telegram bot that supports user registration, chat history storage, image/file analysis, and web search functionality. The bot is built using Python, the `python-telegram-bot` library, and MongoDB for storing user data and chat history. The Gemini API is used for AI-powered responses.

## **Features**
- 📌 **User Registration**: Saves user information (first name, username, chat ID) in MongoDB.
- 🧠 **AI Chat (Gemini API)**: Responds to user queries using Google's Gemini API.
- 🖼️ **Image/File Analysis**: Accepts images/files and provides AI-powered descriptions.
- 🌐 **Web Search**: Allows users to perform web searches and get summarized results.
- 💾 **Chat History Storage**: Stores user queries and bot responses in MongoDB.

---

📂 Telegram-AI-Bot
│── bot.py                 # Main bot file
│── database.py            # MongoDB connection & functions
│── image_analysis.py      # Image and file analysis (Gemini API)
│── web_search.py          # Web search functionality
│── config.py              # Stores environment variables
│── requirements.txt       # Required dependencies
│── README.md              # Project documentation

