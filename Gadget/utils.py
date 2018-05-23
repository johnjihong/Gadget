"""Utility functions"""


def display(widget, visible):
    widget.layout.display = '' if visible else 'none'
    widget.layout.display = 'visible' if visible else 'hidden'
