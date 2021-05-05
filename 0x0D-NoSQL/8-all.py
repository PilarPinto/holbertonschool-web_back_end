#!/usr/bin/env python3
"""List all documents in a collection"""


def list_all(mongo_collection):
    """Lists all documents in a collection
    Args: mongo_collection
    """
    return ([*mongo_collection.find()] if mongo_collection.find().count() > 0
            else [])
