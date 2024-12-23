from flask import Flask
import time


def delay(function):
    def wrap():
        time.sleep(2)
        function()

    return wrap

@delay
def hello():
    print("HELLO")

hello()