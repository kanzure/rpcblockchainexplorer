"""
Web application gears.
"""

# use default logging framework
import logging

from flask import (
    # need to make a flask application
    Flask,

    # request handler thing
    g,
)

# and the application must have a name
from .config import DEFAULT_APP_NAME

# used to create an rpc client on every request
from .rpc import get_bitcoin_rpc_client

# get the only blueprint that matters in this app
from .api import api

DEFAULT_BLUEPRINTS = [
    api,
]

def create_app(config=None, app_name=DEFAULT_APP_NAME, blueprints=DEFAULT_BLUEPRINTS):
    """
    Construct a flask application object.
    """

    app = Flask(app_name)

    configure_app(app, config)
    configure_logging(app)
    configure_hook(app)
    configure_blueprints(app, blueprints)

    return app

def configure_app(app, config=None):
    """
    Really simple configuration for flask applications.
    """

    if config:
        app.config.from_object(config)
    elif not app.config.get("testing"):
        app.debug = True

def configure_logging(app):
    """
    Use python logging.
    """

    # no reason to hide messages yet
    app.logger.setLevel(logging.DEBUG)

def configure_hook(app):
    """
    Setup the before_request hook.
    """

    # http://flask.pocoo.org/docs/0.10/api/#flask.Blueprint.before_request
    @app.before_request
    def before_request():
        """
        Make a new bitcoin RPC client instance for every request.
        """

        # store client on request context object
        g.bitcoin_rpc_client = get_bitcoin_rpc_client()

def configure_blueprints(app, blueprints):
    """
    Setup flask blueprints on the flask application.
    """

    for blueprint in blueprints:
        app.register_blueprint(blueprint)
