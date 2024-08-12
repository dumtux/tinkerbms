import inspect
from abc import ABC, abstractmethod

from tinkerbms.battery import Battery


def test_battery():
    assert inspect.isabstract(Battery)

