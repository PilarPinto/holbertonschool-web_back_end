#!/usr/bin/env python3
"""
Log stats - new version
"""


from pymongo import MongoClient
import pymongo


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    number_documents = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f"{number_documents} logs")
    print("Methods:")
    for method in methods:
        n_docs = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {n_docs}")
    number_docs_path = collection.count_documents({
        "$and": [
            {"method": "GET"},
            {"path": "/status"}
        ]
    })
    print(f"{number_docs_path} status check")
    print("IPs:")
    ips = collection.aggregate([
        {"$group": {"_id": "$ip", "myCount": {"$sum": 1}}},
        {"$sort": {"myCount": -1}},
        {"$limit": 10}
    ])
    for x in ips:
        print(f"\t{x['_id']}: {x['myCount']}")
