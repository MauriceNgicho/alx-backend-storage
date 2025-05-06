#!/usr/bin/env python3
"""
A function that updates topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the school name

    Args:
        mongo_collection: The pymongo collection object
        name (str): The school name to update
        topics (list): List of strings representing the new topics

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
