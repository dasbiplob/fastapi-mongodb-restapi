import json
import logging
from pymongo import MongoClient

# MongoDB connection details
mongodb_host = 'localhost'
mongodb_port = 27017
mongodb_database = 'mydatabase'
mongodb_collection = 'your_collection'

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# MongoDB client initialization
def init_mongodb_client():
    try:
        client = MongoClient(mongodb_host, mongodb_port)
        db = client[mongodb_database]
        collection = db[mongodb_collection]
        # Test the connection
        collection.find_one()
        logger.info('Connected to MongoDB')
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        return collection
    except Exception as e:
        logger.error(f'Failed to connect to MongoDB: {str(e)}')
        return None

# Insert message into MongoDB
async def insert_message(collection, payload):
    try:
        document = json.loads(payload)
        collection.insert_one(document)
        logger.info('Message inserted into MongoDB')
    except Exception as e:
        logger.error(f'Failed to insert message into MongoDB: {str(e)}')
