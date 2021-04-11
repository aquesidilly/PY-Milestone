import os


class Config(object):
    SECRET_KEY = os.environ.get('0123456') or '01234567'
