"""
This script runs the FlaskAppAML application using a development server.
"""

from os import environ
from FlaskAppAML import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5502'))
    except ValueError:
        PORT = 5502
    app.run(HOST, PORT, debug=True)
