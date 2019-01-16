#######     Test        ######
from decorators import register
from decorators import PLUGINS

import random

@register
def hello(name):
    print(f"Hello,{name}")

@register
def yo_hello(name):
    print(f"Yo!!!{name}, nice to meet you")

@register
def be_awesome(name):
    print(f"Hi!{name}, together we are the awesomist!")

def random_greet(name):
    greeter,greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter}!")
    return greeter_func(name)

name = "Mike"
random_greet(name)
