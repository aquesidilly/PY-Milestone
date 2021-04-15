import os


class Config(object):
    SECRET_KEY = os.environ.get('WYrd3mUMyl') or 'WYrd3mUMyl'
mongodb+srv://PY-aquesidilly:Love19901@cluster0.xmxi1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority