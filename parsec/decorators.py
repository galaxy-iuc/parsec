import json
from .io import error

def bioblend_exception(func):
    def dec(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception, e:
            try:
                error(json.loads(e.body)['err_msg'])
            except:
                error(e)
    return dec
