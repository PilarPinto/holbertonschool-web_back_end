#!/usr/bin/env python3
'''Encrypt with hash and validate pass'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''returns a hashed password'''
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''validate hashed vs provided password'''
    password = password.encode("utf-8")
    return True if bcrypt.checkpw(password, hashed_password) else False
