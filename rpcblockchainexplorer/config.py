"""
Application configuration.
"""

import os

# use python-bitcoinlib
import bitcoin

DEFAULT_BITCOIN_MODE = "regtest"

# Set python-bitcoinlib mode to the same as bitcoind's mode, based on
# environment variable and a default in its absence.
BITCOIN_MODE = os.environ.get("BITCOIN_MODE", DEFAULT_BITCOIN_MODE)

# python-bitcoinlib has a mode :-(
bitcoin.SelectParams(BITCOIN_MODE)

# flask application name
DEFAULT_APP_NAME = "rpcblockchainexplorer"
