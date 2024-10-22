#!/usr/bin/env python3
"""
Function inserting new document in collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """New document in collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
