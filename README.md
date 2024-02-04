# HTTPServerLite
### Pure Python implementation of an HTTP server using sockets

## Usage Guide
- Install the package
- Import the HTTPServerLite class
- Start the server by creating an instance of the HTTPServerLite class (or subclass) and call the .listen() method

```python
from http_server_lite import HTTPServerLite
HTTPServerLite().listen()
```

## Intended Usage
This package is NOT intended to serve as a production webserver. This is designed for easy subclassing and working with the HTTP protocol. This package is aimed at developers who want to subclass HTTPLite and utilize the helper functions available to create development/testing servers.

## What's Not Included
- Any form of security or header checking