#!/usr/bin/env python3
'''Filter logs with regex'''
import re
from typing import List

patterns = {
    "password": "[a-zA-Z]*",
    "date_of_birth": r"([0-9]{2}\/){2}[0-9]{4}",
    "name": "[a-zA-Z]*",
    "email": r"[a-zA-Z]*@[a-zA-Z]*\.[a-zA-Z]*",
}


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Filter definition using Regex'''
    for f in fields:
        message = re.sub(f + "=" + patterns[f] + separator + "{1}",
                         "{}={}{}".format(f, redaction, separator), message)
    return message
