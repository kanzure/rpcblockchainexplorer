# RPC-based Blockchain Explorer

This is a small python application that runs a web server for locally exploring
a blockchain using RPC connectivity.

# configuration

$HOME/.bitcoin/bitcoin.conf needs to define rpcuser and rpcpassword.

Optionally, rpcconnect (rpc listening address) and rpcport may be defined.

Notably, the documented recommended command line for alphad configures it to
listen on a nondefault port.

# license

BSD
