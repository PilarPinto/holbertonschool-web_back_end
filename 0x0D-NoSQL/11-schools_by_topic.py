#!/usr/bin/env python3
"""Returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having specific topic
    """
    return [i for i in mongo_collection.find({"topics": topic})]
