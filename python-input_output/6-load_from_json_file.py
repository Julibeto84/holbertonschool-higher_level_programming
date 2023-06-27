#!/usr/bin/python3
"""I'm so tired"""


import json


def load_from_json_file(filename):
    """Loading Loading loading"""
    with open(filename, 'r', encoding='utf-8') as f:
        return (json.load(f))
