
def debug():
    import inspect
    caller_name = inspect.stack()[1][3]
    print("[DEBUG]: enter {}()".format(caller_name))

def hello():
    debug()
    print('hello')

def goodby():
    debug()
    print('goodby')

if __name__ == '__main__':
    hello()
    goodby()