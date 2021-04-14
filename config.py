import os


class Config(object):
    SECRET_KEY = os.environ.get('0123456') or '01234567'
mongodb+srv://PY-aquesidilly:Love19901@cluster0.xmxi1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority