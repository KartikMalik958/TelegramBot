from flask import Flask
from bot import main

app = Flask(__name__)

@app.route('/')
def index():
    return "Telegram Bot is running!"

if __name__ == "__main__":
    main()  # Start the bot
    app.run(host="0.0.0.0", port=5000)  # Run the Flask app (for web interface)
