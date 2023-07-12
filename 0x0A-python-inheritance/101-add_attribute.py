#!/usr/bin/python3
"""
attribute addition Module
"""


def add_attribute(obj, obj_name, value):
    """adds attribute to object
    args:
        obj: class object
        obj_name: object name
        value: value of attribute
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, obj_name, value)
