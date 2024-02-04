import logging

from HTTPServerLite import HTTPLite

server = HTTPLite()


# Configure logging for the application
logging.basicConfig(level=logging.INFO)

server.start()