#!/usr/bin/env python3
"""
Function that returns the list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools where the topic is present in their 'topic' field

    Args:
        mongo_collection: The pymongo collection object
        topic (str): The topic to search for

    Returns:
        List of documents matching the topic
    """
    return mongo_collection.find({"topics": topic})
