#!/usr/bin/env python3
""" task 8 module """


def list_all(mongo_collection):
    """ List all documents in Python """
    return [doc for doc in mongo_collection.find()]
