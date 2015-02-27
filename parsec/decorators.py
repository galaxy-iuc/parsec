import json
import wrapt
from .io import error

@wrapt.decorator
def bioblend_exception(wrapped, instance, args, kwargs):
    try:
        return wrapped(*args, **kwargs)
    except Exception, e:
        try:
            error(json.loads(e.body)['err_msg'])
        except:
            print e
