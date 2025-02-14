#!/usr/bin/python3
"""This module to_json_string() file"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Parameters
    ----------
       my_obj : object

    Return
    ------
        str
            The JSON representation of an object (string)
    """
    return json.dumps(my_obj)
