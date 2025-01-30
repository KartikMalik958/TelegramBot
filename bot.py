from telegram.ext import Application, CommandHandler
from database import register_user

# Command handler for the /start command
async def start(update, context):
    first_name = update.message.from_user.first_name
    username = update.message.from_user.username
    chat_id = update.message.chat_id

    # Register the user in MongoDB
    register_user(chat_id, first_name, username)

    # Send a welcome message to the user
    await update.message.reply_text(f"Welcome, {first_name}! How can I assist you today?")

def main():
    # Replace 'your_bot_token' with your actual bot token
    application = Application.builder().token("7692737561:AAGuHSxBRwoj6NRzPhE6gb6r4nHaG0hwY5E").build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Start polling for new updates (to listen for messages)
    application.run_polling()

if __name__ == "__main__":
    main()
