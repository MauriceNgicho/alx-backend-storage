#!/usr/bin/env python3
"""
A function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection

    Args:
        mongo_collection: The pymongo collection object
        **kwargs: Key-value pairs to insert as the new document

    Returns:
        The _id of the new document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
