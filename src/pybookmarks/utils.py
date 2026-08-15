"""
Utilities
"""


import json
import os.path


def get_accounts():
    path = os.path.expanduser("~/.config/google-chrome/Local State")
    with open(path) as file_handle:
        data = json.load(file_handle)
    return data["profile"]["info_cache"]
