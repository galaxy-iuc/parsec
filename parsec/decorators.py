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
        except Exception, e:
            print e

@wrapt.decorator
def dict_output(wrapped, instance, args, kwargs):
    #TODO enhance
    output = wrapped(*args, **kwargs)
    print(json.dumps(output, indent=4))
