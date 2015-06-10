import os

from rpcblockchainexplorer.flaskapp import create_app
app = create_app()
app.run(debug=True, host=os.environ.get('BCE_ADDR','127.0.0.1'), port=int(os.environ.get('BCE_PORT','5000')))
