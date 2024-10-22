#!/usr/bin/env python3
"""
Function changes all topics of a school document based on name
"""


def update_topics(mongo_collection, name, topics):
    """Changes topics of a collection documents based on name"""
    mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
    )
