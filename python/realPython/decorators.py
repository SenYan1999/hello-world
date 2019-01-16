import functools
import time
import random

################        Debug       ########################
def debug(func):
    @functools.wraps(func)

    def wrap_debug(*args,**kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k,v in kwargs.items()]
        signature = ",".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args,**kwargs)
        print(f"The return value is {value}")
        return value

    return wrap_debug

################        Timer       ########################

def timer(func):
    @functools.wraps(func)
        
    def wrap_timer(*args,**kwargs):
        start_time = time.perf_counter()
        value = func(*args,**kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__} in {run_time} secs")
        return value

    return wrap_timer

################        Do Twice        ####################
def do_twice(func):
    @functools.wraps(func)

    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        print("hi")
        return func(*args,**kwargs)
    
    return wrapper_do_twice

#################       Slow Down       ####################
def slow_down(func):
    @functools.wraps(func)

    def wrap_slowdown(*args,**kwargs):
        time.sleep(1)
        return func(*args,**kwargs)

    return wrap_slowdown

##################      Register Plugin ####################
PLUGINS = dict()

def register(func):
    #register a func in a dict to randomely get
    PLUGINS[func.__name__] = func
    return func

