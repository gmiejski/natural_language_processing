def echo(fn):
    def wrapped(*v, **k):
        print 'starting function: ' + fn.__name__
        return fn(*v, **k)

    return wrapped