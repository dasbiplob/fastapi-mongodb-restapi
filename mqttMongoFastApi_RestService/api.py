from fastapi import FastAPI
from mongoDB.mongodb_client import init_mongodb_client
from models.model import Message

app = FastAPI()

@app.get("/messages")
async def get_messages():
    collection = init_mongodb_client()
    messages = []
    async for document in collection.find():
        message = Message(**document)
        serialized_message = message.to_dict()
        messages.append(serialized_message)
    return messages
