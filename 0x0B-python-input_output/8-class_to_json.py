#!/usr/bin/python3
# Json serialization
"""JSON Serialization"""
import json


def class_to_json(obj):
    """convert to json string and return the dictionary rep"""
    return json.dumbs(obj)
