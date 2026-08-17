"""CRUD operations for the Animal Shelter MongoDB collection."""
from pymongo import MongoClient

class AnimalShelter:
    """Provide Create, Read, Update, and Delete operations."""

    def __init__(self, username, password):
        """Initialize the MongoDB connection."""

        host = "localhost"
        port = 27017
        database_name = "aac"
        collection_name = "animals"

        self.client = MongoClient(
            host=host,
            port=port
        )

        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def create(self, data):
        """Insert a document into the animals collection."""
        if not isinstance(data, dict) or not data:
            return False
        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except Exception as error:
            print(f"Create error: {error}")
            return False

    def read(self, query):
        """Return documents that match the supplied query."""
        if not isinstance(query, dict):
            return []
        try:
            return list(self.collection.find(query))
        except Exception as error:
            print(f"Read error: {error}")
            return []

    def update(self, query, new_values):
        """Update documents matching the supplied query."""
        if not isinstance(query, dict) or not query:
            return 0
        if not isinstance(new_values, dict) or not new_values:
            return 0
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as error:
            print(f"Update error: {error}")
            return 0

    def delete(self, query):
        """Delete documents matching the supplied query."""
        if not isinstance(query, dict) or not query:
            return 0
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as error:
            print(f"Delete error: {error}")
            return 0
