import pymongo
from pymongo import MongoClient

# MongoDB URI
MONGO_URI = "mongodb+srv://myuser:myuser@cluster0.rk9fa.mongodb.net/lkartiko?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client['lkartiko']
users_collection = db['users']

def register_user(chat_id, first_name, username):
    user = {
        "chat_id": chat_id,
        "first_name": first_name,
        "username": username,
    }
    # Insert or update the user
    users_collection.update_one({"chat_id": chat_id}, {"$set": user}, upsert=True)

def save_chat_history(chat_id, message_text):
    chat_history = {
        "chat_id": chat_id,
        "message_text": message_text,
    }
    # Store chat history
    db.chat_history.insert_one(chat_history)
