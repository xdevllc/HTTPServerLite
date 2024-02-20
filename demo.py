import logging
from HTTPServerLite import HTTPLite

# Define the server object
server = HTTPLite("index.html")

# Configure logging for the application
logging.basicConfig(level=logging.INFO)
server.start()

