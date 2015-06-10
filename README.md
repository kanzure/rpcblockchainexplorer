# RPC-based Blockchain Explorer

This is a small python application that runs a web server for locally exploring
a blockchain using RPC connectivity.

# configuration

$HOME/.bitcoin/bitcoin.conf needs to define rpcuser and rpcpassword.

Optionally, rpcconnect (rpc listening address) and rpcport may be defined.

Notably, the documented recommended command line for alphad configures it to
listen on a nondefault port.

The BCE_ADDR and BCE_PORT environment variables can be used to override the
default http server address and port binding of 127.0.0.1:5000.

# license

BSD
