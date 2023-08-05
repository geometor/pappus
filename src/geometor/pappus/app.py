"""
run the main app
"""
from .pappus import Pappus


def run() -> None:
    reply = Pappus().run()
    print(reply)
