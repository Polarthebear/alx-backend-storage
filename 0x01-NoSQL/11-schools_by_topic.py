#!/usr/bin/env python3
"""
Module for Task 11
"""


def schools_by_topic(mongo_collection, topic):
    """Return list of school having specific topic"""
    filter_topic = {
            'topics': {
                '$elemMatch': {
                    '$eq': topic,
                },
            },
    }
    return [doc for doc in mongo_collection.find(filter_topic)]
