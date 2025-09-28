import pymongo
from pymongo import MongoClient
import os

# MongoDB connection settings
MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME = "hospital_db"

class Database:
    client: MongoClient = None
    database = None

# Create global database instance
db = Database()

def connect_to_mongo():
    """Create database connection"""
    try:
        db.client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
        db.database = db.client[DATABASE_NAME]
        
        # Test the connection
        db.client.admin.command('ping')
        print(f"✅ Connected to MongoDB at {MONGO_URL}")
        print(f"✅ Using database: {DATABASE_NAME}")
        
        # Create indexes for users collection (only if MongoDB is available)
        try:
            users_collection = db.database.users
            users_collection.create_index("username", unique=True)
            users_collection.create_index("email", unique=True)
            print("✅ Database indexes created")
        except Exception as idx_error:
            print(f"⚠️  Could not create indexes: {idx_error}")
        
        return True
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {e}")
        print("❌ Make sure MongoDB is running on localhost:27017")
        return False

def close_mongo_connection():
    """Close database connection"""
    if db.client:
        db.client.close()
        print("🔌 Disconnected from MongoDB")

def get_database():
    """Get database instance"""
    if db.client is None or db.database is None:
        print("❌ Database not connected")
        return None
    return db.database
