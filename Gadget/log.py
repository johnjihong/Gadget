"""Loggin configuration."""


import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(threadName)12s %(name)8s %(levelname)8s %(message)s',
    datefmt='%b-%d %H:%M:%S'
)

# Name the logger after the package.
logger = logging.getLogger(__package__)