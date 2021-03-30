#!/usr/bin/env python3
'''Filter logs with regex'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Filter definition using Regex'''
    for f in fields:
        message = re.sub(f + "=.*?" + separator,
                         f + "=" + redaction + separator, message)
    return message
