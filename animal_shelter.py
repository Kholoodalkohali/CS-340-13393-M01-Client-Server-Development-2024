from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self):
        # Connection Variables
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31517
        DB = 'AAC'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert a document into the collection."""
        if data:
            try:
                result = self.collection.insert_one(data)
                return True  # Successful insert
            except Exception as e:
                print(f"An error occurred: {e}")
                return False  # Failed insert
        else:
            raise ValueError("Data cannot be None or empty")

    def read(self, query):
        """Query for documents from the collection."""
        if query is not None:
            try:
                cursor = self.collection.find(query)
                return list(cursor)  # Convert cursor to list of documents
            except Exception as e:
                print(f"An error occurred: {e}")
                return []  # Return empty list on error
        else:
            raise ValueError("Query cannot be None")

    def update(self, query, update_data):
        """Update documents in the collection."""
        if query is not None and update_data is not None:
            try:
                result = self.collection.update_many(query, {"$set": update_data})
                return result.modified_count  # Return number of modified documents
            except Exception as e:
                print(f"An error occurred: {e}")
                return 0  # Return 0 on error
        else:
            raise ValueError("Query and update_data cannot be None")

    def delete(self, query):
        """Delete documents from the collection."""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count  # Return number of deleted documents
            except Exception as e:
                print(f"An error occurred: {e}")
                return 0  # Return 0 on error
        else:
            raise ValueError("Query cannot be None")

