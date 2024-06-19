#!/usr/bin/env python3
""" module for exercise.py """

import redis
from typing import Union
from uuid import uuid4


class Cache:
    """ Cache class """
    def __init__(self):
        """ Initialize the cache """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in the cache """
        randomKey = str(uuid4())
        self._redis.set(randomKey, data)
        return randomKey
