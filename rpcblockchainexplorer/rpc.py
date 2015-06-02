"""
RPC connection details.
"""

# use python-bitcoinlib for RPC
import bitcoin

from .config import BITCOIN_MODE

def get_bitcoin_rpc_client():
    """
    Create a new RPC connection to bitcoind.
    """

    # use local bitcoind config from ~/.bitcoin/bitcoin.conf
    bitcoin_rpc_client = bitcoin.rpc.Proxy()

    return bitcoin_rpc_client
