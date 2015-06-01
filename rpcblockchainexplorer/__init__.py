# coding: utf-8

"""
rpcblockchainexplorer
~~~~~~~~~~~~~~~~~~~~~

This is a small web application that operates as a blockchain explorer using
only an RPC connection to bitcoind.
"""

__title__ = "rpcblockchainexplorer"
__version__ = "0.0.1"
__build__ = 0x000001
__author__ = "Bryan Bishop <kanzure@gmail.com>"
__license__ = "BSD"
__copyright__ = "Copyright 2015 Bryan Bishop"

# set default logging handler to avoid "No handler found" warnings
import logging
try:  # python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
