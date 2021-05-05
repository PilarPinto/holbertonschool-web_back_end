#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """Inserts based on kwargs
    """
    id_ = mongo_collection.insert(kwargs)
    return id_
